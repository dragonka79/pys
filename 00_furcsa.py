# for j in range (1,101):
#    if j % 3 :
#        print("Wizz")
#    else:
#        print(j)

# itt if-eket írtam elif helyett és belelép a ciklusba ha j eléri a 101-et
j = 1
while j <= 100 :
    if j % 10 == 0:
        print("fizzbuzz")
        j += 1
    if j % 2 == 0:
        print("fizz")
        j += 1
    if j % 5 == 0:
        print("buzz")
        j += 1
    else:
        print(j)
        j +=1




j = 1
while j <= 100 :
    if j % 10 == 0:
        print("fizzbuzz")
        j += 1
    elif j % 2 == 0:
        print("fizz")
        j += 1
    elif j % 5 == 0:
        print("buzz")
        j += 1
    else :
        print(j)
        j +=1
