# Código para interpretar avaliação, Carlos Eduardo/Horus 1.2
import random
import matplotlib.pyplot as plt

def gerar_avaliacao():
    adjetivos_positivos = ["incrível", "maravilhoso", "ótimo", "emocionante", "fantástico"]
    adjetivos_negativos = ["terrível", "horrível", "péssimo", "chato", "desapontador"]
    aleatorio = random.choice([True, False, None])

    if aleatorio is True:
        return f"Esse filme foi {random.choice(adjetivos_positivos)}!"
    elif aleatorio is False:
        return f"Que filme {random.choice(adjetivos_negativos)}, perdi meu tempo assistindo isso."
    else:
        neutras = ["O filme foi mais ou menos.", "Nada demais, nem bom nem ruim.", "Foi OK, não me impressionou muito."]
        return random.choice(neutras)

def analisar_sentimento(avaliacao):
    palavras_positivas = ["incrível", "maravilhoso", "ótimo", "emocionante", "fantástico"]
    palavras_negativas = ["terrível", "horrível", "péssimo", "chato", "desapontador"]

    positivas = sum(avaliacao.lower().count(p) for p in palavras_positivas)
    negativas = sum(avaliacao.lower().count(n) for n in palavras_negativas)

    if positivas > negativas:
        return "positivo"
    elif negativas > positivas:
        return "negativo"
    else:
        return "neutro"

def visualizar_resultados(avaliacoes):
    sentimentos = {"positivo": 0, "negativo": 0, "neutro": 0}

    for avaliacao in avaliacoes:
        sentimento = analisar_sentimento(avaliacao)
        sentimentos[sentimento] += 1

    plt.bar(sentimentos.keys(), sentimentos.values(), color=['green', 'red', 'blue'])
    plt.xlabel('Sentimento')
    plt.ylabel('Quantidade')
    plt.title('Distribuição de Sentimentos das Avaliações de Filmes')
    plt.show()

def main():
    num_avaliacoes = int(input("Quantas avaliações de filmes você deseja gerar? "))

    avaliacoes = []
    for _ in range(num_avaliacoes):
        avaliacao = gerar_avaliacao()
        avaliacoes.append(avaliacao)

    print("\nAvaliações de filmes geradas:")
    for avaliacao in avaliacoes:
        print(avaliacao)

    print("\nResultados da análise de sentimento:")
    for avaliacao in avaliacoes:
        sentimento = analisar_sentimento(avaliacao)
        print(f"Avaliação: '{avaliacao}' - Sentimento: {sentimento}")

    print("\nVisualização dos resultados:")
    visualizar_resultados(avaliacoes)

if __name__ == "__main__":
    main()