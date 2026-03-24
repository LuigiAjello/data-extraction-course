Com base no `Plano_de_Ensino.md` (focado no cronograma de 2026.1) e enriquecido com os conceitos técnicos do livro de Wes McKinney, aqui está o plano de aula detalhado para a **Aula 09**.

Esta aula resolve o grande problema deixado como "gancho" na aula anterior (a explosão de memória causada pelo _One-Hot Encoding_) e introduz a técnica de transformação reversa: transformar números contínuos em categorias (Binning).

---

# Plano de Aula 09 - Encoding Avançado e Discretização (Binning)

**Disciplina:** Extração e Preparação de Dados (IBM8915)
**Professor:** Luís Aramis
**Data:** 12/03/2026 (Quinta-feira)
**Carga Horária:** 2 tempos de 50 minutos (100 min)
**Tópico:** Tratamento de categorias de altíssima cardinalidade (Frequency/Target Encoding) e conversão de dados contínuos em faixas categóricas (`pd.cut` e `pd.qcut`).

---

## 1. Objetivos da Aula

### Objetivo Geral

Capacitar os alunos a aplicarem transformações complexas de engenharia de _features_, superando as limitações do _One-Hot Encoding_ para textos de alta cardinalidade e aprendendo a simplificar variáveis numéricas contínuas através da discretização.

### Objetivos Específicos

- **Conceitual:** Compreender os riscos do _Target Encoding_ (como o _Data Leakage_ - vazamento de dados) e o propósito analítico de agrupar números em "baldes" (Binning).
- **Técnico (Encoding):** Implementar _Frequency Encoding_ usando `.map()` e _Target Encoding_ usando as agregações `.groupby().mean()`.
- **Técnico (Discretização):** Dominar as funções `pandas.cut()` (para criar intervalos absolutos definidos) e `pandas.qcut()` (para criar compartimentos baseados em quantis populacionais).

---

## 2. Conteúdo Programático

1.  **Revisão (O Limite do One-Hot):**
    - Retomada do desafio da Aula 08: O que fazer com uma coluna de 10.000 CEPs válidos que não podem ser agrupados em "Outros"?
2.  **Encoding Avançado (Para Alta Cardinalidade):**
    - **Frequency/Count Encoding:** Substituir o rótulo ("São Paulo") pela quantidade de vezes que ele aparece no dataset.
    - **Target Encoding (Mean Encoding):** Substituir o rótulo pela **média** da variável alvo (Ex: Substituir o "CEP" pela taxa média de inadimplência daquele CEP).
3.  **Discretização e Compartimentalização (Binning):**
    - Transformando números em faixas de valores (ex: Idade contínua para "Jovem", "Adulto", "Sênior").
    - Uso prático de `pd.cut()`: definindo os limites (bins), fechamento de intervalos (`right=False`) e renomeação de rótulos (`labels`).
    - Uso prático de `pd.qcut()`: dividindo dados em percentis/quartis para evitar faixas vazias em distribuições distorcidas.

---

## 3. Metodologia e Recursos

- **Metodologia:** Aula focada na resolução de problemas (PBL). Inicia-se com a barreira técnica deixada na última aula, passando para a teoria e culminando em _live coding_ interativo.
- **Recursos:** Computador/Projetor, Jupyter Notebook, Biblioteca Pandas.

---

## 4. Cronograma Detalhado (100 min)

### Primeiro Tempo: Domando a Super Cardinalidade (50 min)

| Tempo      | Atividade                                         | Detalhamento do Conteúdo                                                                                                                                                                                                                                       | Fontes de Apoio |
| :--------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
| **10 min** | **O Paradigma do CEP**                            | Relembrar o _get_dummies_. Perguntar: "Se aplicarmos One-Hot numa base com 5 mil cidades, criaremos 5 mil colunas preenchidas de zeros. O PC trava. Como a IA pode ler cidades sem explodir a matriz?"                                                         |                 |
| **20 min** | **Teoria e Prática: Frequency & Target Encoding** | _Live coding_. **Frequency:** Usar `value_counts().to_dict()` e mapear para a coluna. **Target:** Usar o `groupby('cidade')['inadimplente'].mean()` para achar a média de calote por cidade e substituir a string da cidade por essa probabilidade matemática. |                 |
| **20 min** | **Prática (Fim do Lab 07)**                       | Os alunos reabrem o `lab_07_encoders.ipynb` (iniciado na Aula 08). Missão: Aplicar Target Encoding na variável complexa que havia sido deixada para trás sem estourar a memória RAM do DataFrame.                                                              |                 |

### Segundo Tempo: Discretização / Binning (50 min)

| Tempo      | Atividade                       | Detalhamento do Conteúdo                                                                                                                                                                                                                 | Fontes de Apoio |
| :--------- | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
| **15 min** | **Teoria: O que é Binning?**    | Por que transformar números em texto? Explicar o caso de negócio: "Às vezes, a idade exata (31 ou 32 anos) importa menos do que saber se a pessoa pertence à faixa de 'Jovens Adultos'". Introduzir o conceito de "baldes" (bins).       |                 |
| **15 min** | **Live Coding: `cut` e `qcut`** | Demonstração do `pd.cut(idades, bins=)` no Pandas. Mostrar como os intervalos matemáticos ficam `(18, 25]` e como mudar os rótulos passando `labels=['Jovem', 'Adulto', 'Senior']`. Mostrar a diferença sutil com o `qcut` para quantis. |                 |
| **20 min** | **Laboratório (Lab 09)**        | Abertura do notebook `lab_09_binning.ipynb`. Os alunos recebem um dataset com distribuição de Salários reais do Brasil e devem criar 4 faixas salariais lógicas usando `pd.cut`, e analisar a distribuição populacional nessas faixas.   |                 |

---

## 5. Avaliação e Entrega de Portfólio

Conforme as diretrizes da disciplina para a semana de 10 a 12 de março, a entrega de portfólio no GitHub consistirá em:

- **Entregável:** Finalização do Notebook `lab_07_encoders.ipynb` (agora contendo _Target Encoding_ para alta cardinalidade) e entrega do novo Notebook `lab_09_binning.ipynb` na branch principal do repositório `data-extraction-course`.
- **Critérios de Êxito:**
  1.  O aluno conseguiu substituir categorias literais pelas suas respectivas médias alvo usando `groupby().mean()` sem erro de mesclagem.
  2.  O aluno aplicou `pd.cut` numa variável contínua definindo matrizes de fronteiras (ex: `bins=[0, 1000, 3000, np.inf]`) e aplicou _labels_ textuais legíveis para as faixas geradas.

---

## 6. Referências Bibliográficas (Para o Professor)

- **Plano de Ensino Reestruturado (2026.1):** Extração e Preparação de Dados.
- **McKinney, Wes:** _Python para Análise de Dados_. (Capítulo 7: Discretização e compartimentalização - _binning_, Seção de tratamento do `pd.cut` e objetos `Categorical` gerados por ele).
