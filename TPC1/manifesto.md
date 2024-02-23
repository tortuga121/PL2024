a93191;Daniel Barbosa Faria;https://github.com/tortuga121/PL2024.git


Leitura do Arquivo CSV

A primeira parte do código trata da leitura do arquivo CSV.  As linhas do arquivo são lidas e armazenadas na lista lines. O primeiro elemento dessa lista contém os cabeçalhos, que são extraídos e utilizados para criar dicionários correspondentes às linhas de dados. Esses dicionários são, então, adicionados à lista emd.


A função modalidade_ord_aplhabetical utiliza a função sorted do Python para ordenar a lista de dicionários emd com base na chave 'modalidade'. A ordenação é feita de forma alfabética, e a função retorna uma lista contendo as modalidades ordenadas.
Percentagens de Atletas Aptos e Inaptos

A função percent_atletas_aptos_inaptos calcula as percentagens de atletas aptos e inaptos para a prática desportiva. Ela utiliza uma list comprehension para contar o número de atletas aptos (onde 'resultado' é "true") e, em seguida, calcula as percentagens com base no tamanho total da lista emd.
Distribuição de Atletas por Escalão Etário

A função atletas_por_escalao percorre cada linha do conjunto de dados e calcula o escalão etário para cada atleta com base na idade. A distribuição é armazenada em um dicionário dist_p_idade, onde as chaves são os escalões etários e os valores são as contagens de atletas em cada escalão.
