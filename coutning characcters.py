text = input("enter a string to count the elements")
n,l,s=0,0,0


for c in text:
    if c.isdigit():
        n+=1
    elif c.isalpha():
        l+=1
    else:
        s+=1
print(f'digits:{n}')
print(f'alphabets:{l}')
print(f'special character:{s}')

