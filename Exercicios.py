#Q1
A = 10
B = 20
A = B
print(A)
A = 10
B = 20
B = A
print(B)

#Q2
#a output: [20], [10, 5]
#b output: [50], [10, 50], [30,10,40]
#c output: [10,10,10]
#d output: [12], [14,13]
#e output: [10,20,15]
#f output: [1], [5, 6, 1]

#Q3
#1. sim
#2. não
#3. não

#Q4
A = 6*(3+2)
B = 2+6*(3+2)
C = 2+3*6/(2+4)
D = 2*8/(3+1)
E = 3+(16-2)/(2*(9-2))
F = 6/3+8/2
G = 3+(8/2)*4+3*2
H = 6*3*3+6-10
I = (10*8+3)*9
J = -12*-4+3*(-4)

#Q5
A = int(input('Digite um valor: '))
antecessor = int(A) - 1
print(antecessor)

#Q6
base = float(input('Entre com a base do retântgulo: '))
if base <= 0:
    print('valor de base inválido')
else:
    altura = float(input('Entre com a altura do retângulo: '))
    if altura <= 0:
        print('valor inválido pra altura')
    else:
        area = base*altura
        print('A area do triângulo é:', area)

#Q7
from datetime import datetime
current_date = datetime.now()
Ano = input('Informe o ano que nasceu ')
Mes = input('Informe o mês que nasceu (ex: 3)')
Dia = input('Informe o dia que nasceu ')

num_anos = current_date.year - int(Ano)
num_mes = current_date.month - int(Mes)
num_dia = current_date.day - int(Dia)

total_dias = num_anos*365 + num_mes*30 + num_dia
print(total_dias)

#Q8
total_eleitores = int(input('total de eleitores do seu municipio: '))
votos_nulos = int(input('total de votos nulos do seu municipio: '))
votos_brancos = int(input('total de votos em branco do seu municipio: '))
votos_validos = total_eleitores - (votos_brancos + votos_nulos)
if (votos_brancos+votos_nulos) > total_eleitores:
    print('Brancos e nulos maiores que numero total de eleitores')
else:
    perc_nulos = (votos_nulos/total_eleitores)*100
    print('O percentual de votos nulos em seu município é: ', perc_nulos,'%')

    perc_brancos = (votos_brancos/total_eleitores)*100
    print('O percentual de votos nulos em seu município é: ', perc_brancos,'%')

    perc_validos = (votos_validos/total_eleitores)*100
    print('O percentual de votos nulos em seu município é: ', perc_validos,'%')

#Q9
salario = float(input('Informe seu salario: '))
reajuste = float(input('Informe o reajuste do funcionario (em %): '))
novo_salario = salario*reajuste/100 + salario
print(novo_salario)

#Q10
custo = float(input('Informe o custo de fábrica: '))
taxes = custo*(0.28 + 0.45 + 1)
print(taxes)

#Q11
salario = float(input('informe o salário do funcionário: '))
comissão = float(input('Comissão é de: '))
n_carros = int(input('Informe a quantidade de carros vendidos '))
total_vendas = float(input('Total de vendas foi: '))
comissão_final = comissão*n_carros
salario_final = salario + comissão_final + total_vendas*0.05
print(salario_final)

#Q12
Fahr = float(input('Informe os graus Fahrenheit: '))
Celcius = 5*(Fahr - 32)/9
print(Celcius)

#Q13
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
pesos = [2,3,5]
media_final = (n1*pesos[0] + n2*pesos[1] + n3*pesos[2])/10
print(media_final)

#Q14
valor = float(input("Digite um valor: "))
if valor > 10:
    print('Valor maior que 10')
else:
    print('Valor menor que 10')

#Q15
valor = float(input("Digite um valor: "))
if valor >= 0:
    print('Valor é positivo')
else:
    print('Valor é negativo')

#Q16
quant_comprada = int(input('Comprou quantas maças? '))
if quant_comprada < 12:
    total = quant_comprada*1.30
    print(total)
else:
    total = quant_comprada
    print(total)

#Q17
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2)/2
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
print('Média é:', media)

#Q18
year = 2019
born = int(input('Ano de nascimento: '))
idade = year - born
if idade < 18:
    print('Não pode votar')
