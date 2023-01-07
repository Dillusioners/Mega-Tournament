#ReversedString

       
def main():
    try:
        n = (input(">> Enter the string  : "))
    except Exception as e:
        print("something went wrong")
    else:
        num = str(n)
        new_num =list(reversed(num))

    for i in range(len(new_num)):
        print(new_num[i],end="")


main()
