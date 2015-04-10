# This Python file uses the following encoding: utf-8
import os
#import pylab
#import numpy as np
import csv

import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

arqtransacao = csv.writer(open("transacao.csv", "wb"))
arqacao = csv.writer(open("acao.csv", "wb"))

ano = '2015'
if os.path.exists('alarme.dat'):
    dados = open('alarme.dat', 'r')
    linha = dados.readline()
    x = []
    y = []
    while linha:
        if str(linha[0:6]) == 'IGREJA':
            acao = str(linha[11:-1])
            arqacao.writerow([acao])
            #print (acao)
        else:
            hora = str(linha[0:5])
            data = str(linha[6:-1])
            dia = data[0:2]
            mes = data[3:5]
            x.append(ano + '-' + mes + '-' + dia)
            y.append(hora + ':00')
            arqtransacao.writerow([ano + '-' + mes + '-' + dia, hora + ':00'])
            #print ((data + ano, hora))
        linha = dados.readline()
    dados.close()
else:
    print ('Arquivo não encontrado!')


z = datetime.time(16,00)
print (z)
print('Willy')

# Generate Data
time = mdates.drange(datetime.datetime(2010, 1, 1),
                     datetime.datetime(2011, 1, 1),
                     datetime.timedelta(days=10))
y1 = np.cumsum(np.random.random(time.size) - 0.5)

print (time)
print (y1)

# Plot things...
fig = plt.figure()

plt.plot_date(datetime.date(2015,1,1),46, '-')

fig.autofmt_xdate()
plt.show()
