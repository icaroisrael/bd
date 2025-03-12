def verifica(a, b, c):
    if(a > b):
        if(a > c):
            return a
    elif(b > c):
        return(b)
    else:
        return c
   
print(verifica(4, 5, 6))
