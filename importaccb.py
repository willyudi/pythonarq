#-*-coding:utf8;-*-
import os
import sys
import json
from urllib.request import urlopen
import urllib.parse
import urllib.request

#Get JSON
#alarme_url = 'http://viniciusdepaula.com/api/ccb/alarme/acao/'
#html = urlopen(alarme_url)
#print (html.read())

# 15-11-2015 - Williano Serpa
# Abre arquivo para fazer a leitura
# Campos necess[arios:
# Identificador (11 caracteres) - Fixo 'IGREJA   : '
# Mensagem (50 Caracteres) - Ex.: 'Sistema desarmado por RONALDO  via SMS'
# Horario (10 Caracteres) - Formato HH:MM DD/MM - Ex.: '19:53 27/03'
# Inicializa Variaveis
alarme_url = 'http://viniciusdepaula.com/api/ccb/alarme/acao/'
Identificador = 'IGREJA   : '
Mensagem = ''
DataMensagem = ''
Horario = ''
ano = '2015'
Estado = 0
NumeroLinha = 1
contalinha = 0

#Limpa o terminal
os.system('clear')

#Verifica se o arquivo existe no diretorio
if os.path.exists('ccbalarme072015.txt'):

    #Abre arquivo para verificar tamanho
    dados = open('ccbalarme072015.txt', 'r')
    contalinha = len(dados.readlines())
    dados.close()

    #Abre arquivo para leitura
    dados = open('ccbalarme072015.txt', 'r')
    linha = dados.readline()
    print ('Arquivo ccbalarme072015.txt em Processamento!')

    #Comeca leitura do arquivo
    while linha:

        #Primeira Linha Mensagem
        if str(linha[0:11]) == Identificador:
            Mensagem = str(linha[11:-1])
        else:
            #Segunda linha - Data e Hora
            hora = str(linha[0:5])
            data = str(linha[6:])
            dia = data[0:2]
            mes = data[3:5]
            DataMensagem = ano + '-' + mes + '-' + dia
            Horario = hora + ':00'

            #Consolida informacoes - Responsavel e Acao
            if Mensagem.find('por') > 0:
                Posicao = Mensagem.find('por') + 4
                Responsavel = Mensagem[Posicao:]
                Acao = Mensagem[0:Mensagem.find('por')]
            else:
                Posicao = 0
                Responsavel = 'ALARME'
                Acao = Mensagem

            #Verifica se Alarme ligado (1) ou Desligado (0) - Outros (2)
            if Acao.find('desarmado') > 0:
                Estado = 0
            elif Acao.find('armado') > 0:
                Estado = 1
            else:
                Estado = 2

            #Post JSON - Acessa servico de gravacao banco
            valores = {'data' : DataMensagem,
                        'hora' : Horario,
                        'responsavel' : Responsavel,
                        'acao' : Acao,
                        'estado' : Estado}
            params = json.dumps(valores).encode('utf-8')
            req = urllib.request.Request(alarme_url, data=params,
            headers={'content-type' : 'application/json'})
            response = urllib.request.urlopen(req)

        #Indica que linha esta dentro do arquivo
        print('Carregando Arquivo: % 2d %%' % ((NumeroLinha/contalinha)*100), end = '\r')
        sys.stdout.flush()
        NumeroLinha = NumeroLinha + 1
        linha = dados.readline()
    dados.close()
else:
    print ('Arquivo não encontrado!')

#Finaliza aplicacao
print ('Arquivo Processado com Sucesso!')
