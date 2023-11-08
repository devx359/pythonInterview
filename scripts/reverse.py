def reverse(s):
    res = ""
    for x in s :
        res = x + res
        # print(res)
    return res    



def main():
    inp = input("Enter a string \n")
    print(reverse(inp))
    print("#".join(reversed(inp)))
  


if __name__ == "__main__" :
    main()    