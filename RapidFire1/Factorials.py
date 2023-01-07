#Factorials

        
def main():
    try:
        n = int(input(">> Enter the number  : "))
    except Exception as e:
        print("something went wrong")
    else:
        pro = 1
        for i in range(1,n+1):
            pro *= i
    
    print(pro)
       


main()
