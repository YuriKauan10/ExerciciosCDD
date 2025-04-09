array = ['10','10',9,8,6]

contString = 0
contInt = 0

print(array)

for i in array:
    if isinstance(i, str):
        contString += 1
    elif isinstance(i, int):
        contInt += 1

print(f"Tem {contString} Strings neste array.")
print(f"Tem {contInt} Inteiros neste array.")