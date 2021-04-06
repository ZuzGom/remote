import subprocess
import requests
import json
from time import sleep


while True:
    ngrok = subprocess.Popen(['ngrok','tcp','3306'],stdout = subprocess.PIPE)

    localhost_url = "http://localhost:4040/api/tunnels" #Url with tunnel details
    tunnel_url = requests.get(localhost_url).text #Get the tunnel information
    j = json.loads(tunnel_url)

    wynik = j['tunnels'][0]['public_url'] #Do the parsing of the get
    f = open('tcp.txt','w')
    f.write(wynik)
    f.close()
    #wynik = tunnel_url["tunnels"]
    print(wynik)
    process = subprocess.Popen(['git', 'add', 'tcp.txt'])
    sleep(2)
    process = subprocess.Popen(['git', 'commit', '-m','update'])
    sleep(1)
    process = subprocess.Popen(['git', 'push'])
    sleep(5)
    process.terminate()
    
    sleep(900)
    ngrok.terminate()
