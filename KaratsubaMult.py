

print("Welcome to Karatsuba Multiplicator")

factor1 = input("Please enter the first factor ")
factor2 = input("Please enter the second factor ")


if len(str(factor1)) or len(str(factor2)) <= 4:
    answer = int(factor1)*int(factor2)
    print("The answer is : " + str(answer))
    
else:

    factor1List = [int(i) for i in factor1]

    AList = factor1List[:len(factor1List)//2]
    A = ''.join(str(i) for i in AList)
    A = int(A)
    BList = factor1List[len(factor1List)//2:]
    B = ''.join(str(i) for i in BList)
    B = int(B)


    factor2List = [int(i) for i in str(factor2)]
    CList = factor2List[:len(factor2List)//2]
    C = ''.join(str(i) for i in CList)
    C = int(C)
    DList = factor2List[len(factor2List)//2:]
    D = ''.join(str(i) for i in DList)
    D = int(D)
    step1 = A*C
    step2 = B*D
    step3 = (A+B)*(C+D)
    step4 = step3 - step2 - step1
    step5 = step1 * 10000 + step2 + step4 * 100
    answer = step5
    print("The answer is : " + answer)
    

