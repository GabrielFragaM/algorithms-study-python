#Breath First Search

grafo = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F', 'G'],
  'D': ['B'],
  'E': ['B'],
  'F': ['C'],
  'G': ['C']
}

queue = [list(grafo.keys())[0]]
visitados = set()

while queue:
    node = queue.pop(0)
    print(f'\n\n----- Removendo o primeiro nó ({node}) da frente da fila => {str(queue)} -------')
    print(f'----- Verificando se o nó ({node}) está em visitados => {str(visitados)} -------')
    if node not in visitados:
        visitados.add(node)
        print(f'----- Adicionando o nó ({node}) em visitado => {str(visitados)} -------')
        for vizinho in grafo[node]:
            print(f'----- Verificando o vizinho ({vizinho}) se está em visitados => {str(visitados)} -------')
            if vizinho not in visitados:
                print(f'----- Adicionando o vizinho ({vizinho}) na fila => {str(queue)} -------')
                queue.append(vizinho)

        print(f'----- Fila atualizado => {str(queue)} -------')
