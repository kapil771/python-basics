import time
import urllib.request
url = 'http://www.google.com'
conn = urllib.request.urlopen(url)

print(f'{url} is up')
time.sleep(60)