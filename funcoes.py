salario = 0
endercoArquivo ="liquidemes.txt"
campoSelecionado = 1

print("MENU \n 1)INFORMAR RENDIMENTO \n 2)ALTERAR RENDIMENTO \n 3)EXCLUIR RENDIMENTO \n 4)LISTAR RENDIMENTO \n 5)INFORMAR DESPESA \n 6)ALTERAR DESPESA \n 7)REMOVER DESPESA \n 8)LISTAR DESPESA \n 9)MOSTRAR RESULTADO")

def infosalario ():
    salario = input('Informe Seu Salario')
    data = input('informe a data')
    poupar = input('informe quanto vai polpar')
    rendimento = input('informe o rendimento')
    print('Salario Informado R$',salario)
    with open (endercoArquivo,"r") as arquivo:         
        arquivoAtual = arquivo.read()

    with open (endercoArquivo,"w") as arquivos:         
        arquivos.write(salario+';'+data+';'+poupar+';'+rendimento+'\n'+arquivoAtual)
        #arquivos.write(str(salario) +'\n')
    


def altsalario ():
    nnarquivo = ''
    data = input('informe o mes do Rendimento (dd/MM)')
    with open(endercoArquivo, 'r+') as arquivo:
       
      for linha in arquivo:
        if data in linha:
         array = []
         array = linha.split(';')
         print('Rendimento Encontrado:')
         array[0] = input('Informe o Salario: ')
  
    

def excsalario():
    novoArquivo =''
    data = input('informe o data (dd/MM)')

    with open("liquidemes.txt", 'r') as arquivo:
       
      for linha in arquivo:
        
         if data not in linha:
          novoArquivo = novoArquivo+ linha
     
       
    with open (endercoArquivo,"w") as arquivos:         
       arquivos.write(novoArquivo)    

def listarsalario():
  
    with open("liquidemes.txt", 'r') as arquivo:
              
        for linha in arquivo:
         #print(linha)
         array = []
         array = linha.split(';')
         print('Salario:' +array[0])
         print('Data:' +array[1])
         print('Poupar:' +array[2])
         print('Rendimento:' +array[3])
         print('----------------')
    

def informardespesa():
    print('Despesa informada')

def alterardespesa():
    print('Despesa Alterada')

def excluirdespesa():
    print('Despesa excluida')

def listardespesa():
    print('Despesa listada')

def mostrarResultado():
    print('Resultado mostrado')





resposta = int(input('Qual a opção desejada?'))
if resposta == 1:
    infosalario()
if resposta == 2:
    altsalario()
if resposta == 3:
    excsalario()
if resposta == 4:
    listarsalario()
if resposta == 5:
    informardespesa()
if resposta == 6:
    alterardespesa()
if resposta == 7:
    excluirdespesa()
if resposta == 8:
    listardespesa()
if resposta == 9:
    mostrarResultado()

print ()
