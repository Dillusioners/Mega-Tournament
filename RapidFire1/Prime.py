#Prime
       
def main():
    try:
        n = int(input(">> Enter the number  : "))
    except Exception as e:
        print("something went wrong")
    else:
        cnt = 0
        for i in range(2,n):
            if(n % i == 0):
                cnt += 1
        
    print(cnt == 0)


main()
