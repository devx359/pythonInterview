def largest(target_list):
    max = 0
    for x in target_list :
        if x > max :
            max = x

    return max  

def main():
    ll = [2,5,1,8,4,0,5,7,3,9,1,2]
    print("largest number is ",largest(ll))



if __name__ =='__main__' :
    main()

      