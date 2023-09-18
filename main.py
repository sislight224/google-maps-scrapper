from bose.launch_tasks import launch_tasks
from bose import LocalStorage

from src.config import number_of_scrapers, queries
from src import tasks_to_be_run
import csv
from flask import Flask, send_from_directory, request
from flask_cors import CORS
import pydash

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"], "headers": "Content-Type"}})


msg = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

def print_pro_bot():
    global msg
    print(msg) 

@app.route('/api/generate', methods=['GET'])
def generate():

    keyword = request.args.get('keyword')
    queries[0]['keyword'] = keyword
    launch_tasks(*tasks_to_be_run)
    
    return pydash.kebab_case(keyword)

@app.route('/api/download_csv', methods=['GET'])
def download_csv():

    keyword = request.args.get('keyword')
    # Process the received data as needed
    filename = pydash.kebab_case(keyword) + '.csv'  # The name of the JSON file to be downloaded
    directory = 'output'  # The directory where the JSON file is located
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/api/download_json', methods=['GET'])
def download_json():

    keyword = request.args.get('keyword')
    # Process the received data as needed
    filename = pydash.kebab_case(keyword) + '.json'  # The name of the JSON file to be downloaded
    directory = 'output'  # The directory where the JSON file is located
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == "__main__":

    # count = LocalStorage.get_item('count', 0)
    # queries[0]['keyword'] = 'eee'
    # print(queries[0]['keyword'])

    # launch_tasks(*tasks_to_be_run)

    app.run(debug=True)

    # if count % 5 == 0:
    print_pro_bot()
