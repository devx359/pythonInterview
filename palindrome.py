def palindrome(my_string):
    reversed_str = "" 
    result = False
    for x in my_string :
        reversed_str = x + reversed_str

    if reversed_str == my_string :
        print("its a palindrome")
        result = True
    else :
        print("Not palindrome")    

    return result

def main():
    inp = input("Enter a string to check for palindrome \n")
    print(palindrome(inp))

if __name__ == '__main__' :
    main()    




