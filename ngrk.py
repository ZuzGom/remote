import subprocess
from time import sleep

#result = subprocess.Popen(['ngrok','http','8000'], stdout=subprocess.PIPE)
result=subprocess.Popen(['ngrok','http','8000'])
p = subprocess.Popen(['ngrok','http','8000'], stdout=subprocess.PIPE, shell=True)


#p = subprocess.Popen(['vprobe', '/vprobe/myhello.emt'], stdout=subprocess.PIPE,  buff, universal_newlines=True, preexec_fn=os.setsid)
#process = subprocess.Popen(['ngrok','http','8000'],stdout=subprocess.PIPE)
sleep(5)
#result.terminate()
p.kill()
#print(result)
#print(result.stdout)
out, err = p.communicate()
'''

command = "ngrok http 8000"  # the shell command
process = subprocess.Popen(['ngrok','http','8000'], stdout=subprocess.PIPE, stderr=None, shell=True)
sleep(15)
#process = subprocess.Popen(['killall','ngrok'])
process.terminate()
#Launch the shell command:
output = process.communicate()
out = str(output[0]).split()
#print (output[0])
'''
print(out)
linia = str(out)
#print(linia)
f = open('guni.txt','w')
f.write(linia.split()[-1][:-4])
f.close()
process = subprocess.Popen(['killall','ngrok'])
#process = subprocess.Popen(['ngrok','http','8000'], input='')

