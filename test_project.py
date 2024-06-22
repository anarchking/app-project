import pytest
from project import server_to_db, load_last_server, connect_server


def test_server_to_db():
    assert server_to_db("192.168.1.1", "1883", "username", "password") == True
    assert server_to_db("192.168.255.255", "1883", "username", "password") == True
    # port max
    assert server_to_db("192.168.255.255", "67000", "username", "password") == False
    # no username or password
    assert server_to_db("192.168.0.0", "1") == True
    # ip max
    assert server_to_db("192.168.0.256", "1") == False
    # port min
    assert server_to_db("192.168.0.1", "0") == False
    # port max
    assert server_to_db("192.168.0.1", "65537") == False


def test_load_last_server():
    assert load_last_server() == 


 def test_connect_server():
    assert connect_server() == 