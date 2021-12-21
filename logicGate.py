'''
I just try using logic gate to build function and try to make something very nice.
'''
def A(x,y): #and
    if x == 1 and y == 1:
        return 1
    else:
        return 0
    
def R(x,y): #or
    if x == 0 and y == 0:
        return 0
    else:
        return 1
    
def N(x): #not
    if x == 1:
        return 0
    else:
        return 1
list = ["T","F"]
print("A B | 1 2 3 4")
print("-------------")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                x1 = N(R(a,R(b,R(c,d))))
                x2 = A(N(R(a,R(b,c))),d)
                x3 = A(N(R(a,R(b,d))),c)
                x4 = N(R(R(a,b),R(N(c),N(d))))
                x5 = A(N(R(a,R(c,d))),b)
                x6 = N(R(R(a,c),R(N(b),N(d))))
                x7 = A(b,A(c,A(N(a),N(d))))
                x8 = A(b,A(c,A(d,N(a))))
                x9 = A(N(R(b,R(c,d))),a)
                x10 = N(R(R(b,c),R(N(a),N(d))))
                x11 = A(a,A(c,A(N(b),N(d))))
                x12 = A(a,A(c,A(d,N(b))))
                x13 = A(a,A(b,A(N(c),N(d))))
                x14 = A(a,A(b,A(d,N(c))))
                x15 = A(a,A(b,A(c,N(d))))
                x16 = A(a,A(b,A(c,d)))
                print(a,b,c,d," ",x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16)
