"""
Enunciado
Como você armazenaria a seguinte tabela usando apenas dicionários? Tente imprimir o valor correspondente
da linha Pedro x Coluna B.

Coluna A	Coluna B
Maria	1	5
Pedro	0.5	3
João	3.2	1

"""
lis_tab=list()
tabela=dict()
resp=True
i=0
while resp==True:

    tabela.clear()
    tabela["nome"]=input("Digite um nome :")
    tabela["coluna A"]=float(input("Coluna A ="))
    tabela["coluna B"]=float(input(f"Coluna B ="))
    lis_tab.append(tabela.copy())

    re=input("Quer continuar S/N :")
    if re != "S":
        resp=False
print(lis_tab[1]["coluna A"]*(lis_tab[0]["coluna B"]+lis_tab[1]["coluna B"]+lis_tab[2]["coluna B"]))
resp=lis_tab[1]["coluna A"]*(lis_tab[0]["coluna B"]+lis_tab[1]["coluna B"]+lis_tab[2]["coluna B"])
print(f"A multiplicacao da linha Pedro pela coluna B e ={resp}")
print(lis_tab)
