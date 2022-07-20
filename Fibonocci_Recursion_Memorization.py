
#def fibonocci(n):
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#       return fibonocci(n-1) + fibonocci(n-2)

#for n in range(1, 50):
#    print(n, ":", fibonocci(n))

# In above way, if we use bigger range, It wont run fast due to recursion calculation. Use the memorization means cache the addition.

fibonocci_cache = {}

def fibonocci(n):
    #If we have cached the value, then return it
    if n in fibonocci_cache:
        return fibonocci_cache[n]

    #Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonocci(n-1) + fibonocci(n-2)

    #Cache the value and return it
    fibonocci_cache[n] = value
    return value

for n in range(1,50):
    print(n, ":", fibonocci(n))


#with out dec