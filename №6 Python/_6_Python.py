
def delete(): 
    a = list(map(int, input('Enter your numbers: ').split()))
    print("Начальний список: ", a)

    result = []

    for i in range(len(a)): 
        if (i+1) % 2 == 0: 
            result.append(a[i])
    print("Кінцевий список: ", result)
delete()

