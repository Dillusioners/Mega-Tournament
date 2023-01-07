#Perfect
def factors(num):
    factors = []
    for i in range(1,num):
        if(num % i == 0):
            factors.append(i)
    return factors
        
def main():
    try:
        n = int(input(">> Enter the number  : "))
    except Exception as e:
        print("something went wrong")
    else:
       temp = n
       fact = factors(n)
       sum1 = sum(fact)
       
       print(sum1 == temp)


main()
