import os
from time import sleep
stream = os.popen('ngrok http 8000')
sleep(5)
stream.kill()
output = stream.read()
print(output)