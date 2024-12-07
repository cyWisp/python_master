import sys
import json
import logging
import configargparse


parser = configargparse.get_argument_parser(
    description='Justen\'s Super Gnarly Coding Assessment',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',
                    help='The logging level of the application.')

parser.add_argument('-f', '--data-file', type=str, required=False, default='data.json',
                    help='The data to be read.')

parser.add_argument('-o', '--output-file-path', type=str, required=False, default='output.csv',
                    help='The path of the output csv file.')

parser.add_argument('-t', '--product-type', type=str, required=False, default='food',
                    help='Product type to filter for: [ food | sport | pets ]')


cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)

log = logging.getLogger(__name__)
log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


class SuperMegaDeathParser:
    def __init__(
        self,
        file_path: str,
        output_file_path: str
    ) -> None:

        self.file_content = self.read_file(file_path)
        self.output_file_path, self.output_data = output_file_path, []

    @staticmethod
    def read_file(file_name):
        try:
            logging.info(f'Reading {file_name}')

            with open(file_name, 'r') as f:
                return json.load(f)

        except (FileNotFoundError, IOError) as e:
            log.error(f'Unable to read file:\n{e}. Exiting...')
            sys.exit(1)

    def output_csv(self, file_name):
        try:
            logging.info(f'Writing {file_name}')

            with open(file_name, 'w') as f:
                f.write('Item, Current Price' + '\n')

                for d in self.output_data:
                    f.write(d + '\n')

        except (FileNotFoundError, IOError) as e:
            log.error(f'Unable to read file:\n{e}. Exiting...')
            sys.exit(1)

    def show_all_products(self):
        try:
            log.info('Current inventory:')

            for product in self.file_content['inventory']:
                log.info(json.dumps(product, indent=4))

        except (KeyError, TypeError) as e:
            log.error(e)

    def get_products_by_type(self, product_type: str) -> list:
        try:
            log.info(f'Gathering all products of type {product_type.upper()}.')
            return [x for x in self.file_content['inventory'] if x['type'] == product_type.upper()]

        except (KeyError, TypeError) as e:
            log.error(e)

    def get_item_summary(self):
        for item in self.file_content['inventory']:
            price = item['price'] - (item['price'] * item['discount']) \
                                   if item['price'] else item['price']

            self.output_data.append(f'{item["name"]}, {price}')
            log.info(f'Item: {item["name"]} | Price: {price}')

    # def get_csv_format(self):
    #     try:
    #         log.info(f'Writing data to {self.output_file_path}')
    #
    #         self.output_data['headers'] = ','.join([x for x in list(self.file_content['inventory'][0].keys())])
    #         self.output_data['data'] = [','.join([str(x) for x in list(y.values())])
    #                                     for y in self.file_content['inventory']]
    #
    #     except IOError as e:
    #         log.error(f'Error writing output file:\n{e}')

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with SuperMegaDeathParser(cfg.data_file, cfg.output_file_path) as p:
        p.show_all_products()
        log.info(json.dumps(p.get_products_by_type(cfg.product_type), indent=4))

        p.get_item_summary()
        p.output_csv(cfg.output_file_path)


