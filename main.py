# =============================================
# CHECKPOINT - Problema da Troca de Moedas
# Autores: Leonardo Novaes rm554807
# =============================================

def qtdeMoedas(M, moedas):
    """
    Estratégia Gulosa (Iterativa)
    ----------------------------------
    Determina a menor quantidade de moedas (notas) para compor o montante M,
    escolhendo sempre a maior moeda possível a cada passo.
    *Nem sempre produz o resultado ótimo.*

    Parâmetros:
    M (int): montante total.
    moedas (list[int]): lista com os valores das moedas disponíveis.

    Retorno:
    int: quantidade mínima de moedas ou -1 se não for possível formar M.

    Complexidade:
    - Tempo: O(n), onde n é o número de tipos de moedas.
    - Melhor caso (Ω): O(1), se a primeira moeda já forma o valor.
    - Pior caso (Θ): O(n), pois percorre todas as moedas.
    """
    moedas.sort(reverse=True)
    count = 0
    for moeda in moedas:
        if M >= moeda:
            num = M // moeda
            count += num
            M -= num * moeda
    return count if M == 0 else -1







# ===============================
# TESTES DE EXEMPLO
# ===============================
if __name__ == "__main__":
    print("Gulosa:", qtdeMoedas(6, [1, 3, 4]))
