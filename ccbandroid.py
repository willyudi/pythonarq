#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import re
import android
droid = android.Android()
#droid.ttsSpeak('hello williano')
from datetime import datetime
import sys

import json
from urllib.request import urlopen
import urllib.parse
import urllib.request
import socket

def parseEvent(line):
    print('hi')
    out = json.loads(line)
    out.update(json.loads(out["data"]))
    return out
permission = 'android.permission.BROADCAST_SMS'
ACTION = 'android.provider.Telephony.SMS_DELIVER_ACTION'
droid.eventRegisterForBroadcast(ACTION, False)
#print(droid.eventGetBroadcastCategories())
p = droid.startEventDispatcher().result
print(p)
s = socket.socket()
s.connect(('localhost', p))
f = s.makefile()
#print(f.readline())
#print(droid.getMessagesFromIntent())v


while True:
    print('test')
    #event = droid.eventWait()
    event = parseEvent(f.readline())
    print(event)
    droid.log(str(event))
    print('got', event)

print(droid.eventUnregisterForBroadcast(ACTION))
print(droid.eventGetBroadcastCategories())


#Get JSON
alarme_url = 'http://viniciusdepaula.com/api/ccb/alarme/acao/'
html = urlopen(alarme_url)
print (html.read())
now = datetime.now()
tempo = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

#Post JSON
valores = {'data' : '2015-08-25',
            'hora' : tempo,
            'responsavel' : 'WILLIANO SERPA',
            'acao' : 'DESLIGAMENTO DO ALARME - via Android',
            'estado' : '0'}
params = json.dumps(valores).encode('utf-8')
req = urllib.request.Request(alarme_url, data=params,
                            headers={'content-type' : 'application/json'})
response = urllib.request.urlopen(req)
#print(response.read().decode('utf8'))

x = droid.smsGetMessageCount(0)
print (' ')
print ('Usando APIs do Android')
print ('Total de SMS: ' + str(x.result))

SMSmsgs = droid.smsGetMessages(False, 'inbox').result
conta = 0
for message in SMSmsgs:
    if message['address'] == '+553492314689':
        print (message['body']+'\n')
        conta = conta + 1
        a = message['body']
        #separa = a.split (" ")
        print (a[-5:]+'/2015')
print(conta)