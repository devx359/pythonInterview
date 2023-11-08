def meth(ll):
    firstlargest = 0
    secondlargest = 0
    for x in ll :
        if x > secondlargest :
            if x > firstlargest :
                firstlargest = x 
            else :
                secondlargest =x


    return secondlargest                



def main():
    ll = [2,4,1,9,4,7,0,1,7,8,21,15,0,1]
    print(meth(ll))

if __name__ == '__main__' :
    main()    