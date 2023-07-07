from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    r.incr('visits')
    visits = r.get('visits').decode('utf-8')
    return f'Hello, you have visited this page {visits} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