else:
    print('Permitido votar')

#Q19
valor1 = float(input('Entre com um valor: '))
valor2 = float(input('Entre com um valor: '))
if valor1 > valor2:
    print(valor1)
else:
    print(valor2)

#Q20
valor1 = float(input('Entre com um valor: '))
valor2 = float(input('Entre com um valor: '))
if valor1 > valor2:
    print(valor2, valor1)
else:
    print(valor1, valor2)

#Q21
inicio = int(input('Hora de inicio (em horas): '))
fim = int(input('Hora de término (em horas): '))
total = fim - inicio
print(total)

#Q22
hora = int(input('Quantidade de hora trabalhada no mês atual: '))
salario = int(input('Salario por hora trabalhada: '))

if hora > 160:
    salario_total = hora*salario + hora*salario*0.5
    print(salario_total)
else:
    salario_total = hora*salario
    print(salario_total)

#Q23
#Não foi atribuída a variável "altura", "M" deve ser lido como string

#24
salario = float(input('informe o salário do funcionário: '))
total_vendas = float(input('Total de vendas foi: '))
if total_vendas <= 1500:
    comissão = total_vendas*(1 + 0.03)
else:
    comissão = total_vendas*(1 + 0.03) + 0.05*(total_vendas - 1500)
print(salario + comissão)

#Q25
conta = int(input('Numero da conta: '))
saldo = int(input('Saldo: '))
debito = int(input('Débito: '))
credito = int(input('Crédito: '))
saldo_atual = saldo - debito + credito
print(saldo_atual)
if saldo_atual >= 0:
    print('A conta de numero', conta, 'está com Saldo Positivo de:', saldo_atual)
else:
    print('A conta de numero', conta, 'está com Saldo Negativo de:', saldo_atual)

#Q26
estoque_atual = int(input('Estoque atual: '))
estoque_max = int(input('Estoque maximo permitido: '))
estoque_min = int(input('Estoque minimo permitido: '))
estoque_medio = (estoque_max + estoque_min)/2
if estoque_atual >= estoque_medio:
    print('Efetuar compra')
else:
    print('Não efetuar compra')

#Q27
valor1 = float(input('Digite um valor: '))
if valor1 > 0:
    print('Valor positivo')
else:
    if valor1 < 0:
        print('Valor negativo')
    else:
        print('Valor é nulo, é zero')

#Q28
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
valor3 = float(input('Digite um terceiro valor: '))
if valor1 > valor2 and valor1 > valor3:
    print(valor1)
else:
    if valor2 > valor1 and valor2 > valor3:
        print(valor2)
    else:
        print(valor3)

#29
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
valor3 = float(input('Digite um terceiro valor: '))
if valor1 > valor2 and valor2 > valor3:
    print(valor1 + valor2)
else:
    if valor3 > valor2 and valor2 > valor1:
        print(valor2 + valor3)
    else:
        print(valor1 + valor3)

#30
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
valor3 = float(input('Digite um terceiro valor: '))
lista = [valor1, valor2, valor3]
print(sorted(lista))

#31
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
valor3 = float(input('Digite um terceiro valor: '))
if valor1 > valor2 + valor3:
    print('Não é um triângulo')
else:
    if valor2 > valor1 + valor3:
        print('Não é um triângulo')
    else:
        if valor3 > valor2 + valor1:
            print('Não é um triângulo')
        else:
            print('Parabens, deu bom. Podemos dizer que é um triângulo, de fato!')

#32
time1 = str(input('Nome do primeiro time: '))
time2 = str(input('Nome do segundo time: '))
gols1 = int(input('Gols do primeiro time: '))
gols2 = int(input('Gols do segundo time: '))
if gols1 > gols2:
    print('Time vencedor é:', time1)
else:
    if gols2 > gols1:
        print('Time vencedor é:', time2)
    else:
        print('Empatou')

#33
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um segundo valor: '))
if valor1 > valor2:
    print('Primeiro é maior, no caso:', valor1)
else:
    if valor2 > valor1:
        print('Segundo é maior, no caso:', valor2)
    else:
        print('Ambos são iguais a', valor1)

#34
z = [11, 455, -2, -5, 155]
resposta = ['B', 'C', 'A', 'A', 'C']

