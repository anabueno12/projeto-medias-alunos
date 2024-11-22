# media.py

# Entrada: Receber as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Definir os pesos
peso1 = 1
peso2 = 1
peso3 = 2

# Processo: Calcular a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Saída: Exibir o resultado da média ponderada
print(f"A média ponderada do aluno é: {media_ponderada:.2f}")

# Verificar a situação do aluno com base na média ponderada
if media_ponderada >= 6.0:
    print("Aprovado")
elif media_ponderada > 5.0 and media_ponderada < 6.0:
    print("Recuperação")
else:
    print("Reprovado")
