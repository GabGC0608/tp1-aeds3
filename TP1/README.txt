Pesquisa em Lista Encadeada com Medição de Tempo e Comparações

Este projeto implementa uma lista encadeada que permite realizar buscas de chaves, além de medir o tempo de execução e o número de comparações realizadas para cada busca. As chaves podem ser geradas de forma ordenada ou aleatória, e o programa permite buscas por chaves que existem ou não na lista.

1-Pré-requisitos

    python 3.6+: Este script requer uma versão recente do Python.

2-Estrutura do Código

    inserir_lista: Insere novos elementos na lista encadeada.
    buscar_lista: Busca uma chave na lista e mede o tempo e o número de comparações para cada busca.
    gerar_dados: Gera dados aleatórios ou ordenados, de acordo com a opção fornecida.
    criar_arquivo_de_dados: Gera um arquivo de texto com os dados criados.
    main: Função principal para coletar entradas do usuário, configurar os dados, realizar buscas e calcular estatísticas.
    Execução

3- Para executar o código:
    Salve o script em um arquivo como pesquisa_lista.py.

3.1-Execute-o arquivo salvando como busca_sequencial.py, acessando o diretorio em que salvou e digitando:
    python busca_sequencial.py
A seguir, o programa solicitará as seguintes entradas:

    Número de chaves no arquivo: Quantidade de chaves únicas a serem geradas.
    Quantidade de chaves a buscar: Número de buscas que serão realizadas.
    Chaves ordenadas? (S/N): Define se as chaves devem ser geradas de forma ordenada ou aleatória.
    Deseja buscar chaves que existem ou não existem? (E/N): Determina se as buscas serão feitas por chaves que estão na lista (E) ou que não estão (N).

Após a execução de cada conjunto de buscas, o programa exibirá:

    Tempo de pesquisa para cada chave.
    Número de comparações realizadas para encontrar (ou não) cada chave.
    Médias de tempo e de comparações para todas as buscas realizadas.
    O programa também oferece a opção de continuar realizando novos conjuntos de buscas.

Exemplo de Saída

    Número de chaves no arquivo: 100
    Quantidade de chaves a buscar: 10
    Chaves ordenadas? (S/N): n
    Deseja buscar chaves que existem ou não existem? (E/N): e

    Chave: 23, encontrada. Tempo de pesquisa: 0.032417 ms, Comparações: 23
    Chave: 45, não encontrada. Tempo de pesquisa: 0.042113 ms, Comparações: 50
    ...

    Média do tempo para 10 buscas: 0.025631 ms
    Média de comparações para 10 buscas: 25.30
    
    Deseja realizar mais buscas? (S/N): (O programa continuará a execução até que o usuário decida interromper.)