
def linearSearch(listElement, key):
    for index, val in enumerate(listElement):
        if val == key:
            return index
        else:
            return None
