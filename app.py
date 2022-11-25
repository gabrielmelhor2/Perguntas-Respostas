#Desafio Perguntas e Respostas
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta":  "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["58", "49", "13", "25"],
        "Resposta": "25"
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["5", "98", "0", "7"],
        "Resposta": "5"
    }
]

qtd_acertos = 0
for pergunta in perguntas:
    
    print(pergunta["Pergunta"])
    for i, opcão in enumerate(pergunta["Opções"]):
        print(i, ")", opcão)
    escolha = int(input("Escolha uma opcão: "))
    if escolha == int(pergunta["Resposta"]):
        qtd_acertos += 1
        print("Resposta Correta!!")
    else:
        print("Resposta Incorreta!!")
        print()
print(f"Você acertou {qtd_acertos} perguntas")
    