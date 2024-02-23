O padrão na expressão regular usa grupos nomeados para facilitar a identificação de cada token desejado no texto. Durante uma iteração sobre todos os resultados encontrados pelo `finditer`, a função verifica se o token atual é um "on" para começar a contar, um "off" para parar de contar, ou um número para adicionar ao total somente se estivermos no estado de contagem ativo (`counting = True`). Sempre que um sinal de igual "=" é encontrado e estamos contando, o `total` é impresso.

A variável `total` mantém a soma dos números válidos e é reinicializada no começo da função, e `counting` é um indicador de estado que determina se os números encontrados devem ser somados ao total.

Os dados são lidos de um ficheiro 'input.txt' e passados para a função como texto de entrada. O código assume que os sinais "=" estão rodeados por espaços e, portanto, detecta-os dessa forma.
