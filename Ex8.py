Eleitores_muni = int(input("Quantos eleitores tem no seu município? "))
Votos_Br = int(input("Quantos votos brancos foram? "))
if Votos_Br > Eleitores_muni:
    Votos_Br = int(input("Erro, tente novamente! "))
    
Votos_Nu = int(input("Quantos votos nulos foram? "))
if Votos_Nu > Votos_Br:
    Votos_Nu = int(input("Erro, tente novamente! "))

Votos_Va = int(input("Quantos votos válidos foram? "))
if Votos_Va > Votos_Nu:
    Votos_Va = int(input("Erro, tente novamente! "))
print((Votos_Br / Eleitores_muni) * 100, "%")
print((Votos_Nu / Eleitores_muni) * 100, "%")
print((Votos_Va / Eleitores_muni) * 100, "%")