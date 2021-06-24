
# Projeto `Identificação e visualização de padrões moleculares em compostos inibidores de proteínas associadas ao câncer: Uma abordagem usando aprendizado de máquina`
# Project `Identification and visualization of molecular patterns of compounds that inhibit cancer-related proteins: A machine learning approach`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2021, na Unicamp.

 |Nome  | RA | Especialização|
 |--|--|--|
 | Álvaro Airemoraes Capelo  | 104534  | Engenharia Química|
 | André Eidi Toyota  | 235610  | Ciências Farmacêuticas|
 | Gabriel Oliveira dos Santos  | 197460  | Ciência da Computação|
 | Leonardo Yudi Yamaguishi  | 178674  | Engenharia de Alimentos|


# Descrição Resumida do Projeto

Os avanços em tecnologia da informação e em técnicas de processamento de dados veem permitindo avanços significativos também em outros domínios.
Um desses domínios é o de descoberta de novos fármacos, no qual técnicas de Aprendizado de Máquina podem ser utilizados para otimizar várias etapas do processo. Por exemplo, na descoberta e predição de pequenas moléculas candidatas a inibição. Interessados nesta etapa em particular, neste trabalho, utilizamos _fingerprints_ de Morgan para representar moléculas candidatas e aplicamos algoritmos de aprendizado de máquina baseados em árvore para prever ação inibitória frente à enzima EGFR/ErbB1, associado ao câncer. A seguir, aplicamos algoritmos de interpretação para identificar e investigar os principais padrões que correspondem a uma atividade inibitória.
Esse método foi capaz de corretamente identificar o padrões moleculares de relevância e atividade farmacofórica frente à enzima alvo conhecida em literatura, sugerindo que esse método pode ser usado de maneira análoga no estudo e investigação de moléculas candidatas e padrões moleculares para inibição de outras enzimas-alvo.
Adicionalmente, foram observados subgrupos dentre as moléculas inibidoras caracterizados por padrões moleculares específicos. Essas especificidades foram analisadas para três grupos, mas a investigação requer trabalhos futuros.

*Palavras-chave*: _morgan fingerprints_, _predição_, _interação molécula-enzima_, _aprendizado de máquina_


# Vídeos do Projeto

[Vídeo da Proposta](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/datasci4health_proposta_projeto.mp4)

[Vídeo da Apresentação Final]()

# Slides do Projeto

[Slides da Proposta]()

[Slides da Apresentação Final]()



# Introdução e Referenciais de Teóricos
  O câncer pode ser definido como uma síndrome que engloba mais de 200 doenças, em que as células se dividem expressivamente de forma anormal, invadindo outros tecidos. Cada tipo de câncer se atém a sua especificidade quanto à etiologia genética, histológica, celular, e bioquímica, divergindo assim quanto à progressão patológica, diagnóstico, prognóstico e resposta à terapêutica [6]. Este problema de saúde é de notoriedade e preocupação global, sendo uma das quatro principais causas de morte antes dos 70 anos de idade. Mais de 18 milhões de novos casos de câncer emergiram no mundo no ano de 2018, onde mais da metade destes casos evoluiu para óbito. O câncer de pulmão é o mais incidente, com mais de 2 milhões de casos, seguido pelo câncer de mama, cólon e reto, e próstata [7]. 

 É reconhecido que as tirosina quinases estão envolvidas em diversas etapas do desenvolvimento e progressão do câncer, contribuindo de forma ativa para a proliferação celular e metástase, sem estarem correlacionadas com a sua gênese [8]. Tirosina quinases são enzimas que atuam por mecanismos de fosforilação de polipeptídeos através do ATP, e estão diretamente associadas à proliferação, sobrevivência, diferenciação, funcionalidade e motilidade celular [10]. Essas enzimas são classificadas em dois grandes grupos nomeados receptores ou não receptores, sendo que o primeiro citado é um grupo que caracteriza um domínio de ligação transmembrana glicosilado, conectado a um domínio citoplasmático da enzima catalítica tirosina quinase [8].

 O primeiro receptor de proteína tirosina quinase descrito, o Epidermal Growth Factor Receptor (EGFR) é constituído por uma família de quatro membros, sendo eles o ErbB1/HER1, ErbB2/HER2, ErbB3/HER3 e ErbB4/HER4. Diversos tipos de cânceres têm sido associados com o aumento da estimulação e/ou expressão de ErbB1, como os tumores de bexiga, mama, cabeça e pescoço, rim, pulmão de células não pequenas e próstata, pelo qual se ligam com alta afinidade pelas proteínas Epidermal Growth Factor (EGF) e Transforming Growth Factor-α (TGF-α) [9].

 Diversas terapias na tentativa de inibição da ativação de proteínas tirosina quinase têm sido estudadas como terapia tumoral, entre as mais diversas podemos citar a utilização de pequenas moléculas inibidoras do substrato-ligante, bem como do complexo catalítico de tirosina quinase, e ainda mais inovador, a utilização de anticorpos que se ligam tanto em receptores quanto em ligantes [10].

 Portanto, é de extrema relevância a busca por novas moléculas inibidoras, de forma a viabilizar um tratamento efetivo, seguro e compatível com a vida de todos aqueles que padecem desta grande enfermidade chamada câncer. Tendo esse cenário em vista, exploraramos por meio de ferramentas de ciência de dados, potenciais moléculas inibidoras de ErbB1/HER1.

