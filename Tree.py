class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node:" + str(self.val)


def inserir(root, node):
    if not root:
        root = node
    else:
        if root.val > node.val:  # Se o valor do nó for menor que o pai ele vai para a esquerda
            if root.left is None:
                root.left = node
            else:
                inserir(root.left, node)
        else:
            if root.right is None:  # Se o valor do nó for maior que o pai ele vai para a direita
                root.right = node
            else:
                inserir(root.right, node)


def altura(root):
    if not root:
        return 0
    return 1 + max(altura(root.left), altura(root.right))


def quantidadeNos(root):
    if not root:
        return 0
    return 1 + quantidadeNos(root.left) + quantidadeNos(root.right)


def buscarNosFolhas(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    return buscarNosFolhas(root.left) + buscarNosFolhas(root.right)


def subarvores(root, slist=[]):
    if root is None:
        return []
    if root.left is not None or root.right is not None:
        slist.append(["Raiz: " + str(root.val), str(root.right), str(root.left)])
        subarvores(root.left, slist)
        subarvores(root.right, slist)
    return slist

def grau(root, glist=[]):
    if root is None:
        return []
    if root.left and root.right:
        glist.append({root.val: 2})
    if root.left and root.right is None:
        glist.append({root.val: 1})
    if root.right and root.left is None:
        glist.append({root.val: 1})
    if root.left is None and root.right is None:
        glist.append({root.val: 0})

    grau(root.left)
    grau(root.right)
    return glist


def listarNos(root, nlist=[]):
    if root:
        nlist.append(root.val)
        listarNos(root.left, nlist)
        listarNos(root.right, nlist)
    return nlist


def imprimirAlturaNos(root):
    for index in range(1, altura(root) + 1):
        h = alturaNos(root, index, [])
        if h:
            print("Na altura ", altura(root) - index, " estão: ", h)


def alturaNos(root, h, nodelist=[]):
    if not root:
        return None
    if h == 1:
        nodelist.append(root.val)
    else:
        alturaNos(root.left, h - 1, nodelist)
        alturaNos(root.right, h - 1, nodelist)
    return nodelist


def imprimirNivelNos(root):
    for index in range(1, altura(root) + 1):
        nivel = nivelNos(root, index, [])
        if nivel:
            print("No nível ", index - 1, " estão: ", nivel)


def nivelNos(root, nivel, nodelist=[]):
    if not root:
        return None
    if nivel == 1:
        nodelist.append(root.val)
    else:
        nivelNos(root.left, nivel - 1, nodelist)
        nivelNos(root.right, nivel - 1, nodelist)
    return nodelist


def imprimirProfundidadeNos(root):
    for index in range(1, altura(root) + 1):
        profundidade = profundidadeNos(root, index, [])
        if profundidade:
            print("Na profundidade ", index - 1, " estão: ", profundidade)


def profundidadeNos(root, profundidade, nodelist=[]):
    if not root:
        return None
    if profundidade == 1:
        nodelist.append(root.val)
    else:
        profundidadeNos(root.left, profundidade - 1, nodelist)
        profundidadeNos(root.right, profundidade - 1, nodelist)
    return nodelist



def imprimirArvore(root, nivel=0):
    if root is not None:
        imprimirArvore(root.left, nivel + 1)
        print((' ' * 4 * nivel) + "-> " + str(root.val))
        imprimirArvore(root.right, nivel + 1)


if __name__ == "__main__":
    root = Node(10)
    inserir(root, Node(12))
    inserir(root, Node(13))
    inserir(root, Node(8))
    inserir(root, Node(9))
    inserir(root, Node(11))
    inserir(root, Node(6))
    inserir(root, Node(30))

    print("-" * 30)
    print("--------ÁRVORE BINÁRIA--------")
    print("-" * 30)
    imprimirArvore(root)
    print("-" * 30)
    print("Altura total da Árvore:", altura(root) - 1)
    print("Quantidade de Nós: ", quantidadeNos(root))
    print("Lista de todos os nós: ", listarNos(root))
    print("Nós folhas: ", buscarNosFolhas(root))
    print("Subárvores: ", subarvores(root))
    print("Cada Nó com seu respectivo grau:", grau(root))
    print("-" * 30)
    imprimirNivelNos(root)
    print("-" * 30)
    imprimirAlturaNos(root)
    print("-" * 30)
    imprimirProfundidadeNos(root)






