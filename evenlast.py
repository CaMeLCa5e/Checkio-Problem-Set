def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    x = o
    y = array[-1]
    for number in (len(array)):
        if not i % 2:
            number += x
        if len(array) > 0:
            return x*y

#def checkio(array):
#    result = 0
#    for i in range(0, len(array), 2):
#        result += array[i]
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"