#35
n_litros = float(input('Numero de litros vendidos: '))
tipo = str(input('Qual tipo? ("A" para Alcool ou "G" para Gasolina) '))
gasolina = 3.30
alcool = 2.90
if tipo.lower() == "a" and n_litros <= 20:
    valor_pago = n_litros*alcool - 0.03*n_litros*alcool
    print(valor_pago)
else:
    if tipo.lower() == "a" and n_litros >= 20:
        valor_pago = n_litros*alcool - 0.05*n_litros*alcool
        print(valor_pago)
    else:
        if tipo.lower() == "g" and n_litros <= 20:
            valor_pago = n_litros*gasolina - 0.04*n_litros*gasolina
            print(valor_pago)
        else:
            if tipo.lower() == "g" and n_litros >= 20:
                valor_pago = n_litros*gasolina - 0.06*n_litros*gasolina
                input(valor_pago)
            else:
                input('Digite de novo, tem algo errado!')

#36
M1 = int(input('Nome do primeiro homem: '))
M2 = int(input('Nome do segundo homem: '))
F1 = int(input('Nome da primeiro mulher: '))
F2 = int(input('Nome da segundo mulher: '))

if M1 > M2 and F1 > F2:
    A = M1 + F2
    B = F1*M2
    print(A,B)
else:
    if M2 > M1 and F2 > F1:
        A = M2 + F1
        B = F2*M1
        print(A,B)
    else:
        if M1 > M2 and F2 > F1:
            A = M1 + F1
            B = M2*F2
            print(A,B)
        else:
            A = M2 + F2
            B = F1*M1
            print(A,B)

#37
qntd_morango = float(input('Informe a quantidade, em quilos, de morando adquirido: '))
qntd_maça = float(input('Informe a quantidade, em quilos, de maça adquirida: '))
frutas = [qntd_morango,qntd_maça]

if frutas[0] <= 5 and frutas[1] <= 5:
    valor_frutas = frutas[0]*2.50 + frutas[1]*1.80
    if frutas[0] + frutas[1] > 8 or valor_frutas > 25.00:
        print('Valor total pago: ', valor_frutas*0.9,'R$')
    else:
        print('Valor total pago: ', valor_frutas,'R$')
if frutas[0] >= 5 and frutas[1] <= 5:
    valor_frutas = frutas[0]*2.20 + frutas[1]*1.80
    if frutas[0] + frutas[1] > 8 or valor_frutas > 25.00:
        print('Valor total pago: ', valor_frutas*0.9,'R$')
    else:
        print('Valor total pago: ', valor_frutas,'R$')
if frutas[0] <= 5 and frutas[1] >= 5:
    valor_frutas = frutas[0]*2.50 + frutas[1]*1.50
    if frutas[0] + frutas[1] > 8 or valor_frutas > 25.00:
        print('Valor total pago: ', valor_frutas*0.9,'R$')
    else:
        print('Valor total pago: ', valor_frutas,'R$')    
if frutas[0] >= 5 and frutas[1] >= 5:
    valor_frutas = frutas[0]*2.20 + frutas[1]*1.50
    if frutas[0] + frutas[1] > 8 or valor_frutas > 25.00:
        print('Valor total pago: ', valor_frutas*0.9,'R$')
    else:
        print('Valor total pago: ', valor_frutas,'R$')

#Q38
cod_usuario = int(input('Digite o código: '))
if cod_usuario != 1234:
    print('Usuário Inválido')
else:
    senha = int(input('Digite a senha: '))
    if cod_usuario == 1234 and senha != 9999:
        print('Senha inválida')
    else:
        print('Acesso Permitido')

#Q39
#a) V
#b) F
#c) F

#Q40
nome = str(input('Nome do produto: '))
quant = int(input('Quantidade Adquirida: '))
prec_uni = float(input('Preço unitário: '))
total = quant*prec_uni

if quant <= 5:
    desconto = 0.02
if quant > 5 and quant <= 10:
    desconto = 0.03
if quant > 10:
    desconto = 0.05

total_pagar = total*(1 - desconto)
print(total_pagar)

#Q41
nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
nota3 = float(input('Nota3: '))
med_ex = float(input('Exercicio: '))
media_aprov = (nota1 + nota2*2 + nota3*3 + med_ex)/7

