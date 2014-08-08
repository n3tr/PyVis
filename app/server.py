
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
  return 'Hello %s!' %(name)


if __name__ == '__main__':
  run(host='localhost', port=8080)
