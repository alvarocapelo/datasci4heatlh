
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
  O câncer pode ser definido como uma síndrome que engloba mais de 200 doenças, em que as células se dividem expressivamente de forma anormal, invadindo outros tecidos. Cada tipo de câncer se atém a sua especificidade quanto à etiologia genética, histológica, celular, e bioquímica, divergindo assim quanto à progressão patológica, diagnóstico, prognóstico e resposta à terapêutica [6]. Este problema de saúde é de notoriedade e preocupação global, sendo uma das quatro principais causas de morte antes dos 70 anos de idade. Mais de 18 milhões de novos casos de câncer emergiram no mundo no ano de 2018, onde mais da metade destes casos evoluiu para óbito. O câncer de pulmão é o mais incidente, com mais de 2 milhões de casos, seguido pelo câncer de mama, cólon e reto, e próstata [7]. 

 É reconhecido que as tirosina quinases estão envolvidas em diversas etapas do desenvolvimento e progressão do câncer, contribuindo de forma ativa para a proliferação celular e metástase, sem estarem correlacionadas com a sua gênese [8]. Tirosina quinases são enzimas que atuam por mecanismos de fosforilação de polipeptídeos através do ATP, e estão diretamente associadas à proliferação, sobrevivência, diferenciação, funcionalidade e motilidade celular [10]. Essas enzimas são classificadas em dois grandes grupos nomeados receptores ou não receptores, sendo que o primeiro citado é um grupo que caracteriza um domínio de ligação transmembrana glicosilado, conectado a um domínio citoplasmático da enzima catalítica tirosina quinase [8].

 O primeiro receptor de proteína tirosina quinase descrito, o Epidermal Growth Factor Receptor (EGFR) é constituído por uma família de quatro membros, sendo eles o ErbB1/HER1, ErbB2/HER2, ErbB3/HER3 e ErbB4/HER4. Diversos tipos de cânceres têm sido associados com o aumento da estimulação e/ou expressão de ErbB1, como os tumores de bexiga, mama, cabeça e pescoço, rim, pulmão de células não pequenas e próstata, pelo qual se ligam com alta afinidade pelas proteínas Epidermal Growth Factor (EGF) e Transforming Growth Factor-α (TGF-α) [9].

 Diversas terapias na tentativa de inibição da ativação de proteínas tirosina quinase têm sido estudadas como terapia tumoral, entre as mais diversas podemos citar a utilização de pequenas moléculas inibidoras do substrato-ligante, bem como do complexo catalítico de tirosina quinase, e ainda mais inovador, a utilização de anticorpos que se ligam tanto em receptores quanto em ligantes [10].

 Portanto, é de extrema relevância a busca por novas moléculas inibidoras, de forma a viabilizar um tratamento efetivo, seguro e compatível com a vida de todos aqueles que padecem desta grande enfermidade chamada câncer. Tendo esse cenário em vista, buscamos explorar, por meio de ferramentas de ciência de dados, potenciais moléculas inibidoras de ErbB1/HER1, suportando o conhecimento que será construído por toda a rede científica global na solução desta problemática.

