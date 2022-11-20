#!/usr/bin/env python
import requests
import os
import hashlib
import shutil

from requests.exceptions import ConnectionError, HTTPError, Timeout
from bs4 import BeautifulSoup
from PIL import Image

from module_tester import log

class ImageDownloader:
	def __init__(
			self,
			categories: any = None,
			images_path: str = 'images',
			temp_path: str = 'temp',
			target_width: str = '800w',
			target_height: int = 600
	) -> None:
		self.categories = categories
		self.images_path = images_path
		self.temp_path = temp_path
		self.target_width, self.target_height = target_width, target_height
		self.images = dict()

		self.create_dirs_if_not_exist()
		self.get_categories()
		self.download_images()
		self.delete_wrong_size()
		self.move_to_images()

	def create_dirs_if_not_exist(self):
		for d in [self.images_path, self.temp_path]:
			if not os.path.exists(d):
				log.debug(f'Directory {d} not found... creating it.')

				try:
					sub_dir = os.path.join(os.getcwd(), d)
					log.debug(f'Creating {sub_dir}')
					os.makedirs(sub_dir)
				except Exception as e:
					log.exception(e)

	@staticmethod
	def get_response(url):
		try:
			log.info(f'Requesting: {url}')
			response = requests.get(url)

			if response.status_code != 200:
				raise HTTPError(f'Request returned non-200 status: {response.status_code}')

			log.info(f'Request succeeded: {response.status_code}')
			return response

		except (ConnectionError, HTTPError, Timeout) as e:
			log.error(f'Error making HTTP request: {e}')

		except Exception as e:
			log.error(f'Some other error occurred: {e}')

	def get_source_sets(self, url, category):
		response = self.get_response(url)

		soup = BeautifulSoup(response.content, 'html.parser')
		source_sets = soup.findAll('img', attrs={'srcset': True})

		for s in source_sets:
			image_list = s['srcset'].split(",")
			for i in image_list:
				if i.split(' ')[-1] == self.target_width in i and 'premium' not in i:
					image_id = f'{category}-{i.split("-")[1]}'
					if image_id not in self.images:
						log.info(f'Image found: {i}')
						self.images[image_id] = i

	def get_categories(self):
		for category in self.categories:
			url = f"https://unsplash.com/s/photos/{category}"
			log.debug(f"URL: {url}")
			self.get_source_sets(url, category)

		log.info(f'Images found: {len(self.images)}')

	def download_images(self):
		log.info('Downloading new images.')

		for image_id, image_url in self.images.items():
			try:
				image = requests.get(image_url).content
				file_name = f"{self.temp_path}/{image_id}.jpg"

				with open(file_name, 'wb') as f:
					f.write(image)

				log.debug(f"Downloaded {file_name}")

			except Exception as e:
				log.error(f'Image download failed for {image_id}: {e}')

	def delete_wrong_size(self):
		log.info(f'Deleting any images that are not to specification ({self.target_width}).')

		for image in [f'{os.path.abspath(self.temp_path)}/{x}' for x in os.listdir(self.temp_path)]:
			i = Image.open(image)
			if i.height > self.target_height:
				log.debug(f'Removing: {image}')
				os.remove(image)

	@staticmethod
	def get_hash(file_path: str) -> str:
		h_sha256 = hashlib.sha256()

		with open(file_path, 'rb') as f:
			chunk = 0
			while chunk != b'':
				chunk = f.read(1024)
				h_sha256.update(chunk)

		return h_sha256.hexdigest()

	def get_image_hash_table(self, target_dir: str) -> dict:
		dir_contents = [f'{os.path.abspath(target_dir)}/{x}' for x in os.listdir(target_dir)]

		if len(dir_contents) > 0:
			return {f: self.get_hash(f) for f in [f'{os.path.abspath(target_dir)}/{x}' for x in os.listdir(target_dir)]}
		else:
			log.debug(f'No files to process in {target_dir}')

	def move_to_images(self):
		temp_hashes = self.get_image_hash_table(self.temp_path)

		if not temp_hashes:
			return
		else:
			for file_path, file_hash in temp_hashes.items():
				image_hashes = self.get_image_hash_table(self.images_path)
				target_file_path = os.path.join(os.path.abspath(self.images_path), file_path.split('/')[-1])

				try:
					assert len(os.listdir(self.images_path)) > 0, f'No images currently reside in {self.images_path}'

					if file_hash in image_hashes.values():
						os.remove(file_path)
						continue
					else:
						log.debug(f'Moving {file_path} to {target_file_path}')
						shutil.move(file_path, target_file_path)

				except (AttributeError, AssertionError) as f:
					os.error(f)
					log.debug(f'Moving {file_path} to {target_file_path}')
					shutil.move(file_path, os.path.join(os.path.abspath(self.images_path), file_path.split('/')[-1]))

		os.rmdir(self.temp_path)
