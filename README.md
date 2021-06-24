
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

[Vídeo da Apresentação Final](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/video_apresentacao_final.mp4)

# Slides do Projeto

[Slides da Proposta](https://docs.google.com/presentation/d/1N6wFlCN-toHb3z1b7rcldrbp07E3uzAcUefWiG3h62g/edit?usp=sharing)

[Slides da Apresentação Final](https://docs.google.com/presentation/d/115lWvttFJTZqaI5-IkI9Lc72tVtaRpjjB92PujVOdoo/edit?usp=sharing)



# Introdução e Referenciais Teóricos
  O câncer pode ser definido como uma síndrome que engloba mais de 200 doenças, em que as células se dividem expressivamente de forma anormal, invadindo outros tecidos. Cada tipo de câncer se atém a sua especificidade quanto à etiologia genética, histológica, celular, e bioquímica, divergindo assim quanto à progressão patológica, diagnóstico, prognóstico e resposta à terapêutica [6]. Este problema de saúde é de notoriedade e preocupação global, sendo uma das quatro principais causas de morte antes dos 70 anos de idade. Mais de 18 milhões de novos casos de câncer emergiram no mundo no ano de 2018, onde mais da metade destes casos evoluiu para óbito. O câncer de pulmão é o mais incidente, com mais de 2 milhões de casos, seguido pelo câncer de mama, cólon e reto, e próstata [7]. 

 É reconhecido que as tirosina quinases estão envolvidas em diversas etapas do desenvolvimento e progressão do câncer, contribuindo de forma ativa para a proliferação celular e metástase, sem estarem correlacionadas com a sua gênese [8]. Tirosina quinases são enzimas que atuam por mecanismos de fosforilação de polipeptídeos através do ATP, e estão diretamente associadas à proliferação, sobrevivência, diferenciação, funcionalidade e motilidade celular [10]. Essas enzimas são classificadas em dois grandes grupos nomeados receptores ou não receptores, sendo que o primeiro citado é um grupo que caracteriza um domínio de ligação transmembrana glicosilado, conectado a um domínio citoplasmático da enzima catalítica tirosina quinase [8].

 O primeiro receptor de proteína tirosina quinase descrito, o Epidermal Growth Factor Receptor (EGFR) é constituído por uma família de quatro membros, sendo eles o ErbB1/HER1, ErbB2/HER2, ErbB3/HER3 e ErbB4/HER4. Diversos tipos de cânceres têm sido associados com o aumento da estimulação e/ou expressão de ErbB1, como os tumores de bexiga, mama, cabeça e pescoço, rim, pulmão de células não pequenas e próstata, pelo qual se ligam com alta afinidade pelas proteínas Epidermal Growth Factor (EGF) e Transforming Growth Factor-α (TGF-α) [9].

 Diversas terapias na tentativa de inibição da ativação de proteínas tirosina quinase têm sido estudadas como terapia tumoral, entre as mais diversas podemos citar a utilização de pequenas moléculas inibidoras do substrato-ligante, bem como do complexo catalítico de tirosina quinase, e ainda mais inovador, a utilização de anticorpos que se ligam tanto em receptores quanto em ligantes [10].

 Portanto, é de extrema relevância a busca por novas moléculas inibidoras, de forma a viabilizar um tratamento efetivo, seguro e compatível com a vida de todos aqueles que padecem desta grande enfermidade chamada câncer. Tendo esse cenário em vista, exploraramos por meio de ferramentas de ciência de dados, potenciais moléculas inibidoras de ErbB1/HER1.

Nos últimos anos, técnicas de Machine Learning e Deep Learning vêm sendo impulsionadas devido à geração e incorporação de Big Data, com o advento de métodos automatizados para análises biológicas e químicas. Com a junção entre a precisão de métodos computacionais e bases de dados de alta qualidade, abordagens algorítmicas já são aplicadas em diferentes estágios do fluxo de descoberta de novos fármacos [23]. 

A partir disso, o projeto define a enzima EGFR/ErbB1 como alvo para inibição e se propõe a analisar como a ação inibitória de uma molécula está relacionada com as subestruturas que a compõem. Resumidamente, foi necessária a geração de dados interpretáveis por algoritmos de aprendizado de máquina que foram imputados em algoritmos de classificação. Após a classificação, foram determinadas as subestruturas (features) mais relevantes para a classificação entre moléculas inibidoras e não-inibidoras. Por fim, houve a extração do conhecimento a partir da importância de _features_ e da análise de _clusters_ de moléculas formados com base nas features mais relevantes.

Constatou-se que as técnicas computacionais utilizadas indicaram que as subestruturas mais presentes e relevantes em moléculas inibidoras correspondem à estruturas que, segundo a literatura, são capazes de indicar uma provável ação inibitória da molécula. Combinando este resultado com a performance dos classificadores treinados, há indícios de que essa abordagem apresenta potencial para o estudo de proteínas ainda não estudadas, sendo integrada à busca de estruturas moleculares que possam explicar uma ação inibitória.

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

```
{
    índice: [
        (posição do átomo, raio do átomo),
        ...
    ]
}
```
 
Esta informação foi armazenada para viabilizar a obtenção de informações interpretáveis sobre a moléculas além de permitir a visualização das sub-estruturas de forma isolada.

A determinação do tamanho do vetor e quantidade de vizinhos foi baseada na literatura disponível que comumente emprega vetores de 2048 bits e raio (número de átomos vizinhos) igual a 2 [24]. Paralelamente, ensaios exploratórios com a geração de Fingerprints com 4096 bits, resultaram em vetores ainda mais esparsos que aqueles gerados com 2048 bits. Esta constatação indicou que este incremento não resultaria necessariamente na codificação de mais sub-estruturas e, portanto, vetores de 2048 bits seriam suficientes para a análise.

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

Em nossa análise, nós exploramos as _Fingerprints de Morgan_, extraídas utilizando a biblioteca RDKit, de modo a podermos
visualizar as subestruturas das moléculas e interpretar o significado dos bits. Além disso, para evitar um eventual enviesamento
de nossa análise, nós separamos o conjunto de dados em 20% para teste, sendo utilizado apenas ao final de nossas análises,
e os outros 80% para a exploração e treino de algoritmos. 

Nós assumimos que se conseguíssemos encontrar um bom método de classificação, conseguiríamos também extrair os bits (_Features_)
mais importantes, desde que o método utilizado fosse explicável. Ou seja, esse passo da nossa metodologia
funcionaria como uma etapa de "_Feature Selection_". Assim, optamos pelos métodos de Ensemble de Árvores de Decisão,
pois eles se apresentavam como o equilíbrio entre acurácia e explicabilidade. Em particular, escolhemos os algoritmos 
[Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), 
[Extra Trees](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html?highlight=extra%20trees#sklearn.ensemble.ExtraTreesClassifier), 
[Ada Boost](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html?highlight=ada%20boost#sklearn.ensemble.AdaBoostClassifier) e 
[Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html?highlight=gradient%20boosting#sklearn.ensemble.GradientBoostingClassifier), todos disponíveis na biblioteca do Scikit-Learn. 
 
Para se escolher os melhores hiperparâmetros desses modelos, nós conduzimos uma busca aleatório (_Random Search_) dentre 
os principais parâmetros de cada algoritmo. Além disso, como nossa base tem um volume de dados restrito, 
nós avaliamos todos os modelos através abordagem de validação cruzada  em 5 folds. 
Escolhemos a acurácia como principal métrica  de avaliação, uma vez que o conjunto não apresentava um desbalanceio significativo.
Os resultados dos melhores modelos de cada algoritmo são apresentados na Tabela 1. 
Mais detalhes sobre a modelagem podem ser obtidos no notebook [Modelling](https://github.com/alvarocapelo/datasci4heatlh/blob/main/notebooks/Modelling.ipynb).
 
Uma vez treinados os modelos, escolhemos aquele apresentava melhor performance, no caso o modelo de Gradient Boosting, conduzimos a etapa de interpretação, para isso
foi utlizada a biblioteca SHAP.  A partir dessa interpretação, conseguimos selecionar os 10 bits mais importantes para a classificação.
Em seguida, visualizamos as subestruturas codificadas por esses bits, como ilustrados na Figura 6, e verificamos que 
algumas dessas subestruturas se assemelhavam com aquelas que já são conhecidas na Literatura de inibidores da proteína kinase ErbB1.

Com o objetivo de encontrar subgrupos de moléculas inibidoras com características comuns, nós realizamos a clusterização
das moléculas com base naqueles 10 atributos mais importantes mencionados anteriormente. Para a clusterização, foi utilizado 
o algortimo HDSCAN [16]. Em seguida, reduzimos o número de dimensões de 10 para 2 de modo que pudéssemos visualizar o resultado 
da clusterização como apresentado na Figura 5.

Finalmente, a fim de consolidarmos o conhecimento adquirido com análise de cluster, nós criar um classificador _rule-based_
que leva em conta apenas os padrões observados em alguns clusters. Executamos uma análise comparativa entre esse classificador
e o modelo Gradient Boosting sobre o conjunto de teste. Nessa análise, além da acurácia, consideramos as métricas de sensibilidade 
e especificidade, de modo a avaliarmos a performance dos classificadores dentre os inibidores e não-inibidores conjunta e separadamente. 
Observamos que esse classificador baseado no conhecimento adquirido resultou em uma especificidade superior ao do modelo de aprendizado de máquina e acurácia e sensibilidade razoáveis. Desse modo,
o algoritmo consegue classificar corretamente não-inibidores com grande probabilidade de acerto, porém ainda deixa a desejar 
quanto à classificação de inibidores. Portanto, será necessário um estudo mais aprofundado sobre as subestruturas encontradas
de modo a entendermos como elas se combinam para gerar a ação inibitória frente à proteína kinase ErbB1. 

## Ferramentas

**Linguagem de programação**

Para a execução desse projeto, utilizamos a linguagem Python devido à vasta disponibilidade de bibliotecas em seu ecossistema.

**Geração de fingerpints**

RDKit[4] é uma bilioteca com implementação em C++ e com uma interface em Python. Ela foi utilizada neste trabalho para manipular, gerar representaçãoes computacionais (através de _fingerprints_), visualizar e interpretar informações de moléculas.

**Análise Exploratória e Modelagem**

Utlizamos as bibliotecas Matplotlib, Seaborn, Pandas, Numpy e Scipy do ecossitema Python para manipulação e visualização de dados.

Para modelagem, optamos pela biblioteca Scikit-Learn[3], que disponibiliza diversos algoritmos de aprendizagem de máquina em uma interface amigável e estável. Em particular, neste trabalho utilizamos algoritmos de _Boosting_ e _Bagging_ com Árvores de Decisão como estimador-padrão.

A escolha da Árvore de Decisão como algoritmo base no _ensemble_ foi motivada, neste trabalho, principalmente por sua habilidade na captura de interações entre variáveis (_features_) [5].
Sabendo que o conjunto de dados contém exclusivamente presença ou ausência de uma subestrutura (matrix esparsa de 0's e 1's), é razoável supor que uma boa discriminação entre moléculas inibidoras e não-inibidoras seja observada pela interação (combinação de ausência/presença) dos bits que codificam essas subestruturas.
A estratégia de _ensemble_ foi usada para melhora de performance e prevenção contra _overfitting_(problema que afeta muito Árvores de Decisão[5]). Essa estratégia permite extrair o conhecimento usando diversas árvores, seja em paralelo (_bootstrap aggregating_ ou _bagging_) ou em sequência (_boosting_).

**Aprendizado de Máquina interpretável [5]**

Uma das maneiras de se interpretar modelos "caixa-preta" de aprendizado de máquina é através da importância de variáveis (_features_).
O objetivo da biblioteca SHAP é explicar a predição de uma observação a partir do cálculo da contribuição de cada variável independente. Os valores das variáveis independentes de uma observação atuam como participantes em uma coalisão, e os valores de Shapley nos dizem como distribuir de maneira justa um "pagamento" (no caso, o resultado da predição) entre essas variáveis, e baseia-se na teoria de jogos.

A definição de um "pagamento" ou atribuição de importância justa pode ser definida por 4 características:
- Eficiência: a soma da contribuição das variáveis de uma observação deve igualar-se à diferença entre a predição para essa observação e a predição média.
- Simetria: as contribuições de duas variáveis independentes `j` e `k` devem ter o mesmo valor se elas contribuírem igualmente para todas as coalizões possíveis
- Nulidade (_"Dummy"_): uma variável que não modifica a predição, independente da coalização de que participe, deve tar valor Shapley igual a 0.
- Aditividade: Suponha um modelo de Árvores Aleatórias. A predição é uma média da predição feita por diversas árvores de decisão. A Aditividade garante que, dada uma variável dependente, é possível calcular o valor de Shapley em cada árvore individual, calcular o valor médio, e obter um valor Shapley correspondente àquela variável para o modelo completo de Árvores Aleatórias.

Uma das principais vantagens do valor Shapley é ser o único método que satisfaz todas as propriedades acima, axiomas que dão às explicações por ele explicadas fundamentação teórica. Além disso, está apoiado em uma sólida base matemática na teoria de jogos.

Construida em cima desse conceito, a biblioteca SHAP permite uma interpretação global consistente com interpretações locais (para cada observação), uma vez que valores Shapley individuais são as "unidades formadoras" da interpração global. Por contar com essa consistência e com forte fundamentação teórica, a bilioteca SHAP é uma alternativa muitas vezes preferida a métodos tradicionais de cálculo de importância de variáveis usadas em modelos baseados em árvores, como a simples contagem de quantas vezes uma variável foi utilizada ou a alteração média na impureza promovida por uma variável. É, por isso, escolhida nesse trabalho.

# Resultados e Discussão

Na Tabela 1 apresentamos os resultados dos modelos de classificação entre moléculas inibidoras e não-inibidoras. Podemos 
observar que o modelo de _Gradient Boosting_ teve uma performance consideravelmente superior aos outros métodos. Portanto,
acreditamos que o método de _Gradient Boosting_ conseguiu encontrar padrões mais complexos nas subestruturas moleculares
que não foram encontrados por outros métodos. Assim, escolhemo esse modelo para estudarmos a explicação do método de decisão
e extrairmos os atributos mais importantes.

Método | Acurácia
----- | -----
Ada Boost | 80.8
Extra Trees | 81.1
Random Forest | 82.3 
**Gradient Boosting** | **85.4**

Tabela 1: Resultados obtidos a partir da validação cruzada (5-fold) dos modelos treinados.


A Figura 5 apresenta o gráfico de "_Feature Importance_" com os 15 bits mais importantes, ordenados de forma decrescente com relação à importância. Esse gráfico nos permite observar
quais os atributos mais relevantes para a classificação. Podemos notar que de longe os bits 1367 e 
1226 são os mais importantes para a classificação. Além disso, vale destacar que os 2034 bits menos significativos para
a classicação separadamente têm importância muito baixa na média, porém se combinados podem ter uma relevância considerável.
Na Figura 6, nós plotamos as subestruturas codificadas pelos 10 bits mais significativos.

![Explicabilidade da Classificação por meio da contribuição de cada atributo para o SHAP Value.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/feature_importance.png)

Figura 5: Explicabilidade da Classificação por meio da contribuição de cada atributo para o SHAP Value

![Subestruturas codificadas pelos 10 bits mais importantes.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/important_bits.png)

Figura 6: Subestruturas codificadas pelos 10 bits mais importantes.

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

Figura 7:  As imagens ilustram a distribuição das moléculas com base em uma representação de dimensão reduzida para 2 com o algoritmo UMAP.
À esquerda está a distribuição das moléculas sobre o espaço de atributos, ponto em laranja indicam inibidores e 
pontos em azul indicam não-inibidores. À direta está a mesma representação, porém os pontos estão coloridos de acordo com
o resultado da clusterização, onde o cluster de índice -1 indica outliers.

![Visualização dos clusters obtidos.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/table_bits.png)

Tabela 2: Essa tabela mostra a taxa de incidência dos bits mais importantes dentro de cada cluster.

A Figura 7 mostra à esquerda a distribuição das moléculas de acordo com a anotação original se elas são inibidoras ou não. 
Além disso, à direita temos o resultado da clusterização, foram encontrados doze clusters mais um grupo de outliers. 
Destacamos os clusters 2, 3 e 5, pois eles representam grupos de moléculas nos quais há pelo menos 30 vezes mais inibidoras 
do que não-inibidoras. Portanto, esses são bons grupos a serem estudados em maior nível de detalhamento. Analogamente, 
observamos que os clusters 7 e 11 representam com maioria de não-inibidores, porém essa maioria não chega a duas vezes o 
número de não inibidores.

Assim, realizamos uma análise comparativa entre os clusters 2, 3, 5, 7 e 11, onde analisamos a taxa de incidência de cada 
bit em cada cluster. A taxa de incidência é definida como sendo a média de vezes que um dado bit é ativado dentre os 
inibidores dividida pela média de ativação dentre os não-inibidores. Dessa forma, conseguimos analisar frequência relativa
de ativação dos bits dos inibidores em comparação ao não-inibidores. Os resultados são apresentados na Tabela 2. 

Podemos observar que o bit 1367 não é ativado nos clusters com maioria de não-inibidores (clusters 7 e 11), enquanto que ele tem uma incidência 
maior ou igual a 1 para os clusters com maioria de inibidores, indicando que esse bit têm importância significativa para 
caracterização de inibidores, confirmando o resultado do gráfico de _Feature Importance_ da Figura 5. 
Além disso, podemos ver que apenas os bits 1452 e 650 são ativados dentre os clusters 
majoritariamente não-inibidores (clusters 7 e 11), e a incidência é igual a 1, ao passo que eles ou não são ativados dentre 
os inibidores ou também têm incidência 1. Portanto, esses bits não são suficientes para classificar os não-inibidores. 
Analogamente, os bits 1928 e 650 não são suficientes para explicar os inibidores dos clusters 2, 3 e 5. 
 O que representa um resultado razoável, uma vez que as estruturas codificadas pelos bits 1452, 650 e 1928 são bastante simples, como pode ser 
observado na Figura 6. Já os bits 329 e 1482 são relevantes para a classificação de inibidores dentro do cluster 2, mas não dentro dos clusters 3 e 5. O bit 1482 
parece ser importante para classificar os não-inibidores do cluster 3 e os inibidores do cluster 2. Por fim, o bit 1077 é 
relevante para a classificação de inibidores dentro do cluster 5. Na Figura 8 resumimos os bits característicos de cada
cluster. No notebook [Bit_Importances_Analysis](https://github.com/alvarocapelo/datasci4heatlh/blob/main/notebooks/Bit_Importances_Analysis.ipynb)
há mais detalhes sobre essa análise.

![Bits caracteristicos de cada cluster.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/bit_cluster.png)

Figura 8: Bits característicos de cada cluster.

## Descoberta e Validação do Conhecimento
A partir da análise dos clusters, descobrimos que as moléculas inibidoras frequentemente apresentam o seguinte padrão: 
ativam conjuntamente os bits 329, 1482 e 1367 (cluster 2); ou ativam os bits 489 e 1367, mas não o 1482 (cluster 3); ou ativam apenas o bit 1077 (cluster 5). 
Essa regra, apesar simples, pode ser bastante útil para um filtragem manual de moléculas candidatas com potencial ação inibitória.

Para validar essa regra de classificação que descobrimos a partir da clusterização, criamos um método em python e o 
executamos sobre o conjunto de teste. O resultado está apresentado na Tabela 3. 
Podemos notar que esse método baseado no conhecimento adquirido, embora seja bastante simples, apresentou uma especificidade
superior àquela do método Gradient Boosting. Portanto, acreditamos que esse método possa ser bastante aplicável na prática,
principalmente para selecionar moléculas não-inibidoras da proteína kinase ErbB1. Por outro lado, se o objetivo for selecionar
moléculas inibidoras dessa proteína kinase, é mais recomendado usar o modelo de aprendizado de máquina Gradient Boosting. Por fim,
uma análise mais aprofundada será necessária para entendermos melhor o de que forma comportamento conjunto desses bits provoca
a ação inibitória da maior parte das moléculas dos clusters 2, 3 e 5.    


Método | Acurácia | Sensibilidade | Especificidade
----- | ----- | ----- | -----
Cluster Knowledge based |  61.9 | 52.5 | **82.7**
**Gradient Boosting** |  **84.0** | **89.6** | 71.9

Tabela 3: Resultados dos métodos de classificação Gradient Boosting e baseado no conhecimento adquirido (Cluster Knowledge based) com base no conjunto de teste.

## Análise Comparativa com a Literatura

Em estudos de Structure Activity Relationship (SAR) comumente empregado para descoberta de novos fármacos no campo da química medicinal, 
encontramos que o núcleo de quinazolina substituído por uma anilina no carbono 4, corresponde a uma ação inibitória sobre as enzimas de 
tirosina quinase, competindo com o ATP pela ligação do sítio ativo [18-20].

A presença do núcleo de quinazolina substituído no carbono 4 por uma anilina formaria interações de hidrogênio com o 
sítio ativo da enzima, enquanto que a região representada pela letra ‘Y’ na Figura 9 participará de interações hidrofóbicas, 
e a região representada pela letra ‘X’ da mesma figura, constituiria interações polares com o solvente, permitindo maior 
liberdade de modificações moleculares [21].

![Representação gráfica da região farmacofórica de moléculas inibidoras de ErbB. Fonte: Dos autores.](https://github.com/alvarocapelo/datasci4heatlh/blob/main/asset/images/quinazolina.png)

Figura 9: Representação gráfica da região farmacofórica de moléculas inibidoras de ErbB. Fonte: Dos autores [21].

Em concordância com a literatura, verificamos que os três bits de maior importância (1367, 1226, e 1452, respectivamente), 
de acordo com o gráfico da Figura 5, codificam subestruturas moleculares que fazem parte do grupo farmacofórico quinazolina, importante para a inibição das 
enzima ErbB1. Em particular, o bit 1367 (Figura 6) é o responsável por codificar  a subestrutura que mais se aproxima da estrutura 
da quinazolina (Figura 9). Ele também apresenta o maior valor médio de SHAP, inclusive bastante diferente dos demais bits. 
O bit 489 também codifica uma subestrutura associada à quinazolina, de forma que 4 dos 10 bits
mais importantes parecem codificar subestruturas de diferentes tamanhos associadas a essa região farmacofórica.

> Sugestão: substituir a partir de "Analogamente ..." por
>


Em particular, o bit 329, que caracteriza o cluster 2, representa a substituição em ‘Y’ no modelo da figura 17, caracterizando um grupo substituinte de anilina, em que sua presença corrobora para uma interação hidrofóbica, já discutida anteriormente.
Alguns dos bits que contribuem com alguma importância para a distinção entre moléculas inibidoras e não-inibidoras não foram avaliados em profundidade neste trabalho, e.g., bits 1077, 366, 650, 1482 e 1928. Um estudo mais detalhado desses bits fica para escopo de trabalhos futuros.

Vale destacar os exemplos de moléculas, anotadas como não-inibidoras no dataset, pertencentes aos clusters 2, 3 e 5 que 
apresentam estrutura semelhante a moléculas estudadas por Li S. et. al. [22] e conhecidas em literatura por possuírem 
atividade inibitória frente à ErbB. Em particular, possuem núcleos modificados de pirimidina e quinazolina. Portanto, 
essas moléculas estão anotadas de maneira incorreta de acordo com a Literatura. Assim, essa dissonância deve ser melhor 
avaliada em estudos futuros.

# Conclusão

Neste trabalho, fomos capazes de identificar os principais padrões moleculares para a predição de propriedade inbitória de pequenas moléculas sobre a enzima-alvo EGFR/ErbB1, associada ao câncer, combinando técnicas de representação de moléculas computacionalmente e aplicação e interpretação de modelos de aprendizado de máquina.
Especificamente, verificamos que as subestruturas de maior importância eram bastante semelhantes à quinazolina, uma região farmacofórica considerada de importante contribuição para a inibição da ErbB1 em literatura especializada do domínio farmacêutico.

Para além disso, utilizamos algumas das subsestruturas de maior importância calculada para realizar uma análise de _clusters_ com o intuito de verificar se, mesmo dentro das moléculas inibidoras, haveriam grupos com características específicas. Verificamos que pelo menos 3 grupos, dentro do conjunto estudado, apresentaram esse comportamento e sugerimos quais seriam as subestruturas que caracterizariam esses _clusters_.
 
Observamos um bom compromisso entre performance e interpretação, tendo em vista a acurácia de 84.0% de acurária em conjunto de teste e o relatado no primeiro parágrafo desta seção. Isso sugere que a abordagem utilizada neste trabalho apresenta potencial para o estudo de interação moléculas candidatas-proteínas tanto em cenários já estudados, sugerindo novo conhecimento, quanto na procura regiões farmacofóricas em cenários ainda não estudados.

# Trabalhos Futuros

> Investigar outros valores de raio e maior número de bits no vetor de _fingerprints_

Como é possível observar, as subestruturas codificadas nesse trabalho são relativamente "curtas" se comparadas à principal região farmacofórica observada em literatura com atividade inibitória sobre a enzima-alvo (quinazolina, anel aromático + anel de pirimidina + anilina). Assim, maiores valores de raio e mais bits significariam, respectivamente, capacidade de codificar subestruturas maiores e mais "espaço" representá-las na forma de vetores. É possível supor que, assim, subestruturas ainda mais parecidas com regiões farmacofóricas "completas" estariam codificadas nas _fingerprints_.

> Analisar desempenho em conjuntos de dados com mais moléculas

Nesse trabalho, as moléculas selecionadas para a geração de _fingerprints_ e formação dos conjuntos de treino e teste vieram diretamente de uma base de dados do Kaggle.
Na documentação do conjunto de dados, não há clara menção do porquê essas moléculas em particular foram selecionadas, mas é razoável supor que uma pré-seleção tenha sido realizada.
Observando que um valor muito maior de pequenas moléculas está disponível em bases como o ChEMBL, seria interessante investigar conjuntos de dados com ainda mais moléculas e com distribuições diferentes (e potencialmente extremamente desbalanceadas).
Dessa maneira, seria possível verificar se a performance e a eficácia aqui apresentadas seriam mantidas ou prejudicadas. No caso de serem prejudicadas, isso poderia evidenciar algum viés introduzido na base de dados do Kaggle, e a abordagem aqui sugerida teria que ser adaptada.

> Investigar em maior profundidade subestruturas específicas aos _clusters_ encontrados


Pode-se investigar mais _bits_ além dos 10 principais e buscar em literatura, e com apoio de especialistas de domínio, mais informações acerca da contribuição das subestruturas aqui apontadas. Adicionalmente, verificar se essas subestruturas fazem sentido do ponto de vista farmacológico ou não, de forma a ajudar a refinar o método de extração de conhecimento aqui proposto. Esse tipo de trabalho possui forte intersecção com a proposta de investigação de outros valores para os paâmetros de raio e número de bits no vetor de _fingerprints_, proposto anteriormente.

> Avaliar outros métodos de _fingerprinting_

A fingerprint de Morgan (circular) foi escolhida como forma de representar as moléculas neste trabalho por ser simples e por permitir uma interpretação bastante intuitiva, e, ainda assim, ter potencial para boa performance na aplicação de aprendizado de máquina para classificação.
No entanto, há outros métodos de geração de _fingerprints_ para codificar características moleculares importantes.
A título de exemplo, são alguns deles: Fingerprints Farmacofóricas, Pares Atômicos e Fingerprints Torsionais. Valeria a pena estudar como esses métodos se comparam ao método de Morgan quanto ao _trade-off_ entre performance e explicabilidade.

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

[18]	Zhao F, Lin Z, Wang F, Zhao W, Dong X. Four-membered heterocycles-containing 4-anilino-quinazoline derivatives as epidermal growth factor receptor (EGFR) kinase inhibitors. Bioorg Med Chem Lett. 2013 Oct 1;23(19):5385-8. doi: 10.1016/j.bmcl.2013.07.049. Epub 2013 Jul 31. PMID: 23973168. 

[19]	Barker AJ, Gibson KH, Grundy W, Godfrey AA, Barlow JJ, Healy MP, Woodburn JR, Ashton SE, Curry BJ, Scarlett L, Henthorn L, Richards L. Studies leading to the identification of ZD1839 (IRESSA): an orally active, selective epidermal growth factor receptor tyrosine kinase inhibitor targeted to the treatment of cancer. Bioorg Med Chem Lett. 2001 Jul 23;11(14):1911-4. doi: 10.1016/s0960-894x(01)00344-4. PMID: 11459659.

[20]	Zhang YM, Cockerill S, Guntrip SB, et al. Synthesis and SAR of potent EGFR/erbB2 dual inhibitors. Bioorganic & Medicinal Chemistry Letters. 2004 Jan;14(1):111-114. DOI: 10.1016/j.bmcl.2003.10.010.

[21]	Yun CH, Boggon TJ, Li Y, Woo MS, Greulich H, Meyerson M, Eck MJ. Structures of lung cancer-derived EGFR mutants and inhibitor complexes: mechanism of activation and insights into differential inhibitor sensitivity. Cancer Cell. 2007 Mar;11(3):217-27. doi: 10.1016/j.ccr.2006.12.017. PMID: 17349580; PMCID: PMC1939942.

[22]	Li S, Guo C, Zhao H, Tang Y, Lan M. Synthesis and biological evaluation of 4-[3-chloro-4-(3-fluorobenzyloxy)anilino]-6-(3-substituted-phenoxy)pyrimidines as dual EGFR/ErbB-2 kinase inhibitors. Bioorganic & Medicinal Chemistry. 2012 Jan;20(2):877-885. DOI: 10.1016/j.bmc.2011.11.056.

[23] PATEL, Lauv et al. Machine Learning Methods in Drug Discovery. 2020. Disponível em: https://www.mdpi.com/1420-3049/25/22/5277. Acesso em: 23 jun. 2021.

[24] YOSHIMORI, Atsushi et al. Discovery of Novel eEF2K Inhibitors Using HTS Fingerprint Generated from Predicted Profiling of Compound-Protein Interactions. 2021. Disponível em: https://www.mdpi.com/2305-6320/8/5/23/htm. Acesso em: 24 jun. 2021.
