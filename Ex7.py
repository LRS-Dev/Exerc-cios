#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
I = int(input("Quantos Anos você tem? "))
M = int(input("Quantos Meses você tem? "))
if M > 12:
    print("12 Meses = 1 Ano, tente novamente! ")
    M = M = int(input("Quantos Meses você tem? "))

D = int(input("Quantos Dias você tem? "))
if D >= 0:
    I_f = (I * 365)
    M_f = (M * 30)
    print("Você tem exatos ", I_f + M_f + D, " dias")
