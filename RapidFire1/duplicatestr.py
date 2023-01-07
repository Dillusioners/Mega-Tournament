# duplicates the str
def duplicate_chars(string):
    strList = duplicateList = []
    warn = False
    newString = ''
    for i in string:
        strList.append(i)
    
    duplicateList = strList.copy()
    duplicateList.sort()
    
    for i in strList:
        if i in duplicateList and not warn:
            warn = True
        
        if i in duplicateList and  warn:
            return True
            
    return False

def main():
    myStr = input("Enter your string: ")
    print(f"Is String Having Duplicate? {duplicate_chars(myStr)}")

if __name__ == '__main__':
    main()