[Vídeo de Apresentação](https://github.com/alvarocapelo/datasci4heatlh/blob/main/misc/datasci4health_proposta_projeto.mp4)

# Pergunta de Pesquisa
Quais são os principais padrões moleculares associadas ao comportamento inibitório frente à enzima EGFR/ErbB1, relacionada ao câncer?

# Bases de Dados
 Nós utilizaremos a base de dados Cancer Inhibitors[1] disponibilizada na plataforma Kaggle. Essa base contém informações sobre a estrutura de moléculas coletadas  a partir da ChEMBL[2]. Para cada uma dessas moléculas, há uma anotação se ela inibe ou não uma proteína quinase. Há oito proteínas disponíveis, mas apenas a EGFR/ErbB1 será utilizada nesse trabalho.

 Ao analisar a base de dados, é evidente que sua proposta é a identificação de padrões estruturais nas proteínas que justifiquem a inibição ou não inibição das enzimas a partir de um método de codificação chamado Fingerprinting. Este método apresenta diferentes abordagens, entre elas, as abordagens estruturais e as abordagens farmacofóricas (focadas nas funcionalidades da molécula), que se relacionam diretamente à forma que as moléculas são interpretadas pelos algoritmos de Data Mining.


# Metodologia
Foi utilizada a metodologia _Knowledge Discovery in Databases_[11] proposta por Fayyad et al. em 2016. Partindo da base de dados _Cancer Inhibitors_[1] do Kaggle, foram selecionados os dados correspondentes à enzima EGFR/ErbB1 como conjunto de estudo. 

## Preparo do Dataset:
O preparo do Dataset inicia com a lista de proteínas fornecida na base de dados onde as proteínas são identificadas pelos seus respectivos ChEMBL IDs (identificadores na base de dados ChEMBL) e suas respectivas labels (1 para inibidoras e 0 para não inibidoras). Para seguir com a análise computacional proposta, foi necessário que estes dados fossem transformados em dados interpretáveis por algoritmos de aprendizado de máquina, para isso, foi empregado um método de Fingerprinting disponível na biblioteca RDKit[4].

## Geração de Fingerprints:

O método de Fingerprinting utilizado gera Fingerprints conhecidas como Morgan Fingerprints ou Circular Fingerprints, vetores de extensão definida em que cada elemento represeta uma sub-estrutura molecular que compõe a molécula inputada. As sub-estruturas moleculares, por sua vez, são obtidas considerando um raio, quantidade de átomos vizinhos, determinado. Os inputs utilizados para a geração das Fingerprints dets projeto foram foram:

* A representação das moléculas em notação SMILES (Simplified Molecular-Input Line-Entry System), obtida com auxílio da biblioteca chembl_webresource_client [15] que acessa a base do ChEMBL e busca uma molécula a partir de seu ChEMBL ID
* Tamanho do vetor = 2048
* Número de átomos vizinhos = 2

A geração de uma Fingerprint tem como primeiro passo a identificação de cada um dos átomos não-hidrogênio da molécula com um número inteiro, esta identificação tem como base informações locais, contemplando diferentes propriedades atômicas, como, por exemplo, seu número atômico e número de ligações. Posteriormente, os identificadores são atualizados iterativamente de forma que os identificadores iniciais sejam combinados com os átomos vizinhos até o diâmetro determinado inicialmente. A combinação resultante então passa por um método de hashing e os identificadores são listados, este processo de atualização interativa é baseada no Algoritmo de Morgan [12]. Por fim, ocorre a remoção de identificadores repetidos [13]. Neste projeto, a contagem de cada identificador não foi mantida, de forma que a saída seja um vetor de bits esparso. 

Durante a geração da Fingerprint, a biblioteca RDKit permite o armazenamento de um dicionário (bitInfo) onde as chaves são os índices do vetor (Fingerprint) codificados pela molécula e os valores são tuplas com a posição dos átomos e raios que codificaram determinada estrutura [14].

{índice: (posição do átomo, raio do átomo)}
 
Esta informação foi armazenada para viabilizar a obtenção de informações interpretáveis sobre a moléculas além de permitir a visualização das sub-estruturas de forma isolada.

Por fim, as bases de dados resultantes para a construção dos modelos continham os ChEMBL IDs, Fingerprints, dicionários bitInfo e labels de cada proteína do Dataset original.

## Data Mining:

Para _data mining_, exploraremos uma combinação de técnicas de aprendizagem de máquina, análise estatística e visualização.

Usaremos algoritmos baseados em árvore de decisão pelo poder em capturar interações entre variáveis [5]. Esses algoritmos, porém, tendem a ser instáveis, e por isso modelos de ensemble serão avaliados. Faremos a seleção e visualização de um subconjunto de variáveis por meio dos valores de importância (“feature importance”) calculados usando a biblioteca SHAP[5] (SHapley Additive exPlanations). Por fim, algoritmos de agrupamento (clustering) usando a biblioteca Scikit-Learn[3] serão utilizados para visualizar grupos nos compostos inibidores e não inibidores. 

# Ferramentas
 Para a execução desse projeto, utilizaremos a linguagem Python devido à disponibilidade de bibliotecas em seu ecossistema. Em particular, vamos utilizar as bibliotecas Scikit-Learn[3], que disponibiliza diversos algoritmos para aprendizagem de máquina, RDKit[4] para a manipulação das informações das moléculas e SHAP[5](_SHapley Additive exPlantions_), para interpretação dos modelos de aprendizado de máquina, entre outras que julgarmos necessárias durante o desenvolvimento do trabalho.

# Cronograma
 |Atividades  | Abril | Maio | Junho |
 |--|--|--|--|
 |Revisão bibliográfica, entendimento e geração das fingerprints.  | X |  |  |
 |Criação e treino de modelos de classificação binária.  | X | X |  |
 |Investigação e visualização de padrões.  | X | X |  |
 |Consolidação do conhecimento adquirido.  |  | X | X |

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