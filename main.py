##########################################
##                                      ##
##   Alunos:                            ##
##   - Bruno Luis                       ##
##   - Camila Duarte                    ##
##   - Gabriel Lima                     ##
##   - Igor Amon                        ##
##   - Jorge Fernando                   ##
##   - Samara Jaques                    ##
##                                      ##
##########################################

import os
import numpy as np
from calcular import Calcular
from tabela import Tabela

def main():
    tb = Tabela('coinmetrics2.csv', 'utf-16')
    
    op = -1
    os.system("cls||clear")
    while op != 0:
        print("\n############################################")
        print("##            Escolha uma acao            ##")
        print("############################################")
        print()
        print("[1] Calcular coeficente de correlacao")
        print("[2] Calcular coeficiente de regressao linear")
        print("[3] Calcular regressao linear multivariado")
        print("[0] Sair")
        print()

        op = int(input("> Opcao: "))

        while not (op in [0, 1, 2, 3]):
            print("\nOpcao Invalida\n")
            op = int(input("> Opcao: "))

        # Calcular coeficente de correlacao
        if op == 1:
            os.system("cls||clear")
            esc = []
            arr = []
            for i in range(2):
                print("\n############################################")
                print("##          Escolha a {}ª variavel         ##".format(i+1))
                print("############################################")

                vars = tb.pegar_variaveis()
                for j in range(len(vars)):
                    print("[{}] {}".format(j, vars[j]))

                print()
                esc.append(int(input("> Opcao: ")))

                while not (op in range(len(vars))):
                    print("\nOpcao Invalida\n")
                    op = int(input("> Opcao: "))
                
                arr.append(np.array(tb.pegar_lista(esc[i])))
            
            calc = Calcular()
            coef = calc.coeficiente_correlacao(arr[0], arr[1])
            print("\nCoeficiente de correlacao: {}".format(coef))
            intervalo()

        elif op == 2:
            os.system("cls||clear")
            esc = []
            arr = []
            for i in range(2):
                print("\n############################################")
                print("##          Escolha a {}ª variavel         ##".format(i+1))
                print("############################################")

                vars = tb.pegar_variaveis()
                for j in range(len(vars)):
                    print("[{}] {}".format(j, vars[j]))

                print()
                esc.append(int(input("> Opcao: ")))

                while not (op in range(len(vars))):
                    print("\nOpcao Invalida\n")
                    op = int(input("> Opcao: "))
                
                arr.append(np.array(tb.pegar_lista(esc[i])))
            
            calc = Calcular()
            [b, a] = calc.regressao_linear(arr[0], arr[1])
            print("\nCoeficente de Regressao Linear")
            print("a: {}".format(a))
            print("b: {}".format(b))
            intervalo()

        elif op == 3:
            os.system("cls||clear")
            esc = []
            arr = []
            for i in range(3):
                print("\n############################################")
                print("##          Escolha a {}ª variavel         ##".format(i+1))
                print("############################################")

                vars = tb.pegar_variaveis()
                for j in range(len(vars)):
                    print("[{}] {}".format(j, vars[j]))

                print()
                esc.append(int(input("> Opcao: ")))

                while not (op in range(len(vars))):
                    print("\nOpcao Invalida\n")
                    op = int(input("> Opcao: "))
                
                arr.append(np.array(tb.pegar_lista(esc[i])))
            
            calc = Calcular()
            res = calc.regressao_multivariada(arr[0], arr[1], arr[2])
            print("\nTermo independente: {}".format(res[0]))
            print("Coeficiente da variavel 1: {}".format(res[1]))
            print("Coeficiente de variavel 2: {}".format(res[2]))
            print("Coeficiente de interação entre")
            print("a variavel 1 e 2: {}".format(res[3]))
            intervalo()
        
        else:
            break

def intervalo():
    input("\nPressione qualquer tecla para continuar...")
    os.system("cls||clear")

if __name__ == '__main__':
    main()