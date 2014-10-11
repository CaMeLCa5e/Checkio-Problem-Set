#Three Words


            
def checkio(words):
    l = words.split()
    count = 0
    for i in l:
        if i.isalpha():
            count += 1
            if count > 2:
                return True
        else:
            count = 0
    return False
    
#is alpha- Alphabet characters
#