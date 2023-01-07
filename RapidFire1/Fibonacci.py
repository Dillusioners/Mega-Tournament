#FIbonacci
def main():
    try:
        n = int(input(">> Enter the number of terms you want : "))
    except Exception as e:
        print("something went wrong")
    else:
        a = 0
        b = 1
        print(a +"\n" + b)
        for i in range(n-1):
            c = a + b
            print(c)
            a = b
            b = c

main()