if media_aprov >= 9:
    print('Conceito A')
if media_aprov >= 7.5 and media_aprov < 9:
    print('Conceito B')
if media_aprov >= 6 and media_aprov < 7.5:
    print('Conceito C')
if media_aprov < 6:
    print('Conceito D')

#Q42
from datetime import datetime
cod_emp = int(input('Codigo do empregado: '))
nasc = int(input('Ano de nascimento: '))
entrada = int(input('Ano de entrada na empresa: '))
current_date = datetime.now()
idade = current_date.year - nasc
tempo = current_date.year - entrada
print('Tem '+ str(idade) + ' anos de idade e ' + str(tempo) + ' anos de tempo de empresa')

if idade >= 65:
    print('Requerer aposentadoria')
else:
    if tempo >= 30:
        print('Requerer aposentadoria')
    else:
        if idade >= 60 and tempo >= 25:
            print('Requerer aposentadoria')
        else:
            print('Não requerer')

#Q43
mens = ['Não forma', 'Escaleno', 'Não forma', 'Equilátero', 'Isósceles']

##################################################################################################################

#Q44 #Q46
#Não achei meios, com o que estudei de python, para fazer essa questão com "FOR". Caso seja com "WHILE", está feita abaixo.

#Q45 #47
valor1 = int(input('Informe o numerador: '))
valor2 = 0
while valor2 == 0:
    valor2 = int(input('Informe o denominador: '))
    print('Valor inválido')
print(valor1/valor2)

#Q48 #Q49
novo = 's'
nota1 = 0
nota2 = 0
while novo.lower() == 's':
    nota1 = float(input('Informe a primeira nota: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Informe a segunda nota: '))
    print((nota1+nota2)/2)
    novo = str(input('Deseja fazer um novo cálculo? [S/N]'))

#Q50
i = 0
while i < 11:
    print(i)
    i = i + 1

#Q51
i = 10
while i > 0:
    print(i)
    i = i - 1

#Q52
i = 101
while i < 111:
    print(i)
    i = i + 1

#Q53 #Q54
n = int(input('informe um valor para N: '))
while n <= 0:
    n = int(input('informe um valor para N: '))

i = 1
while i < n + 1:
    print(i)
    i = i + 1

#Q55 #Q56
valor1 = int(input('Informe o valor desejado pra realizar a tabuada: '))
i = 1

while valor1 <= 0 or valor1 > 10:
    valor1 = int(input('Informe o valor desejado pra realizar a tabuada: '))

while i <= 10:
    print(valor1*i)
    i = i + 1

##################################################################################################################

#Q59
i = 0
cont = 0
while i < 10: 
    number = int(input("Digite um número: "))
    i += 1
    
    if number < 0:
        cont += 1
print(cont)

#Q60
i = 0
cont = 0
interv = 0
while i < 10: 
    number = int(input("Digite um número: "))
    i += 1
    
    if number < 10 or number > 20:
        cont += 1
    else:
        interv += 1

print('Tem, ' + str(cont) + ' valores fora do intervalo (10,20), e ' + str(interv) + ' dentro do intervalo (10,20)')

#Q61
def somar():
    soma = 0
    i = 0
    while i < 10:
        num = int(input("Digite um inteiro: "))
        soma = soma + num
        i += 1
    print("A media foi: ", soma/10)
somar()

#Q62
n = int(input('Entre com a quantidade de alunos: '))
def somar():
    soma = 0
    i = 0
    while i < n:
        num = int(input("Digite um inteiro: "))
        soma = soma + num
        i += 1
    print("A media foi: ", soma/n)
somar()

#Q63
def somar():
    soma = 0
    i = 0
    while i < 10:
        num = int(input("Digite um inteiro: "))
        soma = soma + num
        i += 1
    print("A soma foi: ", soma)
somar()

#Q64
def somar():
    soma = 0
    i = 0
    while i < 10:
        num = int(input("Digite um inteiro: "))
        if num < 40:
            soma = soma + num
            i += 1
        else:
            soma = soma
            i += 1
    print("A soma foi: ", soma)
somar()

