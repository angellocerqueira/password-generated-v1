import string
import random

print ('GERADOR DE SENHA PROFISSIONAL')
print('=' * 30)

tamanho = int(input('quantos caracteres sua senha deve ter? '))

usar_maiusculas = input("incluir letras maiúsculas? (s/n): ").lower() == "s"
usar_minusculas = input("incluir letras minúsculas? (s/n ) ").lower() == "s"
usar_numero = input ("incluir números em sua senha? (s/n) ").lower() == "s"
usar_simbolos = input ("incluir sínbolos em sua senha (!@#$%)? (s/n) ").lower() == "s"
caracteres = ""
if usar_maiusculas:
    caracteres += string.ascii_uppercase
if usar_minusculas:
    caracteres += string.ascii_lowercase
if usar_numero:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

if not caracteres:
    print("Você deve escolher pelo menos uma opção!")
else:
    senha = ''.join(random.choice(caracteres) for _ in range (tamanho))
    print(f"\nSua senha gerada é {senha}")
        


