import logging
from slicemypdf.slicemypdf import Extractor

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)


if __name__ == '__main__':

    table = Extractor(pdf_loc='CONT200616108.pdf', page=2)

    extracted_table = table.extract(FS_flag=True)

    log.info(extracted_table.keys())