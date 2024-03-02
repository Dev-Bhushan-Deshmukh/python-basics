x=123
y=12.3
z=False
w=[1,24,5]


li_=[x,y,z,w]
for x in li_:
    print(type(x))


str__='hello'

def rev_string():
    rev_st=""
    x=list(str__)
    print(x)
    rev_arr=x[::-1]
    for i in rev_arr:
        rev_st +=i
   

    print(rev_st)
rev_string()