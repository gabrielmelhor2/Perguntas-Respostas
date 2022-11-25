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

acertou = False
for pergunta in perguntas:
    print(pergunta["Pergunta"])
    for i, opcão in enumerate(pergunta["Opções"]):
        print(i, ")", opcão)
    escolha = input("Escolha uma opcão: ")
    if escolha == pergunta["Resposta"]:
        print("Resposta Correta!!")
    else:
        print("Resposta Incorreta")
    print()
    