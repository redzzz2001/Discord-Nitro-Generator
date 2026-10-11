import string
import secrets
import time

print("""
██████╗ ██╗██████╗  ██████╗ ██████╗ ██████╗ ██████╗
██╔══██╗██║██╔═══╝ ██╔════╝██╔═══██╗██╔══██╗██╔══██╗
██║  ██║██║╚█████╗ ██║     ██║   ██║██████╔╝██║  ██║
██║  ██║██║ ╚═══██╗██║     ██║   ██║██╔══██╗██║  ██║
██████╔╝██║██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝
╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝
          ███╗  ██╗██╗████████╗██████╗  ██████╗
          ████╗ ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
          ██╔██╗██║██║   ██║   ██████╔╝██║   ██║
          ██║╚████║██║   ██║   ██╔══██╗██║   ██║
          ██║ ╚███║██║   ██║   ██║  ██║╚██████╔╝
          ╚═╝  ╚══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
██████╗ ███████╗███╗  ██╗███████╗██████╗  █████╗ ████████╗██████╗  ██████╗
██╔═══╝ ██╔════╝████╗ ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║███╗ █████╗  ██╔██╗██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║ ██║ ██╔══╝  ██║╚████║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗███████╗██║ ╚███║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚══════╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    ██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ███████╗███████╗███████╗
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚══███╔╝╚══███╔╝╚══███╔╝
    ██████╦╝ ╚████╔╝ ██████╔╝█████╗  ██║  ██║  ███╔╝   ███╔╝   ███╔╝ 
    ██╔══██╗  ╚██╔╝  ██╔══██╗██╔══╝  ██║  ██║ ███╔╝   ███╔╝   ███╔╝  
    ██████╦╝   ██║   ██║  ██║███████╗██████╔╝███████╗███████╗███████╗
    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝╚══════╝
    V.2.13
     """)

# =========================================================================
# AVISO DE ISENÇÃO DE RESPONSABILIDADE
# =========================================================================
print("=" * 70)
print("                               AVISO IMPORTANTE")
print("=" * 70)
print("")
print("              ATENÇÃO: A maioria dos codigos vai dar expirado.")
print("             (Pode demorar ate voce encontrar um codigo valido)")
print("")
print("=" * 70)

print("\n\nIniciando gerador...\n")
time.sleep(1.5)

def gerar_nitro(comprimento=16):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    return f"https://discord.gift{codigo}"

# Pergunta ao usuário quantos códigos ele deseja gerar
while True:
    try:
        quantidade = int(input("Quantos códigos você deseja gerar? "))
        if quantidade > 0:
            break
        print("Por favor, digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

print(f"\nGerando {quantidade} códigos:\n")

# Gera a quantidade de códigos solicitada pelo usuário
for _ in range(quantidade):
    print(gerar_nitro(16))

