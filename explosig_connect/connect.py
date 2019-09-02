import requests
from .connection import Connection

HOSTNAME = 'https://explosig.lrgr.io'

def login(password, hostname):
    r = requests.post(hostname + '/login')
    r.raise_for_status()
    return r.json()['token']

def connect(conn_id, password=None, hostname=HOSTNAME):
    if password != None and hostname != HOSTNAME:
        token = login(password, hostname)
    else:
        token = None
    
    return Connection(conn_id, token, hostname)