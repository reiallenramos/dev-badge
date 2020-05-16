from flask import Flask
from flask import jsonify, abort
import importlib
from flask_cors import CORS, cross_origin
scraper = importlib.import_module('scraper', package='scraper')

app = Flask(__name__)
cors = CORS(app)

@app.route('/<username>', methods=['GET'])
@cross_origin(supports_credentials=True)
def ping(username):
  colors = scraper.scrape(username)
  if type(colors) is not dict:
    abort(404)

  return jsonify(colors)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
