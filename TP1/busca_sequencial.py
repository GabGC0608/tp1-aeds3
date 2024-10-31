import random
import string
import time

# Função para inserir um novo nó na lista encadeada.
def inserir_lista(lista, chave, dado1, dado2):
    lista.append((chave, dado1, dado2))

# Função para buscar uma chave na lista encadeada e retornar o tempo gasto na busca.
def buscar_lista(lista, chave):
    comparacoes = 0  # Contador de comparações
    tempo_inicial = time.perf_counter()  # Usa perf_counter para mais precisão
    for no in lista:
        comparacoes += 1  # Incrementando o contador a cada comparação
        if no[0] == chave:
            tempo_final = time.perf_counter()
            return no, (tempo_final - tempo_inicial) * 1000, comparacoes  # Converte o tempo para milissegundos
    tempo_final = time.perf_counter()
    return None, (tempo_final - tempo_inicial) * 1000, comparacoes  # Converte o tempo para milissegundos

# Função para gerar dados aleatórios com chaves únicas.
def gerar_dados(num_registros, ordenados=False):
    dados = []
    if ordenados:
        chaves = list(range(1, num_registros + 1))  # Gera chaves ordenadas
    else:
        chaves = random.sample(range(1, num_registros * 2), num_registros)  # Gera chaves únicas não ordenadas
    
    for chave in chaves:
        dado1 = random.randint(1, 100)
        dado2 = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        dados.append((chave, dado1, dado2))
    return dados

# Função para criar um arquivo com os dados gerados.
def criar_arquivo_de_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for entrada in dados:
            arquivo.write(f"{entrada[0]} {entrada[1]} {entrada[2]}\n")


def main():
    num_registros = int(input("Número de chaves no arquivo: "))
    num_buscas = int(input("Quantidade de chaves a buscar: "))
    ordenados_opcao = input("Chaves ordenadas? (S/N): ").strip().lower()
    dados_ordenados = ordenados_opcao == 's'
    dados = gerar_dados(num_registros, dados_ordenados)
    criar_arquivo_de_dados(dados, 'dados.txt')
    lista = []
    for entrada in dados:
        inserir_lista(lista, *entrada)

    while True:
        # Resetar as variáveis para cada novo conjunto de buscas
        tempo_total = 0
        comparacoes_total = 0

        opcao_busca = input("Deseja buscar chaves que existem ou não existem? (E/N): ").strip().lower()

        if opcao_busca == 'e':  # Busca por chaves que existem
            chaves_para_buscar = random.sample([entry[0] for entry in dados], num_buscas)
        else:  # Busca por chaves que não existem
            numeros_unicos = set(entry[0] for entry in dados)
            chaves_para_buscar = []
            while len(chaves_para_buscar) < num_buscas:
                chave = random.randint(1, num_registros * 2)
                if chave not in numeros_unicos:
                    chaves_para_buscar.append(chave)

        # Realiza as buscas e acumula os tempos e comparações
        for chave in chaves_para_buscar:
            resultado, tempo, comparacoes = buscar_lista(lista, chave)
            tempo_total += tempo
            comparacoes_total += comparacoes

            if resultado:
                print(f"Chave: {chave}, encontrada. Tempo de pesquisa: {tempo:.6f} ms, Comparações: {comparacoes}")
            else:
                print(f"Chave: {chave}, não encontrada. Tempo de pesquisa: {tempo:.6f} ms, Comparações: {comparacoes}")

        # Cálculo das médias
        tempo_medio = tempo_total / num_buscas
        comparacoes_media = comparacoes_total / num_buscas

        # Exibir as médias
        print(f"\nMédia do tempo para {num_buscas} buscas: {tempo_medio:.6f} ms")
        print(f"Média de comparações para {num_buscas} buscas: {comparacoes_media:.2f}\n")

        # Perguntar se deseja fazer mais um conjunto de buscas
        continuar = input("Deseja realizar mais buscas? (S/N): ").strip().lower()
        if continuar == 'n':
            break

if __name__ == "__main__":
    main()
