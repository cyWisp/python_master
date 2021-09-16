#!/usr/bin/env python
import functools
import logging



logging.basicConfig(
	format='%(asctime)s: %(message)s',
	datefmt='%H:%M:%S',
	level=logging.INFO,
	handlers=[logging.StreamHandler()]
)


def get_type(struct):
	return str(type(struct)).split("'")[1]


def log_deco(func):
	@functools.wraps(func)
	def log_wrapper(*args, **kwargs):
		struct = func(*args, **kwargs)
		log_title = f'[+] -----| {func.__name__}() -> {get_type(struct)} | length: {len(struct)} |-----'
		logging.info(log_title)
		logging.info(f'[|]')	
		if isinstance(struct, dict):
			for k, v in struct.items():
				if isinstance(v, dict):
					logging.info(f'[+] key: {k} | value type: {get_type(v)} | length: {len(v)}')
					logging.info('[|]')
					for k, v in v.items():
						logging.info(f'[+] --- {k}: {v}')
					logging.info('[|]')
				if isinstance(v, list):
					logging.info(f'[+] key: {k} | value type: {get_type(v)} | length: {len(v)}')
					logging.info('[|]')
					for i in v:
						logging.info(f'[+] --- {i}')
					logging.info('[|]')
				if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
					logging.info(f'[+] key: {k} | value type: {get_type(v)}')
					logging.info('[|]')
					logging.info(f'[+] --- {str(v)}')
					logging.info('[|]')	
		if isinstance(struct, list):
			for i in struct:
				logging.info(f'[+] {str(i)}')
			logging.info('[|]')
		if isinstance(struct, str) or isinstance(struct, int) or isinstance(struct, float):
			logging.info(f'[+] {struct}')
		end_bar = '[+]' + ''.join(['-' for x in range(len(log_title) - 3)])
		logging.info(end_bar)
		return struct
	return log_wrapper
