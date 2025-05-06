import sys
input=sys.stdin.readline

def cantor(n):
    len=3**n
    line=['-']*len

    def delete_mid(a,b):
        length=b-a

        if length<3:
            return
        
        divide=length//3

        for i in range(a+divide,a+(2*divide)):
            length[i]=''




while True:
    line=input()

    line=line.strip() #공백처리

    n=int(line)

    print(cantor(n))