#Q65 #Q66
inicio = int(input('Primeiro numero: '))
ultimo = int(input('Ultimo numero: '))
if inicio > ultimo:
    soma = sum(range(ultimo, inicio + 1))
else:
    soma = sum(range(inicio, ultimo + 1))
print(soma)

#67
inicio = 15
ultimo = 100
if inicio > ultimo:
    soma = sum(range(ultimo, inicio + 1))
else:
    soma = sum(range(inicio, ultimo + 1))
print(soma/(ultimo - inicio + 1))

#68
n = int(input('Número de mercadorias: '))

def somar():
    soma = 0
    j = 0
    while j < n:
        v = float(input('Valor da mercadoria ' + str(int(j+1)) + ': '))
        soma = soma + v
        j += 1
    print('A soma foi: ', soma)
    print('A média foi: ', soma/n)
somar()

#69
def somar():
    soma = 0
    cont = 0
    maismerc = 's'
    while maismerc.lower() == 's':
        v = float(input('Valor da mercadoria: '))
        maismerc = str(input('Mais mercadorias (s/n)?'))
        soma = soma + v
        cont += 1
    print('A soma foi: ', soma)
    print('A média foi: ', soma/cont)
somar()

#70 #71
i = 0
lista = []
quant = int(input('Quantidade de números desejada: '))
for i in range(0,quant):
    n = int(input('Digite o valor: '))
    lista.append(n)
    i += 1
print('O minimo: ' + str(min(lista)))
print('O máximo: ' + str(max(lista)))
print('A média: ' + str(sum(lista)/quant))

#72
i = 0
lista = []
quant = 15
for i in range(0,quant):
    cod = str(input('Informe o código do produto: '))
    n = int(input('Digite o valor: '))
    lista.append(n)
    i += 1

print('O máximo: ' + str(max(lista)))
print('A média: ' + str(sum(lista)/quant))

#73
listasalario = []
listafilhos = []
salario = 0
cont = 0
i = 0

while salario >= 0:
    salario = float(input('Informe seu salário: '))
    if salario >= 0:
        nfilhos = int(input('Numero de filhos: '))
        listasalario.append(salario)
        listafilhos.append(nfilhos)
        cont += 1
        if salario < 150:
            i += 1

print('A média do salario: ' + str(sum(listasalario)/cont))
print('A média do número de filhos: ' + str(sum(listafilhos)/cont))
print('Maior salário: ' + str(max(listasalario)))
print('Percentual de pessoas com salario < 150,00: ' + str(int(i/cont)*100) + ' %')

###################################################################################################

#74
i = 0
j = 0
for i in range(1,11):
    print('Tabuada do ' + str(i))
    for j in range(1,11):
        print(str(j) + 'x' + str(i) + ' = ' + str(j*i))
    print('\n')

#75
j = 0
for _ in range(1,11):
    print(str(j) +  ',1,2,3,4,5,6,7,8,9,10')
    j += 1

#76
def desenhaQuadrado(altura, largura, simbolo = '+', preenchimento = ' '):
    print(simbolo * largura)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)

desenhaQuadrado(10, 60)

#77
v = [6, 3, 6, 7, 2, 6, 1, 5]

#78
listpessoas = []

for _ in range(10):
    pessoas = str(input('Digite o nome das pessoas: '))
    listpessoas.append(pessoas)

pessoa1 = input('Digite o nome de quem quer procurar: ')
if pessoa1 in listpessoas[0:10]:
    print('ACHEI')
else:
    print('NÃO ACHEI')

#79
listnotas = []
n = int(input('Insira a quantidade de alunos na turma: '))
for _ in range(n):
    notas = float(input('Digite as notas: '))
    listnotas.append(notas)

media = sum(listnotas)/n
cont = 0
i = 0
for i in range(n):
    if listnotas[i] > media:
        cont += 1
    else:
        cont = cont

print('Media da turma: ' + str(media))
print('Numero de alunos acima da média: ' + str(cont))

#80 #81
Q = []
n = int(input('Insira a quantidade de posições desejadas: '))
for _ in range(n):
    qvalues = int(input('Digite os valores: '))
    while qvalues < 0:
        qvalues = int(input('Digite um valor positivo: '))
    Q.append(qvalues)

