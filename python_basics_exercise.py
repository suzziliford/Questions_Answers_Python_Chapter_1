#exercise 1

for i in [1**1, 2**2, 3**3, 4**4, 5**5, 6**6, 7**7, 8**8]:
    if i >=1000:
        break
    print(i)


#exercise 2

for num in range (2, 101):
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


#exercise 3

age = 8

if age < 18:
    print("Kids")
elif age <= 65:
    print("Adults")
elif age >= 65:
    print("Seniors")
else:
    print("Please Enter a Number")