#ReversedNumber

       
def main():
    try:
        n = int(input(">> Enter the number  : "))
    except Exception as e:
        print("something went wrong")
    else:
        num = str(n)
        new_num =list(reversed(num))

    for i in range(len(new_num)):
        print(new_num[i],end="")


main()
