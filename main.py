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


def qtdeMoedasRec(M, moedas):
    """
    Função Recursiva Pura (Sem Memoização)
    -----------------------------------------
    Calcula recursivamente o número mínimo de moedas para formar M.
    Testa todas as combinações possíveis, o que gera reprocessamentos.

    Parâmetros:
    M (int): montante total.
    moedas (list[int]): lista de valores das moedas disponíveis.

    Retorno:
    int: quantidade mínima de moedas ou -1 se não for possível formar M.

    Complexidade:
    - Tempo: O(2^M), pois há sobreposição de subproblemas.
    - Melhor caso (Ω): O(1), se M = 0.
    - Pior caso (Θ): O(2^M).
    """
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    min_moedas = float('inf')
    for moeda in moedas:
        resultado = qtdeMoedasRec(M - moeda, moedas)
        min_moedas = min(min_moedas, resultado + 1)

    return min_moedas if min_moedas != float('inf') else -1

def qtdeMoedasRecMemo(M, moedas, memo=None):
    """
    Função Recursiva com Memoização (Top-Down)
    ----------------------------------------------
    Usa cache (memo) para armazenar resultados já calculados.
    Evita o reprocessamento dos mesmos subproblemas.

    Parâmetros:
    M (int): montante total.
    moedas (list[int]): lista de valores das moedas disponíveis.
    memo (dict): dicionário usado para armazenar subresultados.

    Retorno:
    int: quantidade mínima de moedas ou -1 se não for possível formar M.

    Complexidade:
    - Tempo: O(M * n), onde n é o número de moedas.
    - Melhor caso (Ω): O(M).
    - Pior caso (Θ): O(M * n).
    """
    if memo is None:
        memo = {}

    if M in memo:
        return memo[M]
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    min_moedas = float('inf')
    for moeda in moedas:
        resultado = qtdeMoedasRecMemo(M - moeda, moedas, memo)
        min_moedas = min(min_moedas, resultado + 1)

    memo[M] = min_moedas
    return min_moedas if min_moedas != float('inf') else -1



# ===============================
# TESTES DE EXEMPLO
# ===============================
if __name__ == "__main__":
    print("Gulosa:", qtdeMoedas(6, [1, 3, 4]))
    print("Recursiva:", qtdeMoedasRec(6, [1, 3, 4]))
    print("Recursiva Memo:", qtdeMoedasRecMemo(6, [1, 3, 4]))
