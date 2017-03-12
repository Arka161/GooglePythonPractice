import sys
def func(string,booleanfunc):
    result=string*3
    if booleanfunc:
        return result+"!!!!!"
    return result
def main():
    print("Here is the program \n")
    print func("yahoo",True)
    print(sys.argv[0])
if __name__=='__main__':
    main()



