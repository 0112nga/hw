import math


def entropy(S):
    H = 0
    for i in S:
        if i != 0:
            H += -i/sum(S)*math.log2(i/sum(S))
    return round(H,2)

def G(S, A):
    if isNotLeaf(A) == False:
        return None
    H = entropy(S)
    average = 0
    for i in range(len(A.child)):
        arr = A.child[i].root.gain_S
        average += entropy(arr) * sum(arr)/sum(S)
        average = round(average,2)
    g = round(H - average, 2)
    return g

def gainS(arr):
    yesCount = 0
    noCount = 0
    S = []
    for i in arr:
        if i == 'yes':
            yesCount = yesCount +1
        elif(i == 'no'):
            noCount = noCount +1

    S.append(yesCount)
    S.append(noCount)

    return S

def isNotLeaf(tree):
    return tree.next

def findRoot(arr):
    root = Tree(None)
    G_arr = [i.S for i in arr]
    max = G_arr[0]
    index = 0
    for i in range(len(G_arr)):
        if G_arr[i] > max:
            max = G_arr[i]
            index = i
    root = arr[index]
    return root

def decisionTree(rootTree, arr):
    deciTree = rootTree
    gainS_root = []
    S_root = []
    index = []
    for i in range(len(rootTree.child)):
        gain_Sroot = rootTree.child[i].root.gain_S
        if entropy(gain_Sroot) != 0:
            gainS_root.append(rootTree.child[i].root.value)
            S_root.append(rootTree.child[i].root.gain_S)
            index.append(i)
    # print(f'S {S_root}')
    # print(f'gainS {gainS_root}')
    arr.remove(rootTree)
    for i in range(len(index)):
        for x in arr:
            if isNotLeaf(x):
                makeChild(gainS_root[i],x)
                x.gain_S = S_root[i]
                x.S = G(x.gain_S , x)
                nextChild = findRoot(arr)
                deciTree.child[index[i]] = nextChild
        if containTree(arr):
            decisionTree(deciTree.child[index[i]],arr)
    return deciTree

def makeChild(gainS_root, tree):
    g = gainS(gainS_root.values())
    tree.gain_S = g
    list1 = set(gainS_root)
    for y in tree.child:
        list2 = set(y.root.value)
        l = {}
        for i in list1.intersection(list2):
            l[i] = y.root.value[i]
        y.root.value = l
        y.root.gain_S = gainS(list(l.values()))

def containTree(arr):
    found = False
    count = 0
    for i in range(len(arr)):
        if isNotLeaf(arr[i]):
            count = count +1
    if count > 1:
        found = True
    return found

def printTree(tree):
    print(tree.root.value,end='')
    print(f' - {tree.S}')
    if isNotLeaf(tree):
        for i in range(len(tree.child)):
            if isNotLeaf(tree.child[i]):
                print('    -- ', end='')
                printTree(tree.child[i])
            else:
                print(f'    -- {tree.child[i].root.value}', end='')
                print(f'-- {tree.child[i].root.gain_S}')

def main():
    # lower case input
    # RED = ['yes','yes','no','no','no']
    RED = { 1: 'yes', 2: 'yes', 3: 'no', 6: 'no', 9:'no'}
    WHITE = {4:'yes',7:'yes', 8:'no'}
    PINK = {5:'yes',10:'yes'}
    # index_RED = [1,2,3,6,9]
    # index_WHITE = [4,7,8]
    # index_PINK = [5,10]

    TRUE_ContainMeat = {1:'yes',6:'yes'}
    FALSE_ContainMeat = {2:'yes',3:'yes',4:'yes',5:'yes',7:'no',8:'no',9:'no',10:'no'}
    # index_TRUE_ContainMeat = [1,6]
    # index_FALSE_ContainMeat = [2,3,4,5,7,8,9,10]

    TRUE_ContainSeafood = {3:'no',4:'no'}
    FALSE_ContainSeafood = {1:'yes', 2:'yes', 5:'yes', 6:'yes', 7:'yes',8:'yes', 9:'no', 10:'no'}
    # index_TRUE_ContainSeafood = [3,4]
    # index_FALSE_ContainSeafood =[1,2,5,6,7,8,9,10]

    arr_sauceColor = []
    LikeR = Tree(RED)
    LikeR.root.gain_S = gainS(list(RED.values()))
    LikeW = Tree(WHITE)
    LikeW.root.gain_S = gainS(list(WHITE.values()))
    LikeP = Tree(PINK)
    LikeP.root.gain_S = gainS(list(PINK.values()))
    arr_sauceColor.append(LikeR)
    arr_sauceColor.append(LikeW)
    arr_sauceColor.append(LikeP)
    sauceColor = Tree('sauceColor')
    sauceColor.child = arr_sauceColor
    sauceColor.gain_S = gainS(list(RED.values()) + list(WHITE.values()) + list(PINK.values()))
    sauceColor.S = G(sauceColor.gain_S, sauceColor)
    sauceColor.next = True
    # printTree(sauceColor)

    arr_containMeat = []
    LikeT_containMeat = Tree(TRUE_ContainMeat)
    LikeT_containMeat.root.gain_S = gainS(list(TRUE_ContainMeat.values()))
    LikeF_containMeat = Tree(FALSE_ContainMeat)
    LikeF_containMeat.root.gain_S= gainS(list(FALSE_ContainMeat.values()))
    arr_containMeat.append(LikeT_containMeat)
    arr_containMeat.append(LikeF_containMeat)
    containMeat = Tree('containMeat')
    containMeat.child = arr_containMeat
    containMeat.gain_S = gainS(list(TRUE_ContainMeat.values())+list(FALSE_ContainMeat.values()))
    containMeat.S = G(containMeat.gain_S, containMeat)
    containMeat.next = True
    # printTree(containMeat)

    arr_containSeafood = []
    LikeT_containSeafood = Tree(TRUE_ContainSeafood)
    LikeT_containSeafood.root.gain_S = gainS(list(TRUE_ContainSeafood.values()))
    LikeF_containSeafood = Tree(FALSE_ContainSeafood)
    LikeF_containSeafood.root.gain_S = gainS(list(FALSE_ContainSeafood.values()))
    arr_containSeafood.append(LikeT_containSeafood)
    arr_containSeafood.append(LikeF_containSeafood)
    containSeafood = Tree('containSeafood')
    containSeafood.child = arr_containSeafood
    containSeafood.gain_S = gainS(list(TRUE_ContainSeafood.values()) + list(FALSE_ContainSeafood.values()))
    containSeafood.S = G(containSeafood.gain_S, containSeafood)
    containSeafood.next = True
    # printTree(containSeafood)


    arr =[]
    arr.append(sauceColor)
    arr.append(containMeat)
    arr.append(containSeafood)

    root = findRoot(arr)
    d = decisionTree(root, arr)
    printTree(d)



class Node:
    def __init__(self, value):
        self.value = value
        self.gain_S = []

class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.child = None
        self.gain_S = []
        self.S = 0
        self.next = None

main()



