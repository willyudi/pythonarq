# This Python file uses the following encoding: utf-8
import os, sys

# Lista Telefonica que grava e le de arquivo de texto

ARQUIVO = "lista_telefonica.txt" # Nome do arquivo de texto

def le_arquivo():                # Função que le o arquivo de texto
    try:                         # Tratamento de erro
        arq = open(ARQUIVO,"r+") # Abre o arquivo para leitura
        print( '\n'+arq.read() ) # Quebra linha e mostra o conteudo
        arq.close()              # Fecha o arquivo
    except IOError:              # Tratamento de erro
        print('\nArquivo não encontrado!')

def escreve_arquivo(texto):        # Função que le e escreve no arquivo
    try:                           # Tratamento de erro
        arq = open(ARQUIVO,"a+")   # Abre o arquivo para gravação no
        arq.writelines('\n'+texto) # Escreve no arquivo o parametro 'texto'
        arq.close()                # Fecha o arquivo
        print('\nRegistro gravado com sucesso')
    except IOError:                # Tratamento de erro
        print('\nErro ao abrir o arquivo!') # Mostra na tela uma mensagem

while(True):                     # Loop infinito
    print('\nEscolha a opcao:')
    print('1-Cadastrar Telefone')
    print('2-Listar Telefones')
    print('0-Sair')
    vOpcao = int(input('Digite a sua opcao:')) # Entrada da opcao pelo teclado

    if vOpcao == 1:                           # Se a opcao for 1
        nome = str(input('\nDigite o nome:'))
        telefone = input('Digite o telefone:')
        nome = str(str(nome) + ' - ' + str(telefone))
        escreve_arquivo(str(nome))            # Chama a função que grava em
    elif vOpcao == 2:             # Se a opcao for 2
        le_arquivo()              # Chama a função que le o arquivo
    elif vOpcao == 0:             # Se a opcao for 0
        break                     # Quebra o laço infinito