```
- adicionar parágrafo sobre Machine Learning aplicado a descoberta de drogas. referenciar papers: André
- Machine Learning Methods in Drug Discovery, Patel, L. et al. doi:10.3390
- Cano, G.; Garcia-Rodriguez, J.; Garcia-Garcia, A.; Perez-Sanchez, H.; Benediktsson, J.; Thapa, A.; Barr, A. Automatic     selection of molecular descriptors using random forest: Application to drug discovery. Expert Syst. Appl. 2017, 72, 151–15    9.
```

> Indicação (bastante resumida) da análise proposta
>
> Indicação (bastante resumida) dos resultados alcançados



# Pergunta de Pesquisa
Quais são os principais padrões moleculares associadas ao comportamento inibitório frente à enzima EGFR/ErbB1, relacionada ao câncer?

# Objetivos do Projeto
Identificar os principais padrões moleculares associados ao comportamento inibitório frente à enzima EGFR/ErbB1, relacionada ao câncer, através de técnicas de Machine Learning.

# Metodologia
Foi utilizada a metodologia _Knowledge Discovery in Databases_[11] proposta por Fayyad et al. em 2016. Partindo da base de dados _Cancer Inhibitors_[1] do Kaggle, foram selecionados os dados correspondentes à enzima EGFR/ErbB1 como conjunto de estudo. 


