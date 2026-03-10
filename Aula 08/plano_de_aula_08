# Plano de Aula 08 - Tratamento de Categorias: Raros, Cardinalidade e Encoding Básico

**Disciplina:** Extração e Preparação de Dados (IBM8915)
**Professor:** Luís Aramis
**Data:** 10/03/2026 (Terça-feira)
**Carga Horária:** 2 tempos de 50 minutos (100 min)
**Tópico:** Redução de dimensionalidade categórica (agrupamento) e introdução à transformação de texto em matemática (One-Hot e Label Encoding).

---

## 1. Objetivos da Aula

### Objetivo Geral

Capacitar os alunos a manipular e transformar variáveis textuais (categóricas) com alto ruído em formatos matriciais limpos e numéricos, preparando o terreno para que algoritmos matemáticos e de Machine Learning possam processar a informação.

### Objetivos Específicos

- **Analítico:** Compreender o impacto negativo da alta cardinalidade (o fenômeno da _cauda longa_) no desempenho de modelos e na memória.
- **Técnico (Cardinalidade):** Isolar e agrupar categorias raras (baixa frequência) em uma categoria unificada ("Outros") usando ferramentas do Pandas.
- **Técnico (Encoding):** Diferenciar a aplicação de _Label/Ordinal Encoding_ da aplicação de _One-Hot Encoding_ (_Dummy Variables_), utilizando o método `pandas.get_dummies()` na prática.

---

## 2. Conteúdo Programático

1.  **Revisão e o Paradigma do Texto:**
    - Na aula 07 resolvemos os "buracos" numéricos. Hoje o problema são as strings ("Rio de Janeiro", "São Paulo"). O Scikit-Learn e a matemática não compreendem letras.
2.  **Tratamento de Dados Raros (Cardinalidade):**
    - Como definir "raridade" através de proporções usando `df['coluna'].value_counts(normalize=True)`.
    - Estratégia de _Binning_ Categórico: O uso de máscaras booleanas ou `np.where` para forçar valores minoritários para o rótulo `'Other'`.
3.  **Introdução ao Encoding:**
    - **Ordinal/Label Encoding:** Transformação 1 para 1 baseada em hierarquia (ex: "Pequeno=1", "Médio=2", "Grande=3").
    - **One-Hot Encoding (Variáveis Dummy):** Para dados nominais sem hierarquia (ex: "Cor"). Geração de matrizes esparsas.
    - **Armadilha da Variável Dummy:** A importância da exclusão de uma categoria de base para evitar multicolinearidade (explicando o uso de `drop_first=True`).

---

## 3. Metodologia e Recursos

- **Metodologia:** Aula de "Mão na Massa Orientada". Após uma rápida introdução das armadilhas da alta cardinalidade na lousa/projetor, a aula entra nos notebooks para limpar o ruído e converter os dados.
- **Recursos:** Computador/Projetor, Jupyter Notebook, Pandas e NumPy.

---

## 4. Cronograma Detalhado (100 min)

### Primeiro Tempo: O Problema da Cauda Longa e Cardinalidade (50 min)

| Tempo      | Atividade                | Detalhamento do Conteúdo e Código                                                                                                                                                                                           |
| :--------- | :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **10 min** | **Check-in e Hook**      | Conectar com o fim das aulas de nulos. Levantar a questão: "Temos uma coluna de CEPs ou Cidades do interior, a maioria com apenas 1 cliente. Vale a pena o algoritmo decorar tudo isso?"                                    |
| **20 min** | **Teoria e Diagnóstico** | Apresentação do conceito de _Overfitting_ devido ao ruído. Uso no Pandas de `frequencias = df['cidade'].value_counts(normalize=True)` para encontrar o limite de corte (ex: tudo que aparece em menos de 1% da base).       |
| **20 min** | **Prática (Lab 06)**     | Abertura do notebook `lab_06_cardinality.ipynb`. Construir com os alunos um _script_ usando list comprehension, `.map()` ou `df.loc` que converte todas as categorias raras diagnosticadas para a string global `'Outros'`. |

### Segundo Tempo: Tradução Matemática e Encoding (50 min)

| Tempo      | Atividade                               | Detalhamento do Conteúdo e Código                                                                                                                                                                                                           |
| :--------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **15 min** | **Teoria: O Paradigma Dummy**           | Por que não podemos simplesmente dizer que "Azul=1, Verde=2 e Vermelho=3"? (Porque a matemática entenderá que Verde é maior que Azul). Apresentar visualmente a solução do _One-Hot Encoding_ criando colunas booleanas isoladas.           |
| **15 min** | **Live Coding:** <br>`pd.get_dummies()` | Demonstração técnica gerando "Dummy Variables" a partir do Pandas. Execução do comando isolando as colunas categóricas e mostrando como o DataFrame incha horizontalmente.                                                                  |
| **20 min** | **Laboratório (Lab 07)**                | Início do notebook `lab_07_encoders.ipynb`. Missão dos alunos: pegar a coluna limpa no 1º tempo ("Categorias Principais" + "Outros") e explodi-la usando o método `get_dummies(drop_first=True)` para transformá-la 100% em números `int8`. |

---

## 5. Avaliação e Entrega de Portfólio

Conforme as diretrizes do cronograma de atividades no repositório:

- **Entregável Semanal:** Commit dos notebooks **`lab_06_cardinality.ipynb`** concluído e do **`lab_07_encoders.ipynb`** (Início/Parte 1) no repositório `data-extraction-course`.
- **Critérios de Êxito:**
  1.  O aluno reduziu de fato a dimensão categórica (comprovado pela contagem do `.nunique()` antes e depois da limpeza).
  2.  O aluno aplicou a conversão correta com `get_dummies` sobre a coluna tratada, devolvendo a variável livre de strings.

---

## 6. Referências Bibliográficas (Para o Professor)

- **Cronograma Reestruturado:** _Extração e Preparação de Dados (2026.1)_.
- **McKinney, Wes.** _Python para Análise de Dados_. Novatec. (Capítulo 7: Seção `7.2` - Variáveis indicadoras/Dummy usando o método `get_dummies` com o pacote `pandas` e o módulo categórico).
