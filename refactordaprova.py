from datetime import datetime
from dateutil import relativedelta
import csv

enddes='despesas.txt'
endsal='salario.txt'

def informar_float(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            return float(valor)
        else:
            print('Entrada inválida! Insira um número válido.')

def informar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('inválido!')

def retornar_saldo(ano, mes):
    with open(endsal, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for registro in leitor:
            if (ano == int(registro[0]) and mes == int(registro[1])):
                return registro[2]
    return None

def buscar_total_despesa(ano, mes):
    with open(enddes, 'r') as arquivo:
        linhas = arquivo.readlines()
        despesas = [float(linha.split(',')[2]) for linha in linhas if int(linha.split(',')[0]) == ano and int(linha.split(',')[1]) == mes]
        total = sum(despesas)
        return total

def calcular_rendimento(valor, ano, mes):
    d1 = '01/' + mes + '/'+ ano
    now = datetime.now()
    d2 = '01/' + str(now.month) + '/' + str(now.year)
    
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")
    
    delta = relativedelta.relativedelta(end_date, start_date)
    total_meses = delta.months + (delta.years * 12)    
    taxa = 0.01
    return valor * (1 + taxa) ** total_meses

menu = input("MENU \n 1)INFORMAR RENDIMENTO \n 2)ALTERAR RENDIMENTO \n 3)EXCLUIR RENDIMENTO \n 4)LISTAR RENDIMENTO \n 5)INFORMAR DESPESA \n 6)ALTERAR DESPESA \n 7)REMOVER DESPESA \n 8)LISTAR DESPESA \n 9)MOSTRAR RESULTADO")

if (menu == '1'):
    with open(endsal, 'a+') as arquivo:
        while True:
            try:
                ano = int(input('Informe o ano: '))
                mes = int(input('Informe o mês: '))
                salario = float(input('Informe o salário: '))
                break
            except ValueError:
                print('Entrada inválida! Por favor, tente novamente.')
        
        linha = str(ano) + ',' + str(mes) + ',' + str(salario)
        arquivo.write(linha)
        arquivo.write('\n')
        
elif menu == '2':
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o novo salário: ')
    with open(endsal, 'r') as arquivo:
        linhas = arquivo.readlines()
    with open(endsal, 'w') as arquivo:
        for i, linha in enumerate(linhas):
            registro = linha.split(',')
            if ano == int(registro[0]) and mes == int(registro[1]):
                linha = f"{ano},{mes},{salario}\n"
            arquivo.write(linha)

    with open(endsal, 'w') as arquivo:
        arquivo.writelines(linhas)

elif (menu == '3'):
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    linha_alterada = False
    with open(endsal, 'r') as arquivo:
        linhas = arquivo.readlines()
    with open(endsal, 'w') as arquivo:
        for linha in linhas:
            registro = linha.split(',')
            if (ano == int(registro[0]) and mes == int(registro[1])):
                linha_alterada = True
            else:
                arquivo.write(linha)
    if linha_alterada:
        print('Registro removido com sucesso!')
    else:
        print('Registro não encontrado.') 

    
    linhas.pop(linha_alterada)
    with open(endsal, 'w') as arquivo:
        arquivo.writelines(linhas)

if (menu == '4'):
    with open(endsal, 'r') as arquivo:
        linhas = arquivo.readlines();
        salarios = []
        for linha in linhas:
            registro = linha.split(',')
            salario = {'ano': int(registro[0]), 'mes': int(registro[1]), 'valor': float(registro[2])}
            salarios.append(salario)
        
        salarios_ordenados = sorted(salarios, key=lambda k: (k['ano'], k['mes']))
        
        print('----Salários----')
        for salario in salarios_ordenados:
            print('Ano: ' + str(salario['ano']) + ' Mês: ' + str(salario['mes']) + ' Salário: ' + str(salario['valor']))

elif (menu == '5'):
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    despesa = informar_float('Informe a despesa: ')
    
    saldo_mes = float(retornar_saldo(ano, mes))
    
    if despesa > saldo_mes:
        print('Saldo insuficiente!')
    else:   
        with open(enddes, 'a+') as arquivo:
            linha = str(ano) + ',' + str(mes) + ',' + str(despesa) + ';'
            arquivo.write(linha)
            arquivo.write('\n')

elif menu == '6':
    ano = informar_inteiro('Informe o ano: ')
    mes =  informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe a nova despesa: ')
    with open(enddes, 'r') as arquivo:
        linhas = arquivo.readlines()
    with open(enddes, 'w') as arquivo:
        for i, linha in enumerate(linhas):
            registro = linha.split(',')
            if ano == int(registro[0]) and mes == int(registro[1]):
                linha = f"{ano},{mes},{salario}\n"
            arquivo.write(linha)

    with open(enddes, 'w') as arquivo:
        arquivo.writelines(linhas)

elif (menu == '7'):
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    linha_alterada = False
    with open(enddes, 'r') as arquivo:
        linhas = arquivo.readlines()
    with open(enddes, 'w') as arquivo:
        for linha in linhas:
            registro = linha.split(',')
            if (ano == int(registro[0]) and mes == int(registro[1])):
                linha_alterada = True
            else:
                arquivo.write(linha)
    if linha_alterada:
        print('Registro removido com sucesso!')
    else:
        print('Registro não encontrado.') 
    
    linhas.pop(linha_alterada)
    with open(enddes, 'w') as arquivo:
        arquivo.writelines(linhas)

if (menu == '8'):
    with open(enddes, 'r') as arquivo:
        linhas = arquivo.readlines();
        despesas = []
        for linha in linhas:
            registro = linha.split(',')
            salario = {'ano': int(registro[0]), 'mes': int(registro[1]), 'valor': float(registro[2])}
            despesas.append(despesas)
        
        despesas_ordenados = sorted(despesas, key=lambda k: (k['ano'], k['mes']))
        
        print('----Salários----')
        for despesas in despesas_ordenados:
            print('Ano: ' + str(despesas['ano']) + ' Mês: ' + str(despesas['mes']) + ' Salário: ' + str(despesas['valor']))


            
elif (menu == '9'):
    with open(endsal, 'r') as arquivo:
        linhas = arquivo.readlines();
        linhas.sort()
        print(linhas)
        print('----Salários----')
        for linha in linhas:
            registro = linha.split(',')
            print('Ano: ' + registro[0] + ' Mês: ' + registro[1])
            salario = float(registro[2]);
            print('Salário: ' + str(salario))
            total_despesa = buscar_total_despesa(registro[0], registro[1])
            print('Despesa: ', total_despesa)
            saldo = salario - float(total_despesa)
            print('Saldo: ', saldo)
            bateu_meta = saldo > (salario * 0.1)
            print('Meta: ', bateu_meta)
            print('Valor investido: ', saldo)
            rendimento = calcular_rendimento(saldo, registro[0], registro[1])
            print('Rendimento: ', rendimento)