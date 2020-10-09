a = 100000
while a <= 999999:
    counter = 0
    n1 = a
    n2 = a + 1
    n3 = a + 2
    n4 = a + 3
    if n1 % 10 == n1 // 10000 % 10 and n1 // 1000 % 10 == n1 // 10 % 10:
        counter += 1
    if n2 % 10 == n2 // 10000 % 10 and n2 // 1000 % 10 == n2 // 10 % 10:
        counter += 1
    if n3 // 10000 % 10 == n3 // 10 % 10 and n3 // 1000 % 10 == n3 // 100 % 10:
        counter += 1
    if n4 // 10000 % 10 == n4 // 10 % 10 and n4 // 1000 % 10 == n4 // 100 % 10 and n4 // 100000 == n4 % 10:
        counter += 1
    if counter == 4:
        print(a)
    a += 1


