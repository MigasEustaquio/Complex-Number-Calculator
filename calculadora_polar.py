import math


def para_polar(real, imaginario):
    resultado_mod=math.sqrt(real*real+imaginario*imaginario)

    if(real==0.0):
        if imaginario>0:
            resultado_ang=math.pi/2
        else:
            resultado_ang=-math.pi/2
    else:
        resultado_ang=math.atan(imaginario/real)
    
    return resultado_mod, resultado_ang

def conversao(operacao):

    if operacao == "polar":

        real=float(input("\nInsira a parte REAL do número  "))
        imaginario=float(input("\nInsira a parte IMAGINÁRIA do número  "))

        modulo, angulo = para_polar(real, imaginario)

        print("\nO resultado na forma polar é: ", modulo, " ângulo (", math.degrees(angulo), ")\n")

    else:
        modulo=float(input("\nInsira o MÓDULO do número  "))
        angulo=float(input("\nInsira o ÂNGULO do número  "))
        real=modulo*math.cos(math.radians(angulo))
        imaginario=modulo*math.sin(math.radians(angulo))

        print("\nO resultado na forma retangular é: ", real, " + j(", imaginario, ")")


def soma(operacao):

    if operacao=="+":
        quantidade=int(input("\nSOMA\nQuantos números serão somados?   "))
    else:
        print("\nSUBTRAÇÃO")
        quantidade=2

    modulos=[]
    angulos=[]
    reais=[]
    imaginarios=[]
    i=0
    while i<quantidade:
        modulos.append(float(input("\nInsira o Módulo do "+ str(i+1) +"° número  ")))
        angulos.append(float(input("\nInsira o Ângulo do "+ str(i+1) +"° número  ")))
        reais.append(modulos[i]*math.cos(math.radians(angulos[i])))
        imaginarios.append(modulos[i]*math.sin(math.radians(angulos[i])))
        i+=1


    resultado_real=0
    resultado_im=0

    if operacao=="+":
        for real in reais:
            resultado_real=resultado_real+real
        for imaginario in imaginarios:
            resultado_im=resultado_im+imaginario
    else:
        resultado_real=reais[0]-reais[1]
        resultado_im=imaginarios[0]-imaginarios[1]

    resultado_mod, resultado_ang = para_polar(resultado_real, resultado_im)


    print("\nO resultado na forma retangular é: ", resultado_real, " + j(", resultado_im, ")")
    print("\nO resultado na forma polar é: ", resultado_mod, " ângulo (", math.degrees(resultado_ang), ")\n")


print("\nCalculadora polar python versão 1.5\n(Soma, subtração e conversão)\n")
print("\nInstruções:\nUtilize numeros reais\nUtilize ponto (.) para separar parte inteira de parte decimal\nUtilize graus (não radianos)")

while True:
    operacao=input("\nInsira a operação\nsoma de números polares ('+' ou '-')\nconersao para qual deseja converter ('polar' ou 'retangular')\npara sair ('0')\n")

    if operacao=="soma":
        operacao="+"
    elif operacao=="subtracao" or operacao=="subtraçao":
        operacao="-"

    if operacao =="+" or operacao=="-":
        soma(operacao)
        print("\n\nMenu")
    elif operacao == "polar" or operacao == "retangular":
        conversao(operacao)
        print("\n\nMenu")
    elif operacao == "0":
        print("\nFINALIZADO")
        break
    else:
        print("\nOperação não encontrada, cheque a lista de operações para mais informações.\n\nMenu")