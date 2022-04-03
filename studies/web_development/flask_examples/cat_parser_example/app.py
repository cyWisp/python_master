import logging
import os

from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename

# TODO: move to cli_tools
import catalina_parser

app = Flask(__name__)

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploaded')

# Make directory if "uploaded" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def upload():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def process_files():
    try:
        logging.debug(request.files)
        if 'catalina.log' not in request.files:
            return 'No file part'

        files = request.files.getlist('catalina.log')

        filenames = []
        for file in files:
            try:
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filename)
                    filenames.append(filename)
                    logging.debug(f'Uploaded {filename}')
            except Exception as e:
                logging.exception(e)
                return str(e)

        if filenames:
            report = catalina_parser.parse_files(filenames)
            return render_template('downloads.html', filename=report.replace('generated/', ''))

        else:
            return 'No files to process.'

    except Exception as e:
        return str(e)


@app.route('/generated/<filename>')
def generated(filename):
    # return send_file(filename, mimetype='application/vnd.ms-excel')
    # TODO: cleanup generated folder
    return send_from_directory('generated', filename, mimetype='application/vnd.ms-excel')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
