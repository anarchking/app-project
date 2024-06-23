import pytest
from main import server_to_db, load_last_server, connect_server


def main():
    test_server_to_db()
    test_load_last_server()
    test_connect_server()


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


# make sure output matches input
def test_load_last_server():
    server_to_db("192.168.1.1", "1883")
    assert load_last_server() == "Connect to Server 192.168.1.1 on Port 1883?"
    server_to_db("192.168.4.1", "1883")
    assert load_last_server() == "Connect to Server 192.168.4.1 on Port 1883?"
    server_to_db("192.168.4.1", "1884")
    assert load_last_server() == "Connect to Server 192.168.4.1 on Port 1884?"


# test for absurd values
def test_connect_server():
    with pytest.raises(ValueError):
        connect_server("192.168.42.3", "string")
    with pytest.raises(AttributeError):
        connect_server("192.168.42.3", "1883", 1234)
    with pytest.raises(TypeError):
        connect_server("192.168.42.3", 1883, "username", 1)
    with pytest.raises(AttributeError):
        connect_server("192.168.42.3", 1883, 1, "42")