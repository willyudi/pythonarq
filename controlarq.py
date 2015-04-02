# This Python file uses the following encoding: utf-8
import os
import matplotlib.pyplot as plt
import numpy as np

ano = '/2015'
if os.path.exists('alarme.dat'):
    dados = open('alarme.dat', 'r')
    linha = dados.readline()
    while linha:
        if str(linha[0:6]) == 'IGREJA':
            acao = str(linha[11:-1])
            print (acao)
        else:
            hora = str(linha[0:5])
            data = str(linha[6:-1])
            print ((data + ano, hora))
        linha = dados.readline()
    dados.close()
else:
    print ('Arquivo não encontrado!')
