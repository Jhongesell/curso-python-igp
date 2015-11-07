import sys
import requests

def contar_bytes(url):
    resp = requests.get(url)
    if resp.ok:
       return len(resp.content)

if __name__ == '__main__':
	print contar_bytes('http://www.google.com.pe')
