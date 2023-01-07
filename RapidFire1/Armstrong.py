#Armstrong
def main():
    try:
        n = int(input(">> Enter the number  : "))
    except Exception as e:
        print("something went wrong")
    else:
        lent = len(str(n))
        sum1 = 0
        temp = n
        while(n >= 1):
            sum1 += (n % 10)**lent
            n /= 10

        print(temp == sum1)


main()
