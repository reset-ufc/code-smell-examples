# Exemplos de código para cada smell

**NaN Equivalence Comparison Misused:** é um "code smell" que ocorre quando a comparação de valores NaN (Not a Number) é feita de maneira
incorreta ou ineficiente no código-fonte.

**Empty Column Misinitialization:** é um code smell que ocorre em bancos de dados relacionais quando uma coluna é inicializada com um 
valor incorreto para indicar uma condição vazia.

**Memory Not Freed:** É um code smell que ocorre quando a alocação de memória não é corretamente liberada após o uso. 
Esse code smell é mais comum em linguagens de programação que fornecem recursos de gerenciamento manual de memória, como C ou C++.

**Columns and DataType Not Explicitly Set:** Refere-se a uma situação em que as colunas de uma estrutura de dados, como um banco de dados ou uma 
tabela, não têm seus tipos de dados explicitamente definidos. Isso geralmente ocorre quando as colunas são 
criadas sem especificar seus tipos ou quando os tipos de dados são inferidos automaticamente pelo sistema, 
mas não são verificados ou ajustados manualmente.

**Chain Indexing:** Esse code smell ocorre quando há uma cadeia de índices sendo usada para acessar propriedades ou 
elementos em um objeto ou matriz.

**In-Place APIs Misused:** Refere-se a uma situação em que APIs ou funções de um sistema são usadas de maneira incorreta ou inadequada, 
resultando em efeitos indesejados ou comportamentos inesperados. Especificamente, esse code smell ocorre quando 
APIs de modificação em tempo real, também conhecidas como "in-place" ou "mutating APIs", são usadas de forma 
inadequada, levando a resultados indesejáveis ou inesperados.

**Data Leakage:** É um code smell que ocorre quando há um fluxo não intencional de informações entre conjuntos de dados 
durante o treinamento ou avaliação de um modelo de machine learning. Esse vazamento pode levar a 
resultados falsamente otimistas e não realistas durante a fase de teste ou validação do modelo.

**No Scaling before Scaling-Sensitive Operation:** Existem muitas operações sensíveis ao escalonamento de recursos, como
Análise de Componente Principal (PCA). A falta de dimensionamento pode levar a uma conclusão errada. Por
exemplo, se uma variável estiver em uma escala maior que outra, ela dominará o
procedimento PCA . Portanto, o PCA sem dimensionamento de recursos pode produzir
um resultado de componente principal incorreto.

**Unnecessary Iteration:** Padrão de código que indica a presença de iterações repetitivas ou redundantes, que não são essenciais ou
não contribuem para a funcionalidade ou eficiência do código.

**Merge API Parameter Not Explicitly Set:** É um code smell que ocorre quando os parâmetros de mesclagem (merge) em uma API não são 
explicitamente definidos ou configurados corretamente.