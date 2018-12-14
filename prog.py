import random

def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        m = 3
        k = len(l)/2
        mid = sampleMedianSelect(l, left, right, k, m)
        partition(l, left, right, mid)

    mid = left
    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    return sup

def randomIns(l, m):
    V = []
    I = []
    for i in range(0, m):
        e = random.randint(0, len(l)-1)
        if e not in I:
            V.append(l[e])
            I.append(e)
    return V

def sampleMedianSelect(l, left, right, k, m):
    if len(l) == 0:
        return l
    if len(l) <= m:
        l.sort()
        return l[int(len(l)/2)]
    else:
        V = randomIns(l, m)
        x = sampleMedianSelect(V, 0, len(V), len(V)/2, 3)
        A = []
        B = []
        C = []
        for i in range(0, len(l)-1):
            if l[i] < x:
                A.append(l[i])
            elif l[i] == x:
                B.append(l[i])
            else:
                C.append(l[i])
        if k <= (len(A)-1):
            return sampleMedianSelect(A, left, right, k, m)
        elif k > (len(A)+len(B)-1):
            return sampleMedianSelect(C, left, right, k - len(A) - len(B), m)
        else:
            return l[i]

def quickSelectionSort(l):
    recursiveQuickSelectionSort(l, 0, len(l)-1)

def recursiveQuickSelectionSort(l, left, right):
    if left >= right:
            return
    m = 3
    k = len(l)/2
    pivot = sampleMedianSelect(l, left, right, k, m)
    mid = partition(l, left, right, pivot)
    recursiveQuickSelectionSort(l, left, mid - 1)
    recursiveQuickSelectionSort(l, mid + 1, right)

def reverseSelectionSort(l):
    """
    Utilizzato per testare l'efficienza dell'algoritmo nel caso di una lista ordinata al contrario
    """
    for k in range(len(l) - 1):

        min_pos = k
        for j in range(k + 1, len(l)):
            if l[j] > l[min_pos]:
                min_pos = j

        l[min_pos], l[k] = l[k], l[min_pos]

def generatoze(b):
    """
    Utilizzato per generare una lista di interi tra 0 e 100 in modo random, con b numero di elementi
    """
    l = []
    for i in range(b):
        k = random.randint(0, 100)
        l.append(k)
    return l


if __name__ == '__main__':
    l = generatoze(1000)
    quickSelectionSort(l)
    print(l)
