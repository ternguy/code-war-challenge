Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.




def unique_in_order(iterable):
    char = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i -1]:
            char.append(iterable[i])
    return char
