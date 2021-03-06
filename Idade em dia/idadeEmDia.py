'''
    Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

    Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

    Entrada
    O arquivo de entrada contém um valor inteiro.

    Saída
    Imprima a saída conforme exemplo fornecido
    ex:
    400	
    1 ano(s)
    1 mes(es)
    5 dia(s)
    
'''
from cgitb import reset


anos = 365
meses = 12
dias = 30

entrada = int(input())
ano = entrada // anos

restoDoAno = entrada % anos
mes  = restoDoAno // dias
dia = restoDoAno % dias

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))







