import os
import sys
import ast
from copy import copy

class D_C(object):
    def __init__(self):
        self.array = [3, 8, 9, 4, 20, 64, 12, 5]

    def mergeSort(self, array):
        if len(array)>1:
            print("Splitting " + str(array))
            m = int(len(array)/2)
            lv = array[:m]
            rv = array[m:]

            self.mergeSort(lv)
            self.mergeSort(rv)
            self.merge(array, lv, rv)
            print("Result " + str(array))

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

    def partition(self, array, l, r):
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    def quickSelect(self, array, k):
        l = 0
        r = len(array) - 1
        print("Partitioning " + str(array))
        split_point = self.partition(array, l, r)
        if split_point == r - k + 1:
            result = array[split_point]
        elif split_point > r - k + 1:
            result = self.quickSelect(array[:split_point], k - (r - split_point + 1))
        else:
            result = self.quickSelect(array[split_point + 1:r + 1], k)
        print("Result " + str(array))
        return result


if __name__ == "__main__":
    d_c = D_C()
    clear = lambda: os.system('clear')
    while(1):
        clear()
        print("Current array: " + str(d_c.array))
        print("1 - Insert a new array")
        print("2 - See the sorted array, using merge sort algorithm")
        print("3 - Find the kth largest element using quickSelect")
        print("4 - Exit")
        option = input("Insert the option value: ")
        if option == '1':
            try:
                print("Input example: [2, 3, 8, 1, 4]")
                array = input("Insert the new array: ")
                array = ast.literal_eval(array)
                d_c.array = array
            except ValueError:
                print("\nInvalid input!")
                input("\nClick any key to continue")
        elif option == '2':
            try:
                array = copy(d_c.array)
                d_c.mergeSort(array)
                print("\nSorted array: " + str(array))
                input("\nClick any key to continue")
            except ValueError:
                print("Invalid input!")
        elif option == '3':
            try:
                value = input("Insert the kth largest wanted: ")
                array = copy(d_c.array)
                result = d_c.quickSelect(array, int(value))
                print("\nThe kth largest element is " + str(result))
                print("The resulted array is " + str(array))
                input("\nClick any key to continue")
            except ValueError:
                print("Invalid input!")
        elif option == '4':
            print("Saindo...")
            exit()
        else:
            print("Opção invalida!")