print('\n')
print('O maior valor foi: ' + str(max(Q)))
print('Na posição: ' + str(Q.index(max(Q))))
print('\n')
print('O menor valor foi: ' + str(min(Q)))
print('Na posição: ' + str(Q.index(min(Q))))

#82
import numpy as np

A = []
M = []
n = int(input('Insira a quantidade de numeros desejados: '))
for _ in range(n):
    nvalues = int(input('Insira o número: '))
    A.append(nvalues)

X = int(input('Insira o multiplicador da matriz: '))
M = X*np.array(A)
print(M)

#83
A = []

n = int(input('Insira a quantidade de numeros desejados: '))
for _ in range(n):
    nvalues = int(input('Insira o número: '))
    A.append(nvalues)

for i in A[::-1]:
    print(i)

#84
import numpy as np

n = int(input('Insira o tamanho dos vetores A e B: '))
A = []
B = []
soma = []

for _ in range(n):
    avalues = int(input('Insira um número para A: '))
    A.append(avalues)

for _ in range(n):
    bvalues = int(input('Insira um número para B: '))
    B.append(bvalues)

soma = np.array(A) + np.array(B)
print(soma)

#85
listtemp = []
n = int(input('Insira a quantidade de dias do ano que deseja avaliar: '))
for _ in range(n):
    temp = float(input('Digite as temperaturas: '))
    listtemp.append(temp)

media = sum(listtemp)/n
cont = 0
i = 0
for i in range(n):
    if listtemp[i] < media:
        cont += 1
    else:
        cont = cont

print('Maior temperatura registrada: ' + str(max(listtemp)))
print('Menor temperatura registrada: ' + str(min(listtemp)))
print('Media da temperatura desses dias: ' + str(media))
print('Numero de dias abaixo da média: ' + str(cont))

#86
vetor = []

n = int(input('Insira a quantidade de numeros desejada: '))
for _ in range(n):
    vetorvalue = int(input('Digite os numeros: '))
    vetor.append(vetorvalue)

vetor.sort()
print(vetor)

#87
vetor = []

n = int(input('Insira a quantidade de numeros desejada: '))
for _ in range(n):
    vetorvalue = int(input('Digite os numeros: '))
    vetor.append(vetorvalue)

vetor.sort()
print(vetor)

new = int(input('Inserir novo valor no vetor: '))
vetor.append(new)
vetor.sort()
print(vetor)

#88
listnum = []
n = int(input('Informe o tamanho do vetor desejado: '))
for _ in range(n):
    num = int(input('Digite os numeros: '))
    listnum.append(num)
    
num2 = int(input('Digite um número: '))
flag = False
novo = []
for j in listnum:
    if num2 == j:
        flag = True
        listnum.remove(j)
        novo = listnum
        print(novo)

if flag == False:
    print(listnum)

#89
V1 = []
V2 = []

n1 = int(input('Informe o tamanho dos vetores 1 e 2: '))

for _ in range(n1):
    num1 = int(input('Digite os numeros do vetor1: '))
    V1.append(num1)
for _ in range(n1):
    num2 = int(input('Digite os numeros do vetor2: '))
    V2.append(num2)
    
cont = 0
for j in range(n1):
    if V1[j] == V2[j]:
        cont += 1

print('Se repetem ' + str(cont) + ' vezes')

#90
N = []
n1 = int(input('Informe o tamanho do vetor desejado: '))

for _ in range(n1):
    num1 = int(input('Digite os numeros do vetor: '))
    N.append(num1)

new = int(input('Informe um novo numero: '))
cont = 0

for j in range(n1):
    if new == N[j]:
        cont += 1

print('Se repetem', cont, 'vezes')

#91
VET = []

n1 = int(input('Informe o tamanho do vetor desejado: '))

for _ in range(n1):
    num1 = int(input('Digite os numeros do vetor: '))
    VET.append(num1)

i = 0
j = 0
aux1 = []
cont = 0
for i in range(n1):
    for j in range(n1): 
        if VET[i] == VET[j]:
            if i == j:
                cont += 0
            else:
                cont += 1
                aux10 = i+1
                aux1.append(aux10)
                
print('Há', int(cont/2), 'números repetidos nas posições: ')
print(aux1)
      

