import sys
sys.path.append('./bikerite/server')
sys.path.append('./explorify-server')
sys.path.append('./candidate_app')

from flask import Flask

from bikerite.views.weather import weather

from candidate_app.views.candidates import candidates
from candidate_app.views.election_cycles import election_cycles
from candidate_app.views.offices import offices
from candidate_app.views.parties import parties

from explorify.views.album import albums
from explorify.views.artist import artists


app = Flask(__name__)

# Bikerite
app.register_blueprint(weather, url_prefix='/bikerite/weather')

# Explorify
app.register_blueprint(albums, url_prefix='/explorify/album')
app.register_blueprint(artists, url_prefix='/explorify/artist')

# Candidate App
app.register_blueprint(candidates, url_prefix='/candidate_app/candidates')
app.register_blueprint(election_cycles, url_prefix='/candidate_app/election_cycles')
app.register_blueprint(offices, url_prefix='/candidate_app/offices')
app.register_blueprint(parties, url_prefix='/candidate_app/parties')

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
