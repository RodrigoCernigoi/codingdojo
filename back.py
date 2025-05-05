from flask import Flask, request, jsonify

app = Flask(__name__)
## "Flask" serve como Framkework para criar a API.
## "request" permite acessar os dados enviados na requisição.
## "jsonify" converte dados Python (ex: listas) para JSON de forma segura.

def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)
## Mantém a propriedade de heap: para cada nó i, seus filhos (esquerdo e direito) devem ser menores do que ele.
## "arr": lista que estamos ordenando.
## "n": tamanho da heap (pode mudar durante o processo).
## "i": índice do "nó" atual a ser ajustado.
## Se o filho for maior que o pai, troca. E chama a função recursivamente no filho trocado.

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
## Algoritmo heapsort completo. 
## Passo 1: Construir uma heap máxima (max-heap)
## Começa da metade da lista e vai até o início, garantindo que cada subárvore respeite a regra do heap.
## Passo 2: Ordenar extraindo o maior
## Troca o primeiro (maior) com o último elemento não ordenado e reaplica o heapify para "reorganizar" a heap com o restante.

@app.route('/ordenar', methods=['POST'])
def ordenar():
    data = request.get_json()

## Recebe um JSON como:
    lista = data.get('lista')

## Valida se existe uma chave chamada "lista" e se é uma lista contendo apenas inteiros.
## Se for válido, chama heapsort() para ordenar e retornar.

    if not isinstance(lista, list) or not all(isinstance(x, int) for x in lista):
        return jsonify({'erro': 'Envie uma lista de números inteiros.'}), 400
    return jsonify({'ordenada': heapsort(lista)})

if __name__ == '__main__':
    app.run(debug=True)

## Executa o servidor.
## Se você rodar o arquivo com python app.py, isso inicia o servidor Flask local em http://127.0.0.1:5000.
