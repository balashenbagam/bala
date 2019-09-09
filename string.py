def toString(List):
    return ''.join(List) 
def permute(s, l, r):
    if l==r: 
        print toString(s) 
    else: 
        for i in xrange(l,r+1): 
            s[l], s[i] = s[i], s[l] 
            permute(s, l+1, r) 
            s[l], s[i] = s[i], s[l] 
string = "ABC"
N=len(string) 
s=list(string)
permute(s, 0, N-1) 
