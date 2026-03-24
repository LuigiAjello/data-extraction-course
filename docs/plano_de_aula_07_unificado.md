# Plano de Aula 07 - Dados Ausentes: Tratamento Univariado e Multivariado

**Disciplina:** Extração e Preparação de Dados (IBM8915)
**Professor:** Luís Aramis
**Tópico:** Descarte de dados ausentes, preenchimento (imputação) estatístico univariado e algoritmos de machine learning para imputação multivariada.

---

## 1. Bloco Teórico

### 1.1. Dados Ausentes: Tratamento Univariado (Simples)

**Objetivos da Teoria Univariada:**

- Capacitar os alunos a decidir entre o descarte e o preenchimento de dados ausentes, aplicando técnicas de imputação simples (média, mediana, moda) e avaliando o impacto dessas modificações.
- Compreender os riscos de viés estatístico ao substituir valores ausentes por medidas de tendência central univariadas (ex: reduzir a variância artificialmente e a "cegueira contextual").

**Conteúdo Teórico:**

- **Revisão e Estratégias:** Quando um "buraco" no dataset é tratável? Deletar vs. Imputar.
- **Exclusão de Dados (Listwise/Pairwise Deletion):** O método `dropna()`: exclusão de linhas com qualquer valor ausente vs. exclusão de colunas (`axis=1`). Uso de `how='all'` e limites numéricos com `thresh`.
- **Imputação Univariada com Constantes e Estatísticas:** O método `fillna()` como a "força de trabalho" para substituição de lacunas.
  - Preenchimento com valor constante (ex: 0 ou "Desconhecido").
  - Preenchimento estatístico usando `mean()`, `median()` e `mode()`.
  - Discussão: Por que variáveis com outliers severos exigem a mediana no lugar da média.

### 1.2. Dados Ausentes: Tratamento Multivariado (Avançado)

**Objetivos da Teoria Multivariada:**

- Compreender a diferença entre imputação univariada (olha apenas para a própria coluna) e multivariada (olha para a linha inteira, acha padrões e utiliza correlações para preencher lacunas).

**Conteúdo Teórico:**

- **Imputação baseada em Vizinhança (KNN):** A lógica básica do algoritmo K-Nearest Neighbors (KNN) aplicado à reconstrução de dados. Como o `KNNImputer` calcula a distância entre linhas para achar os registros mais "parecidos".
- **Imputação Iterativa (Modelagem de Equações):** Como o `IterativeImputer` cria um modelo de regressão para cada coluna esburacada usando as outras colunas como "previsores".
- **Integração Pandas e Scikit-Learn:** O método `.fit_transform()` e o retorno em formato NumPy array. Como reconstruir o DataFrame Pandas após o Scikit-Learn remover os nomes das colunas.

---

## 2. Bloco Prático e Laboratório

**Metodologia:** Laboratório prático precedido e intercalado com breves exposições teóricas e live coding.

### 2.1. Laboratório de Tratamento Univariado (A "Faca" e a "Seringa")

- **A "Faca" (`dropna`):** Demonstração de como descartar linhas totalmente nulas ou colunas excessivamente vazias.
- **A "Seringa" (`fillna`):** Substituição por constante em colunas específicas (uso de dicionários no `.fillna()`). Modificações com `inplace=True`.
- **Imputação com Estatística:** Demonstração prática do comando `df.fillna(df.mean())`.
- **Início do `lab_05_imputation.ipynb`:**
  - Carregar os dados defeituosos.
  - Descartar colunas intratáveis (>70% de ausência).
  - Imputar a média ou mediana nas colunas tratáveis, conforme a distribuição da variável.

### 2.2. Laboratório de Tratamento Multivariado (Scikit-Learn)

- **Live Coding `KNNImputer`:**
  - Importação de `from sklearn.impute import KNNImputer`.
  - Instanciação do imputador (`imputer = KNNImputer(n_neighbors=5)`).
  - Execução do `imputer.fit_transform(df)`.
  - Passo crucial: Reconstruir o dataset com `pd.DataFrame(dados_numpy, columns=df.columns)`.
- **Live Coding `IterativeImputer`:** Demonstração simples da configuração da regressão múltipla para imputação.
- **Finalização do `lab_05_imputation.ipynb`:**
  - Criação de uma nova subseção no laboratório.
  - Imputar os nulos do dataset original usando o `KNNImputer`.
  - Comparar o resultado estatístico usando `.describe()` entre a versão do `.fillna()` e a versão multivariada.

---

## 3. Avaliação e Entrega (Portfólio)

- **Entrega Final:** Versão concluída do Notebook `lab_05_imputation.ipynb` no repositório `data-extraction-course`.
- **Critério de Avaliação:**
  - Código funcional aplicando corretamente o descarte (dropna) e o preenchimento univariado (fillna).
  - Demonstração da capacidade de importar um imputador da `scikit-learn`.
  - Aplicação correta do imputador multivariado e conversão do array NumPy de volta para um DataFrame legível no Pandas, contendo os nomes das colunas e sem erros de execução.

---

## 4. Referências Bibliográficas

- **Plano de Ensino e Cronograma da Disciplina.**
- **McKinney, Wes.** _Python para Análise de Dados_. (Capítulo 7: Limpeza e preparação dos dados).
- **Documentação Oficial do Scikit-Learn:** Guia de Usuário sobre Imputação de Valores Ausentes (`sklearn.impute`).
