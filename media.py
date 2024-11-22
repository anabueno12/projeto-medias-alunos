# media.py

# Entrada: Receber as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processo: Calcular a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Saída: Exibir o resultado da média
print(f"A média do aluno é: {media:.2f}")

# Verificar a situação do aluno com base na média
if media >= 6.0:
    print("Aprovado")
elif media > 5.0 and media < 6.0:
    print("Recuperação")
else:
    print("Reprovado")
