# Depth First Search

grafo = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'F', 'G'],
  'D': ['B'],
  'E': ['B'],
  'F': ['C'],
  'G': ['C']
}

stack = [list(grafo.keys())[0]]  # Usamos uma pilha para DFS
visitados = set()

while stack:
    node = stack.pop()  # Retire o nó do topo da pilha
    print(f'\n\n----- Removendo o nó ({node}) do topo da pilha => {str(stack)} -------')
    print(f'----- Verificando se o nó ({node}) está em visitados => {str(visitados)} -------')
    if node not in visitados:
        visitados.add(node)
        print(f'----- Adicionando o nó ({node}) em visitado => {str(visitados)} -------')
        for vizinho in grafo[node]:
            print(f'----- Verificando o vizinho ({vizinho}) se está em visitados => {str(visitados)} -------')
            if vizinho not in visitados:
                print(f'----- Adicionando o vizinho ({vizinho}) na pilha => {str(stack)} -------')
                stack.append(vizinho)

        print(f'----- Pilha atualizada => {str(stack)} -------')
