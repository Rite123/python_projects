def multiply(num1,num2):
    n1=len(num1)
    n2=len(num2)

    if n1==0 and n2==0:
        return "0"

    result=[0]*(n1+n2)
    i_n1=0
    i_n2=0

    for i in range(n1-1,-1,-1):
        carry=0
        n_1=ord(num1[i]-ord('0'))

        i_n2=0

        for j in range(n2-1,-1,-1):
            n_2=ord(num2[j])-ord('0')

        sum=n_1*n_2+result[i_n1+i_n2]+carry;