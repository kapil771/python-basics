def solution(s):
    length = 0
    n = len(s)
    lps = [0]*n
    i=1
    while(i<n):
        if(s[i]==s[length]):
            length+=1
            lps[i]=length
            i+=1
        else:
            if(length!=0):
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    if(length>0 and (n%(n-length)==0)):
        print(n/(n-length))
    else:
        print('false')

solution('ABCCBAABCCBAABCCBA')