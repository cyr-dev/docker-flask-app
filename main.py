from flask import Flask
from redis import Redis

app = Flask(__name__)

redis = Redis(host='localhost', port=6379)

@app.route('/')
def hello_world():
  redis.incr('hits')
  return 'KEEP LEARNING, KEEP MOVING AHEAD_Count %s' % redis.get('hits')


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5001, debug=True)
  # app.run(port=5001, debug=True)