# Checkpoint — Problema da Troca de Moedas 🪙

### Integrantes do Grupo
| Nome Completo | RM |
|----------------|----|
| Leonardo Novaes | [554807] |

---

## 🎯 Introdução e Contextualização

O **Problema da Troca de Moedas** consiste em determinar o **menor número de moedas** necessário para formar um determinado valor **M**, usando moedas de valores inteiros e **quantidade ilimitada**.

Este é um **problema de otimização**, pois busca a **melhor solução possível (mínima quantidade de moedas)** entre todas as combinações possíveis.

---

## 🧩 Natureza do Problema

### Subestrutura Ótima
A solução ótima para o montante `M` depende das soluções ótimas para montantes menores (`M - moeda`).  
Por exemplo, para `M = 6`, a solução ótima depende da melhor forma de formar `M = 3`, `M = 2`, etc.

### Subproblemas Sobrepostos
Os mesmos subproblemas são resolvidos diversas vezes, como `f(3)` aparecendo em vários caminhos recursivos.  
Essa característica é o que permite otimizar o problema com **Memoização (Top-Down)** ou **Programação Dinâmica (Bottom-Up)**.

---

## ⚙️ Análise das Funções

### 1️⃣ Estratégia Gulosa (Iterativa)
- **Ideia:** Escolhe sempre a maior moeda possível até completar `M`.
- **Limitação:** Não garante o resultado ótimo em todos os casos.  
  Exemplo: para `M = 6` e moedas `[1, 3, 4]`, o guloso escolhe `4 + 1 + 1 = 3 moedas`, mas o ótimo é `3 + 3 = 2 moedas`.
- **Complexidade:** `O(n)`

---

### 2️⃣ Recursiva Pura
- **Ideia:** Testa todas as combinações possíveis recursivamente.
- **Desvantagem:** Processa os mesmos subproblemas muitas vezes.
- **Complexidade:** Exponencial `O(2^M)`

---

### 3️⃣ Recursiva com Memoização (Top-Down)
- **Ideia:** Usa cache (dicionário) para guardar resultados já calculados.
- **Vantagem:** Evita recomputação dos mesmos subproblemas.
- **Complexidade:** `O(M * n)`

---

### 4️⃣ Programação Dinâmica (Bottom-Up)
- **Ideia:** Resolve de forma iterativa, preenchendo uma tabela `dp` onde `dp[i]` é o mínimo de moedas para formar `i`.
- **Vantagem:** Dispensa recursão e é mais eficiente.
- **Complexidade:** `O(M * n)`

---

## 📊 Tabela Comparativa

| Método | Abordagem | Tipo | Complexidade | Garante Ótimo |
|--------|------------|------|---------------|----------------|
| Gulosa | Iterativa | Heurística | O(n) | ❌ |
| Recursiva | Pura | Exponencial | O(2^M) | ✅ |
| Recursiva + Memo | Top-Down | PD | O(M·n) | ✅ |
| DP Bottom-Up | Iterativa | PD | O(M·n) | ✅✅ |

---

## 🧠 Conclusão

A **Programação Dinâmica (Bottom-Up)** é a abordagem mais eficiente e robusta para o Problema da Troca de Moedas.  
Ela garante o resultado ótimo com complexidade polinomial e evita o custo de chamadas recursivas.

A compreensão desse problema é essencial para entender como **subestrutura ótima** e **subproblemas sobrepostos** fundamentam a **Programação Dinâmica**, técnica amplamente utilizada em algoritmos de otimização.

---

