names = ["Sridhar", "Usha", "Nishkal", "Anvika", "Sridhar", "Robert", "Susan", "Samba", "Usha", "Alex", "Andy"]

for i in range(0, len(names)):
    for j in range(i+1, len(names)):
        if names[i] == names[j]:
           print(names[i])
           break


