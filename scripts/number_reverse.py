def numrev(number):
    reversed_num = int(0)
    num = int(number)

    while num !=0 :
        digit = num % 10
        print('digit ',digit)
        reversed_num = reversed_num * 10 + digit
        num = num // 10 
        print('num ',num)
        print('------reversed_num ',reversed_num )

    return reversed_num   

def main():
    inp = input("Enter a number \n")
    print(numrev(inp))


if __name__ == '__main__' :
    main()



