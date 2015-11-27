#-*-coding:utf8;-*-
import os
import sys
import time
from datetime import datetime
import json
from urllib.request import urlopen
import urllib.parse
import urllib.request

os.system('clear')

#Get JSON
alarme_url = 'http://viniciusdepaula.com/api/ccb/alarme/acao/'
#html = urlopen(alarme_url)
#print (html.read())
now = datetime.now()
tempo = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

# 15-11-2015 - Williano Serpa
# Abre arquivo para fazer a leitura
# Campos necess[arios:
# Identificador (11 caracteres) - Fixo 'IGREJA   : '
# Mensagem (50 Caracteres) - Ex.: 'Sistema desarmado por RONALDO  via SMS'
# Horario (10 Caracteres) - Formato HH:MM DD/MM - Ex.: '19:53 27/03'

Identificador = 'IGREJA   : '
Mensagem = ''
DataMensagem = ''
Horario = ''
ano = '2015'
NumeroLinha = 1

if os.path.exists('ccbalarme032015.txt'):

    dados = open('ccbalarme032015.txt', 'r')
    linha = dados.readline()
    print ('Arquivo ccbalarme032015.txt em Processamento!')

    while linha:

        if str(linha[0:11]) == Identificador:
            Mensagem = str(linha[11:-1])
        else:
            hora = str(linha[0:5])
            data = str(linha[6:-1])
            dia = data[0:2]
            mes = data[3:5]
            DataMensagem = ano + '-' + mes + '-' + dia
            Horario = hora + ':00'

            if Mensagem.find('por') > 0:
                Posicao = Mensagem.find('por') + 4
                Responsavel = Mensagem[Posicao:]
                Acao = Mensagem[0:Mensagem.find('por')]
                Estado = 2
                if Mensagem.find('Armado') > 0:
                    Estado = 1
                elif Mensagem.find('Desarmado') > 0:
                    Estado = 0
            else:
                Posicao = 0
                Responsavel = 'ALARME'
                Acao = Mensagem

            #Post JSON
            valores = {'data' : DataMensagem,
                        'hora' : Horario,
                        'responsavel' : Responsavel,
                        'acao' : Acao,
                        'estado' : Estado}
            params = json.dumps(valores).encode('utf-8')
            req = urllib.request.Request(alarme_url, data=params,
            headers={'content-type' : 'application/json'})
            response = urllib.request.urlopen(req)
        print('Linha do Arquivo: % 2d' % NumeroLinha, end = '\r')
        sys.stdout.flush()
        NumeroLinha = NumeroLinha + 1
        linha = dados.readline()
    dados.close()
else:
    print ('Arquivo não encontrado!')

print ('Arquivo Processado com Sucesso!')
