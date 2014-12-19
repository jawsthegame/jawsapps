import sys
sys.path.append('./bikerite/server')
sys.path.append('./explorify-server')

from flask import Flask

from bikerite.views.weather import weather

from explorify.views.album import albums
from explorify.views.artist import artists


app = Flask(__name__)

# Bikerite
app.register_blueprint(weather, url_prefix='/bikerite/weather')

# Explorify
app.register_blueprint(albums, url_prefix='/explorify/album')
app.register_blueprint(artists, url_prefix='/explorify/artist')

@app.after_request
def add_cors_header(response):
  from flask import request
  origin = request.headers.get('Origin', '')
  if origin in ['http://localhost:9000', 'http://explorify.jawsapps.com',
      'http://bikerite.jawsapps.com']:
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = \
      'Content-Type, Pragma, Cache-Control, *'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
  return response


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5001)
