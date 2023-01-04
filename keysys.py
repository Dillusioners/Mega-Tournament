number = int(input("Enter a 13 digit number:- "))

while len(str(number)) != 13:
    number = int(input("Enter a 13 digit number:- "))

numbers = []

for i in str(number):
    numbers.append(i)

odd = []
even = []

for i in range(0 , len(numbers)):
    if i % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])

odd_even = []
even_even = []

for i in range(0 , len(even)):
    if i % 2 == 0:
        even_even.append(even[i])
    else:
        odd_even.append(even[i])

odd_odd = []
even_odd = []

for i in range(0 , len(odd)):
    if i % 2 == 0:
        even_odd.append(odd[i])
    else:
        odd_odd.append(odd[i])

print("Odd:- ", odd)
print("Even:- ", even)
print("odd_odd:- ", odd_odd)
print("even_odd:- ", even_odd)
print("odd_even:- ", odd_even)
print("even_even:- ", even_even)

def join(arr):
    string = ""
    for i in arr:
        string = string + str(i)
    return string

main = join(odd_odd) + join(odd_even) + join(even_odd) + join(even_even)
print("Main", main)

mains = []

for i in str(main):
    mains.append(i)

last_sums = int(mains[10]) + int(mains[11]) + int(mains[12])
main = int(main) - last_sums

print(main)
