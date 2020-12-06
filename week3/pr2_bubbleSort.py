
def bubbleSort(unsorted_list):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                isSorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list
def main():
    print(bubbleSort([4, 6, 8, 3, 2, 5, 7, 8, 9]))
if __name__ == '__main__':
    main()