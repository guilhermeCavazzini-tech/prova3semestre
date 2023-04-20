salario = 1

def infosalario ():
    with open ("liquidemes.txt","w") as arquivos:  
        arquivos.write('salario R$')
        arquivos.write(str(salario) +'\n')

infosalario()



print("MENU \n 1)INFORMAR RENDIMENTO \n 2)ALTERAR RENDIMENTO \n 3)EXCLUIR RENDIMENTO \n 4)LISTAR RENDIMENTO \n 5)INFORMAR DESPESA \n 6)ALTERAR DESPESA \n 7)REMOVER DESPESA \n 8)LISTAR DESPESA \n 9)MOSTRAR RESULTADO")