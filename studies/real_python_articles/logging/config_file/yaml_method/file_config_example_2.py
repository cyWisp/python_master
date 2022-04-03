#!/usr/bin/env python
import logging, logging.config, yaml

if __name__ == '__main__':
	with open('./config.yaml', 'r') as f:
		config = yaml.safe_load(f.read())
		logging.config.dictConfig(config)

	logger = logging.getLogger(__name__)

	logger.debug('This is a debug message...')
