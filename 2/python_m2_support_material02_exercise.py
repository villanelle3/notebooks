# -*- coding: utf-8 -*-
"""Python_M2_support material02_exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15jgkuymvk67RXOzxb8VTQ0DRtUEEy4yl

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo** | Python: Estruturas de Dados
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Listas;</li>
  <li>Conjuntos;</li>
  <li>Dicionários.</li>
</ol>

---

# **Exercícios**

## 1\. Listas

Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

filmes = ['Um Sonho de Liberdade',
    'O Poderoso Chefão',
    'Batman: O Cavaleiro das Trevas',
    'O Poderoso Chefão II',
    '12 Homens e uma Sentença',
    'A Lista de Schindler',
    'O Senhor dos Anéis: O Retorno do Rei',
    'Pulp Fiction - Tempo de Violência',
    'O Senhor dos Anéis: A Sociedade do Anel',
    'Três Homens em Conflito']

print(filmes)

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.


"""

# trocar a posição do primeiro e do segundo filme da lista
filmes.insert(1, filmes.pop(0))

print(filmes)

"""---

## 2\. Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

# Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
tres_ultimos = filmes[len(filmes)-3:len(filmes)]
filmes.extend(tres_ultimos)
print(filmes)

"""

```
# Isto está formatado como código
```

Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado."""

# Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado.
filmes = list(set(filmes))
print(filmes)

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}`.
"""

filmes = [{'nome': 'Um Sonho de Liberdade', 'ano': 1994, 'sinopse': 'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'},
        {'nome':'O Poderoso Chefão', 'ano': 1972, 'sinopse': '<sinopse do filme>'},
        {'nome': 'Batman: O Cavaleiro das Trevas', 'ano': 2008, 'sinopse': '<sinopse do filme>'},
        {'nome': 'O Poderoso Chefão II', 'ano': 1974, 'sinopse': '<sinopse do filme>'},
        {'nome': '12 Homens e uma Sentença', 'ano': 1957, 'sinopse': '<sinopse do filme>'},
        {'nome': 'A Lista de Schindler', 'ano': 1993, 'sinopse': '<sinopse do filme>'},
        {'nome': 'O Senhor dos Anéis: O Retorno do Rei', 'ano': 2003, 'sinopse': '<sinopse do filme>'},
        {'nome': 'Pulp Fiction - Tempo de Violência', 'ano': 1994, 'sinopse': '<sinopse do filme>'},
        {'nome': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': 2001, 'sinopse': '<sinopse do filme>'},
        {'nome': 'Três Homens em Conflito', 'ano': 1966, 'sinopse': '<sinopse do filme>'}]

print(filmes)