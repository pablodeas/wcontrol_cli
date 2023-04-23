# IMPORTS
import json
import sys
from datetime import datetime, timedelta

# OBJETO DATA
hoje = datetime.now().date()
dias_ate_domingo = (6 - hoje.weekday()) % 7
domingo = hoje + timedelta(dias_ate_domingo)
# FORMATANDO AS DATAS
hoje_c = hoje.strftime("%d, %B %Y")
domingo_c = domingo.strftime("%d, %B %Y")
# LIMITE SEMANAL
limite_semanal = 120

# TELA DE ABERTURA - MENU

print(f"""
Bem vindo ao Controlador de Gastos Semanais!

O limite de gastos está atualmente no valor de R${limite_semanal}

Estamos no dia: {hoje_c}

Proximo domingo será: {domingo_c}
""")
def menu():
    print(f"""
* Escolha uma opção abaixo *

1 - Inserir novo valor.
2 - Verificar valor disponível.
3 - Sair.
""")


def new_value(file_path, key, value):
    with open(file_path, 'r') as f:
        data = json.load(f)
        data[key] = value
    with open('dados.json', 'w') as f:
        json.dump(data, f)
    return "Tudo certo!"


def sum_values(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        total = 0
    for value in data.values():
        total += value
    print("R$", limite_semanal - total)

menu()
choose = int(input("-> "))

while choose != 3:
    if choose == 1:
        valor = int(input("Digite o valor: \n"))
        dia = input("Digite o dia: \n")
        new_value('dados.json', dia, valor)
        menu()
        choose = int(input("-> "))
    else:
        print()
    
    if choose == 2:
        sum_values('dados.json')
        menu()
        choose = int(input("-> "))
    else:
        print()
    
    if choose == 3:
        print("Saindo... \n")
    else:
        print()
    
    if choose == 0 or choose >= 4:
        print("Você escolheu uma opção errada, tente novamente!")
    else:
        print()
else:
    sys.exit()