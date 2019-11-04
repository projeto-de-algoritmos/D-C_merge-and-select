import os
import sys
import ast
from copy import copy

class D_C(object):
    def __init__(self):
        self.array = [3, 8, 9, 4, 20, 64, 12, 5]

    def mergeSort(self, array):
        if len(array)>1:
            m = int(len(array)/2)
            lv = array[:m]
            rv = array[m:]

            self.mergeSort(lv)
            self.mergeSort(rv)
            self.merge(array, lv, rv)

    def merge(self, array, lv, rv):
        i = j = k = 0
        while i<len(lv) and j<len(rv):
            if lv[i] <= rv[j]:
                array[k] = lv[i]
                i += 1
            else:
                array[k] = rv[j]
                j += 1
            k += 1

        while i<len(lv):
            array[k] = lv[i]
            i += 1
            k += 1

        while j<len(rv):
            array[k] = rv[j]
            j += 1
            k += 1


if __name__ == "__main__":
    d_c = D_C()
    clear = lambda: os.system('clear')
    while(1):
        clear()
        print("Atual array: " + str(d_c.array))
        print("1 - Inserir novo array")
        print("2 - Ver o array ordenado, usando o merge sort")
        print("3 - Sair")
        option = input("Digite a opção desejada: ")
        if option == '1':
            try:
                print("Exemplo de entrada: [2, 3, 8, 1, 4]")
                array = input("Digite o array desejado: ")
                array = ast.literal_eval(array)
                d_c.array = array
            except ValueError:
                print("\nInvalid input!")
                input("\nClick any key to continue")
        elif option == '2':
            try:
                array = copy(d_c.array)
                d_c.mergeSort(array)
                print("Array ordenado: " + str(array))
                input("\nClick any key to continue")
            except ValueError:
                print("Invalid input!")
        elif option == '3':
            print("Saindo...")
            exit()
        else:
            print("Opção invalida!")
