for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print (i* int(bin(2**i-1), 10))
    print(i*int(bin(2**i-1)[2:],10))