# Bases de Dados e Evolução
 Nós utilizamos a base de dados [Cancer Inhibitors](https://www.kaggle.com/xiaotawkaggle/inhibitors) [1] disponibilizada na plataforma Kaggle. Essa base contém informações sobre a estrutura de moléculas coletadas  a partir da ChEMBL[2]. Para cada uma dessas moléculas, há uma anotação se ela inibe ou não uma proteína quinase. Há oito proteínas disponíveis, mas apenas a EGFR/ErbB1 será utilizada nesse trabalho.

 Ao analisar a base de dados, é evidente que sua proposta é a identificação de padrões estruturais nas moléculas que justifiquem a inibição ou não inibição das enzimas a partir de um método de codificação chamado Fingerprinting. Este método apresenta diferentes abordagens, entre elas, as abordagens estruturais e as abordagens farmacofóricas (focadas nas funcionalidades da molécula), que se relacionam diretamente à forma que as moléculas são interpretadas pelos algoritmos de Data Mining.

## Bases Estudadas mas Não Adotadas

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Cyclin-dependent kinase 2: cdk2 | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=cdk2.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase cdk2. Essa base contém 1270 inibidoras e 618 não-inibidoras da proteína kinase cdk2. 
Glycogen synthase kinase-3 beta: gsk3b | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=gsk3b.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase gsk3b. Essa base contém 1676 inibidoras e 512 não-inibidoras da proteína kinase gsk3b.
Hepatocyte growth factor receptor: hgfr | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=hgfr.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase hgfr. Essa base contém 2551 inibidoras e 326 não-inibidoras da proteína kinase hgfr.
MAP kinase p38 alpha: mapkp38a | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=map_k_p38a.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase mapkp38a. Essa base contém 4086 inibidoras e 582 não-inibidoras da proteína kinase mapkp38a.
Tyrosine-protein kinase LCK: tpk_lck | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=tpk_lck.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase tpk_lck. Essa base contém 1628 inibidoras e 539 não-inibidoras da proteína kinase tpk_lck.
Tyrosine-protein kinase SRC: tpk_src | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=tpk_src.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase tpk_src. Essa base contém 2414 inibidoras e 1171 não-inibidoras da proteína kinase tpk_src.
Vascular endothelial growth factor receptor 2: vegfr2 | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=vegfr2.h5 | Base com moléculas inibidoras ou não-inibidoras da proteína kinase vegfr2. Essa base contém 5656 inibidoras e 1202 não-inibidoras da proteína kinase vegfr2.

Essas bases de dados não foram adotadas pois apresentavam poucos dados ou desbalanceamento significativo. 

## Bases Estudadas e Adotadas

Base de Dados | Endereço na Web | Resumo descritivo
----- | ----- | -----
Epidermal growth factor receptor erbB1: egfr_erbB1 | https://www.kaggle.com/xiaotawkaggle/inhibitors?select=egfr_erbB1.h5 |  Base com moléculas inibidoras ou não-inibidoras da proteína kinase egfr_erbB1. Essa base contém 5010 inibidoras e 1925 não-inibidoras da proteína kinase egfr_erbB1.

Essa base contém dados de moléculas associadas à proteína kinase egfr_erbB1. Essas moléculas são identificadas pelos seus respectivos ChEMBL IDs (identificadores na base de dados ChEMBL) e suas respectivas labels (1 para inibidoras e 0 para não inibidoras). Para seguir com a análise computacional proposta, foi necessário que estes dados fossem transformados em dados interpretáveis por algoritmos de aprendizado de máquina, para isso, foi empregado um método de Fingerprinting disponível na biblioteca RDKit[4].

### Geração de Fingerprints:

O método de Fingerprinting utilizado gera Fingerprints conhecidas como Morgan Fingerprints ou Circular Fingerprints, vetores de extensão definida em que cada elemento represeta uma sub-estrutura molecular que compõe a molécula inputada. As sub-estruturas moleculares, por sua vez, são obtidas considerando um raio, quantidade de átomos vizinhos, determinado. Os inputs utilizados para a geração das Fingerprints dets projeto foram foram:

* A representação das moléculas em notação SMILES (Simplified Molecular-Input Line-Entry System), obtida com auxílio da biblioteca chembl_webresource_client [15] que acessa a base do ChEMBL e busca uma molécula a partir de seu ChEMBL ID
* Tamanho do vetor = 2048
* Número de átomos vizinhos = 2

A geração de uma Fingerprint tem como primeiro passo a identificação de cada um dos átomos não-hidrogênio da molécula com um número inteiro, esta identificação tem como base informações locais, contemplando diferentes propriedades atômicas, como, por exemplo, seu número atômico e número de ligações. Posteriormente, os identificadores são atualizados iterativamente de forma que os identificadores iniciais sejam combinados com os átomos vizinhos até o diâmetro determinado inicialmente. A combinação resultante então passa por um método de hashing e os identificadores são listados, este processo de atualização interativa é baseada no Algoritmo de Morgan [12]. Por fim, ocorre a remoção de identificadores repetidos [13]. Neste projeto, a contagem de cada identificador não foi mantida, de forma que a saída seja um vetor de bits esparso. 

Durante a geração da Fingerprint, a biblioteca RDKit permite o armazenamento de um dicionário (bitInfo) onde as chaves são os índices do vetor (Fingerprint) codificados pela molécula e os valores são tuplas com a posição dos átomos e raios que codificaram determinada estrutura [14].

{índice: (posição do átomo, raio do átomo)}
 
Esta informação foi armazenada para viabilizar a obtenção de informações interpretáveis sobre a moléculas além de permitir a visualização das sub-estruturas de forma isolada.

Por fim, as bases de dados resultantes para a construção dos modelos continham os ChEMBL IDs, Fingerprints, dicionários bitInfo e labels de cada proteína do Dataset original.


## Análise Exploratória

A fim de se ter uma primeira ideia dos nossos dados, nós começamos por plotar o histograma com o número de vezes que 
cada bit é ativado, como ilustrado na Figura 1. A partir desse gráfico, observamos que determinados bits eram ativados
com maior que frequência que outros. Então, levantamos a pergunta se esses bits mais frequêntes eram de fato importantes
para a ação inibitória de uma proteína, ou se eles apenas codificavam estruturas comuns a diversas moléculas sem ter qualquer
relação com a ação inibitória. 

Para respondermos essa pergunta, nós construímos outro histograma mas plotando separadamente os valores de ativação dos bits 
em moléculas inibidoras e não-inibidoras. Porém, para que pudéssemos comparar as distribuições
entre inibidores e não-inibidores, foi preciso normalizar essas contagens. Portanto, definimos a *ativação média*, que simplesmente
conta as vezes que cada bit foi ativado e divide pelo total de moléculas. Realizamos esse processo separadamente para inibidores
e não-inibidores e plotamos conjuntamente no mesmo histograma representado na Figura 2. Ao analisar o gráfico da Figura 2,
podemos notar que claramente há bits que são ativamdos com maior frequência dentre os inibidores que detre os não-inibidores, e 
vice versa. Portanto, isso nos dá um bom indicativo de que podemos utilizar algoritmos de aprendizado de máquina para aprender
esses padrões e classificar as moléculas como inibidoras e não-inibidoras. 


![Histograma da distribuição da frequência de ativação dos bits.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/hist_activation.png) 

Figura 1: Histograma com o número de vezes que cada bit é ativado.

![Histograma com a ativação média de cada bit.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/hist_mean_activation.png) 

Figura 2: Histograma com a ativação média de cada bit.

A fim de entendermos melhor o funcionamento das Fingerprints e aprofundarmos nossa análise, nós selecionamos diferentes
 moléculas geramos suas Fingerprints e plotamos as subestruturas codificadas por diferentes bits. Nós observamos que os
 de fato bits na mesma posição (índice) em moléculas diferentes codificavam a mesma estrutura. No notebook [Investigating_RDKit_Morgan_FPs](https://github.com/alvarocapelo/datasci4heatlh/blob/main/notebooks/Investigating_RDKit_Morgan_FPs.ipynb)
 há uma descrição mais aprofundada desse estudo.   


Além disso, para termos uma ideia da distribuição das moléculas sobre o espaço de atributos, nós utilizamos o algoritmo
UMAP [17] para reduzir o número de dimensões de 2048 para 2. A Figura 4 mostra essa representação em 2D. Podemos observar que 
há determinados agrupamentos que parecem ser formados majoritariamente por moléculas inibidoras, outros por não-inibidoras, e 
ainda outras regiões onde inibidoras e não-inibidoras estão mais misturadas. Com isso, nós levantamos a seguinte hipótese,
é possível que haja diferentes combinações de subestruturas moleculares que provoquem a ação inibitória de uma proteína?
Para responder essa pergunta, nós realizamos a análise de clusters dessas moléculas, como descrito na Seção "Análise de Clusters".   


![Visualização da distribuição das moléculas sobre o espaço de atributos.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/cluster_initial.png)

Figura 4: Visualização da distribuição das moléculas sobre o espaço de atributos. Em laranja estão representadas as moléculas
inibidoras e em azul as não-inibidoras.

# Análises Realizadas

Geração usando RDKit e estudo de _fingerprints_: visualização de subestruturas e significados dos _bits_
Separado dataset entre treino e teste, usando 20% para teste
- Usados modelos de ensemble de árvore <lista>
- otimização de parâmetros através de busca randomizada otimizando <lista_de_hiperparâmetros> buscando boa performance     com minimização de _overfitting_
- validação cruzada em 5 folds
- Performance avaliada por acurácia dado conjunto de dados relativamente balanceado
- cálculo de Sensibilidade e Especificidade
7 - Interpretação de modelo vencedor usando SHAP:
- escolhidos arbitrariamente 10 bits mais importantes
- buscado em literatura conhecimento sobre moléculas inibidoras para comparação com bits mais importantes
- Utilização de HDSCAN para análises de clusters
- objetivo de encontrar grupos de moléculas com particularidades, mesmo dentro de inibidoras
- Utlização de UMAP para visualizar clusters em 2 dimensões

## Modelagem

Seguindo nossa metodologia, nessa etapa nós objetivamos treinar algoritmos de classificação de modo a posteriormente extrairmos,
por meio da biblioteca SHAP, os bits (atributos) de maior relevância estudá-los em detalhe. Ou seja, esse passo da nossa metodologia
funcionaria como uma etapa de "_Feature Selection_". Então, nós experimentamos algoritmos que não apenas resultassem em boa 
acurácia na classifocação, mas também que possibilitassem a explicabilidade do método de decisão. Dessa forma, nós decidimos
trabalhar com algoritmos baseados em árvores de decisão, em particular os algoritmos 
[Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), 
[Extra Trees](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html?highlight=extra%20trees#sklearn.ensemble.ExtraTreesClassifier), 
[Ada Boost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html?highlight=ada%20boost#sklearn.ensemble.AdaBoostClassifier) e
 [Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html?highlight=gradient%20boosting#sklearn.ensemble.GradientBoostingClassifier), todos disponíveis na biblioteca do Scikit-Learn.
 Avaliamos a performance desses algoritmos, separamos nosso conjunto de dados como sendo 80% para treino e validação e 20% para 
 teste. Ademais, como nossa base tem um volume de dados restrito, utilizamos a abordagem de validação cruzada (5-fold), os resultados são apresentados
 na Tabela 1. Mais detalhes sobre a modelagem podem ser obtidos no notebook [Modelling](https://github.com/alvarocapelo/datasci4heatlh/blob/main/notebooks/Modelling.ipynb).

## Ferramentas
 Para a execução desse projeto, utilizamos a linguagem Python devido à disponibilidade de bibliotecas em seu ecossistema. Em particular, usamos as bibliotecas Scikit-Learn[3], que disponibiliza diversos algoritmos para aprendizagem de máquina, RDKit[4] para a manipulação das informações das moléculas e SHAP(_SHapley Additive exPlantions_) [5], para interpretação dos modelos de aprendizado de máquina, além de outras bibliotecas amplamente utilizadas para a manipulação e visualização de dados (e.g., Matplotlib, Seaborn, Pandas, Numpy).

### Importância de Variáveis e SHAP
O objetivo da biblioteca SHAP é explicar a predição de uma observação a partir do cálculo da contribuição de cada variável independente. Os valores das variáveis independentes de uma observação atuam como participantes em uma coalisão, e os valores de Shapley nos dizem como distribuir de maneira justa um "pagamento" (no caso, o resultado da predição) entre essas variáveis, e baseia-se na teoria de jogos.

A definição de um "pagamento" ou atribuição de importância justa pode ser definida por 4 características:
- Eficiência: a soma da contribuição das variáveis de uma observação deve igualar-se à diferença entre a predição para essa observação e a predição média.
- Simetria: as contribuições de duas variáveis independentes `j` e `k` devem ter o mesmo valor se elas contribuírem igualmente para todas as coalizões possíveis
- Nulidade (_"Dummy"_): uma variável que não modifica a predição, independente da coalização de que participe, deve tar valor Shapley igual a 0.
- Aditividade: Suponha um modelo de Árvores Aleatórias. A predição é uma média da predição feita por diversas árvores de decisão. A Aditividade garante que, dada uma variável dependente, é possível calcular o valor de Shapley em cada árvore individual, calcular o valor médio, e obter um valor Shapley correspondente àquela variável para o modelo completo de Árvores Aleatórias.

Uma das principais vantagens do valor Shapley é ser o único método que satisfaz todas as propriedades acima, axiomas que dão às explicações por ele explicadas fundamentação teórica. Além disso, está apoiado em uma sólida base matemática na teoria de jogos.

Construida em cima desse conceito, a biblioteca SHAP possui pequenas modificações que permitem a interpretações globais serem consistentes com interpretações locais (para cada observação), tendo em vista que valores Shapley individuais são as "unidades formadoras" da interpração global. Por contar com essa consistência e com forte fundamentação teórica, a bilioteca SHAP é uma alternativa muitas vezes preferida a métodos tradicionais de cálculo de importância de variáveis usadas em modelos baseados em árvores, como a simples contagem de quantas vezes uma variável foi utilizada ou a alteração média na impureza promovida por uma variável. É, por isso, escolhida nesse trabalho.

# Resultados e Discussão

Método | Acurácia
----- | -----
Ada Boost | 80.8
Extra Trees | 81.1
Random Forest | 82.3 
Gradient Boosting | 85.4

Tabela 1: Resultados obtidos a partir da validação cruzada (5-fold) dos modelos treinados.

> colocar figura de SHAP importância de features
> colocar figura do slide de bits mais importantes
> textos André

## Análise de Clusters

Nesta etapa do projeto, buscamos descobrir se existe alguma combinação de subestruturas moleculares que aparece com
frequência dentre as moléculas inibidoras e não aparece naquelas não-inibidoras. Desse modo, a clusterização se
apresenta como uma boa abordagem, pois ela nos permite encontrar moléculas que compartilham determinados padrões.

Então, nós tomamos os 10 bits que codificam as subestruturas de maior importância para a classificação, e realizamos a 
clusterização sobre esse embedding utilizando o algoritmo HDBSCAN [16]. Assim, nós garantimos que os padrões encontrados 
durante a clusterização se baseiam nos bits de maior importância para a classificação, além de reduzir a dimensão do 
espaço de features, o que traz ganhos em termos de tempo de processamento. Para podemos visualizarmos os clusters, nós 
também realizamos a redução de 10 para 2 dimensões utilizando o algoritmo UMAP [17]. 

![Visualização dos clusters obtidos.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/clusters.png)

Figura 5:  As imagens ilustram a distribuição das moléculas com base em uma representação de dimensão reduzida para 2 com o algoritmo UMAP.
À esquerda está a distribuição das moléculas sobre o espaço de atributos, ponto em laranja indicam inibidores e 
pontos em azul indicam não-inibidores. À direta está a mesma representação, porém os pontos estão coloridos de acordo com
o resultado da clusterização, onde o cluster de índice -1 indica outliers.

![Visualização dos clusters obtidos.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/table_bits.png)

Tabela 2: Essa tabela mostra a taxa de incidência dos bits mais importantes dentro de cada cluster.

A Figura 5 mostra à esquerda a distribuição das moléculas de acordo com a anotação original se elas são inibidoras ou não. 
Além disso, à direita temos o resultado da clusterização, foram encontrados doze clusters mais um grupo de outliers. 
Destacamos os clusters 2, 3 e 5, pois eles representam grupos de moléculas nos quais há pelo menos 30 vezes mais inibidoras 
do que não-inibidoras. Portanto, esses são bons grupos a serem estudados em maior nível de detalhamento. Analogamente, 
observamos que os clusters 7 e 11 representam com maioria de não-inibidores, porém essa maioria não chega a duas vezes o 
número de não inibidores.

Assim, realizamos uma análise comparativa entre os clusters 2, 3, 5, 7 e 11, onde analisamos a taxa de incidência de cada 
bit em cada clusters. A taxa de incidência é definida como sendo a média de vezes que um dado bit é ativado dentre os 
inibidores dividida pela média de ativação dentre os não-inibidores. Os resultados são apresentados na Tabela 2. 

> imagem bits característicos dos clusters

Podemos observar que o bit 1367 não é ativado nos clusters com mais não-inibidores, enquanto que ele tem uma incidência 
maior ou igual a 1 para os clusters com maioria de inibidores, indicando que esse bit têm importância significativa para 
caracterização de inibidores. Além disso, podemos ver que apenas os bits 1452 e 650 são ativados dentre os clusters 
majoritariamente não-inibidores (clusters 7 e 11), e a incidência é igual a 1, ao passo que eles ou não são ativados dentre 
os inibidores ou também têm incidência 1. Portanto, esses bits não são suficientes para classificar os não-inibidores. 
Analogamente, os bits 1928 e 650 não são suficientes para explicar os inibidores dos clusters 2, 3 e 5. Já os bits 329 e 
1482 são relevantes para a classificação de inibidores dentro do cluster 2, mas não dentro dos clusters 3 e 5. O bit 1482 
parece ser importante para classificar os não-inibidores do cluster 3 e os inibidores do cluster 2. Por fim, o bit 1077 é 
relevante para a classificação de inibidores dentro do cluster 5.


## Descoberta e Validação do Conhecimento
A partir da análise dos clusters, descobrimos que as moléculas inibidoras frequentemente apresentam o seguinte padrão: 
ativam conjuntamente os bits 329, 1482 e 1367; ou ativam os bits 489 e 1367, mas não o 1482; ou ativam apenas o bit 1077. 
Essa regra, apesar simples, pode ser bastante útil para um filtragem manual de moléculas candidatas a inibidoras.

Para validar essa regra de classificação que descobrimos a partir da clusterização, criamos um método em python e o 
executamos sobre o conjunto de teste. Esse método apresentou uma acurácia de 61,9%, sensibilidade e especificidade de 52,5% e 82,7%, 
respectivamente. Portanto, acreditamos que esse método pode ser bastante aplicável na prática, porém para se ter resultados mais 
precisos de classificação de fato serão necessários algoritmos de aprendizado de máquina, tais como os que apresentamos nesse trabalho (vide Seção Modelagem).

# Conclusão

> Destacar as principais conclusões obtidas no desenvolvimento do projeto.
> bits de maior importância encontrados através de método proposto correspondem a estruturas com atividade farmacofóricas conhecidas em literatura: quinazolina
> incluir conclusão do André
> <imagem da quinazolina>
> isso sugere que esse método pode ser usado como processo inicial de busca de regiões farmacologicamente ativas em out    ras interações candidato-enzima
> encontrados subgrupos dentro das moléculas inibidoras com características específicas e distintas entre si
> Destacar os principais desafios enfrentados.
> Principais lições aprendidas.

# Trabalhos Futuros

> analisar outros valores de raio e tamanho de fingerprint de Morgan => valeria a pena codificar subestruturas maiores?
> analisar outros métodos de fingerprint e comparar performance e explicabilidade
> analisar desempenho em conjuntos de dados com mais moléculas => avaliar efeito de desbalanço
> investigar subestruturas em clusters encontrados a fim de entender significado farmacológico

# Referências Bibliográficas
 [1] XIAO, Kelvin, et al.. Cancer Inhibitors (Version 2). kaggle, 14 Jan. 2020. Disponível em: https://www.kaggle.com/xiaotawkaggle/inhibitors. Acesso em: 03 Abr. 2021.

 [2] ChEMBL. Disponível em: https://www.ebi.ac.uk/chembl/. Acesso em: 03 Abr. 2021.

 [3] Scikit-Learn. Disponível em:  https://scikit-learn.org/stable/. Acesso em: 08 Abr. 2021.

 [4] RDKit. Disponível em: https://github.com/rdkit/rdkit. Acesso em: 08 Abr. 2021.

 [5] MOLNAR, Christoph. Interpretable Machine Learning - A Guide for Making Black Box Models Explainable. Disponível em: https://christophm.github.io/interpretable-ml-book/.  2021.

 [6] SAITO, Renata, et al. Fundamentos de oncologia molecular. Editora Atheneu, , 2015.

 [7] SANTOS, M. de O. Estimativa/2020 – Incidência de Câncer no Brasil. Revista Brasileira de Cancerologia, v. 66, n. 1 SE-EDITORIAL. 2020. Disponível em: https://rbc.inca.gov.br/revista/index.php/revista/article/view/927.

 [8] KOLIBABA, K. S.; DRUKER, B. J. Protein tyrosine kinases and cancer. Biochimica et Biophysica Acta - Reviews on Cancer, v. 1333, n. 3, 1997.

 [9] ROSKOSKI, R. The ErbB/HER receptor protein-tyrosine kinases and cancer. Biochemical and Biophysical Research Communications, v. 319, n. 1, p. 1–11, 2004.

 [10] KRAUSE, D. S.; VAN ETTEN, R. A. Tyrosine Kinases as Targets for Cancer Therapy. New England Journal of Medicine, v. 353, n. 2, p. 172–187, 2005.

[11] FAYYAD, U. M., PIATETSKY-SHAPIRO, G., and SMYTH, P., 1996, Knowledge Discovery and Data Mining: Towards a Unifying Framework.,  KDD-96, 1996.

[12] Morgan, H. L. The Generation of a Unique Machine Description for Chemical Structures - A Technique Developed at Chemical Abstracts Service. J. Chem. Doc. 1965, 5: 107-112.

[13] CHEMAXON. Extended Connectivity Fingerprint ECFP. Disponível em: https://docs.chemaxon.com/display/docs/extended-connectivity-fingerprint-ecfp.md#src-1806333-extendedconnectivityfingerprintecfp-introduction. Acesso em: 21 jun. 2021.

[14] RDKIT. Getting Started with the RDKit in Python. Disponível em: https://www.rdkit.org/docs/GettingStartedInPython.html#rogers. Acesso em: 21 jun. 2021.

[15] CHEMBL. Chembl_webresource_client. Disponível em: https://github.com/chembl/chembl_webresource_client. Acesso em: 21 jun. 2021.

[16] HDBSCAN. The hdbscan Clustering Library. Disponível em:  https://hdbscan.readthedocs.io/en/latest/index.html. Acesso em 23 jun. 2021.

[17] UMAP. Uniform Manifold Approximation and Projection for Dimension Reduction. Disponível em:  https://umap-learn.readthedocs.io/en/latest/. Acesso em 23 jun. 2021.
