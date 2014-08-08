
from app import server

def test_webapp_index():
  assert server.index('Travis') == 'Hello Travis!'
