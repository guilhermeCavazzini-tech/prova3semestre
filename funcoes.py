salario = 0
loop = input('Deseja continuar?').lower

def infosalario ():
    salario = (float(input('Informe Seu Salario')))
    print('Salario Informado R$',salario)
    with open ("liquidemes.txt","w") as arquivos:  
        arquivos.write('salario R$')
        arquivos.write(str(salario) +'\n')
    

def altsalario ():
    with open ("liquidemes.txt","w") as arquivos:
        salario = (float(input('Novo Salario')))
        arquivos.write(('Novo Salario R$')+(str(salario)))
        print('Salario alterado para R$',salario)

def excsalario():
    print('Salario excluido com sucesso')

def listarsalario():
    print('Salario listado')

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


while loop == 's' or 'sim':

    print("MENU \n 1)INFORMAR RENDIMENTO \n 2)ALTERAR RENDIMENTO \n 3)EXCLUIR RENDIMENTO \n 4)LISTAR RENDIMENTO \n 5)INFORMAR DESPESA \n 6)ALTERAR DESPESA \n 7)REMOVER DESPESA \n 8)LISTAR DESPESA \n 9)MOSTRAR RESULTADO")

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

    loop = input('Deseja continuar?').lower
