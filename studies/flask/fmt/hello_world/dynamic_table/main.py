import logging
import json
from config import parser
from flask import Flask, render_template
from db.qdb import QDB

cfg = parser.parse_known_args()[0]


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s',
    level=cfg.log_level,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(cfg.log_file, 'a+', encoding='utf-8')
    ]
)

log = logging.getLogger()
app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    db_object = QDB('db/random_data.db')
    data_values = db_object.get_all_records()
    headers = db_object.get_column_names()


    return render_template(
        'index.html',
        headers=headers,
        data_values=data_values,
        title='Ze Table w00t!'
    )


if __name__ == '__main__':
    log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')
    app.run(host='0.0.0.0', port=8086, debug=True)
