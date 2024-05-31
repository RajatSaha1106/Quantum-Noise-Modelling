def num_picker(string):
    l = len(string)
    counter = 0
    curr = 0
    while curr < l:
        curr = 2**counter
        counter += 1
    return counter - 1
