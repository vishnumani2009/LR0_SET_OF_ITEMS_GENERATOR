#global array for usage
prod = []
setofitems = []
hike = []
gms = list("SCce")
hi = []
y = []
c = []
jan = []


#used for closure give A=B this gives back A=.B
def appenddot(a):
    j=a.replace("=","=.")
    return j

#finds closure of the item used appenddot
def closure(a):
    temp = []
   # done =0      
    temp.append(a)
    for item in temp:
        j=item[item.index(".")+1]        
        if j != len(item)-1 :
            for k in prod:
                if k[0][0] == j and (appenddot(k)) not in temp:
                        temp.append(appenddot(k))
        else:
            for k in prod:
                if k[0][0] == j and item not in temp:
                    temp.append(item)        
    return (temp)



def swap(new,pos):
    new=list(new)
    temp=new[pos]
    if pos != len(new):
        new[pos]=new[pos+1]
        new[pos+1]=temp
        new1="".join(new)
        return new1
    else:
        return "".join(new)


def goto1(x):
        hh = []
       # print x,len(x)
        pos=x.index(".")
        if pos != len(x)-1:
            jj=list(x)
            kk=swap(jj,pos)
            if kk.index(".") != len(kk)-1:
               jjj=closure(kk)
               return jjj
            else :
                     hh.append(kk)
                  #   print kk
                     return hh
        else:
            return x






#main()
print "Enter number of productions"
n=input();

i=0
print "enter the productions"
while i < n:
    prod.append(raw_input())
    i=i+1;
    

prod.insert(0,"W=.S")
print "augumented grammar"
print prod
print "--------------------------------------"

j=closure("W=.S")
#print j
print len(j)
#print goto1("W=.S")
setofitems.append(j)
print setofitems
#print len(setofitems)
#length=len(j)
print "________________________________________:"



print setofitems
while True:
    if len(setofitems) == 0:
        break;
   # print "setofitems"
    #print setofitems
    jk=setofitems.pop(0)
    kl=jk
    c.append(jk)
    #print jk
    #print len(jk)
    if len(jk)>1:
        for item in jk:
                jl= goto1(item)
                print kl,setofitems
                print jl,"hi"
                if jl not in setofitems and jl!=kl  :
                        setofitems.append(goto1(item))
                       # print setofitems

print setofitems
print c



#error check conditon
for item in c:
    for j in range(len(item)):
        if goto1(item[j]) not in c:
             if item[j].index(".")!=len(item[j])-1:
                 c.append(goto1(item[j]))


print "---------------------------------------------------------------"
print c

print "---------------------------------------------------------------"









'''
sample productions
S=AaAb
S=BbBa
A=$
B=$

S=CC
C=cC
C=d


S=a
S=(A)

S=S+T
S=T
T=F
T=T*F
F=e
F=(S)


S=AA
A=Aa
A=b

S=V+E
E=F
E=E+F
F=V
F=e
F=(E)
V=g

S=AB
A=aA
B=t

S=a
S=(S)


S=ABc
A=aA
A=b
B=bB

S=TT+
T=aT
T=c
T=Ab
A=e

S=TBc
T=aT
B=tA
B=$
A=aa
A=aC
C=e

# a 8 production grammar 
S=TS
S=e
S=gT
T=$
T=AbC
A=aA
A=e
C=v

'''

















##for i in range(len(setofitems)):
##    print i
##    for j in range(len(setofitems[i])):
##        j=goto1(setofitems[i][j])
##        if j not in setofitems:
##            setofitems.append(j)
##print setofitems
##
##
##
##j=setofitems[2:3]
##for item in j:
##    for i in range(len(item)):
##        print item[i]
##        if goto1(item[i]) not in setofitems:
##            print goto1(item[i])
##
##
##















###global array for usage
##prod = []
##setofitems = []
##hike = []
##gms = list("SCce")
##hi = []
##y = []
##c = []
##
##def appenddot(a):
##    j=a.replace("=","=.")
##    return j
##
## 
##def closure(a):
##    temp = []
##    done =0      
##    temp.append(a)
##    for item in temp:
##        j=item[item.index(".")+1]        
##        if j != len(item)-1 :
##            for k in prod:
##                if k[0][0] == j and (appenddot(k)) not in temp:
##                        temp.append(appenddot(k))
##        else:
##            for k in prod:
##                if k[0][0] == j and item not in temp:
##                    temp.append(item)        
##    return (temp)
##
##
##
##def swap(new,pos):
##    new=list(new)
##    temp=new[pos]
##    if pos != len(new):
##        new[pos]=new[pos+1]
##        new[pos+1]=temp
##        new1="".join(new)
##        return new1
##    else:
##        return "".join(new)
##    
##def goto1(x):
##       #S print x,len(x)
##        pos=x.index(".")
##        
##        if pos != len(x)-1:
##            jj=list(x)
##            kk=swap(jj,pos)
##            if kk.index(".") != len(kk)-1:
##               jjj=closure(kk)
##              # print jjj
##               return jjj
##            else :
##                    jkl=list(kk)
##                   # print jkl
##                    kk="".join(jkl)
##                    hi.append(kk)
##                    return hi
##        else:
##            return x
##
###main()
##        
##print "Enter number of productions"
##n=input();
##
##i=0
##print "enter the productions"
##while i < n:
##    prod.append(raw_input())
##    i=i+1;
##    
##
##prod.insert(0,"W=.S")
##print "augumented grammar"
##print prod
##print "--------------------------------------"
##
##j=closure("W=.S")
####print j
####print len(j)
####print goto1("W=.S")
##setofitems.append(j)
##print setofitems
####print len(setofitems)
####length=len(j)
##print "________________________________________:"
##
##print setofitems
##print "________________________________________:"
##
##
##
##while True:
##    if len(setofitems) == 0:
##        break
##    else:
##        jk=setofitems.pop(0)
##        print "jk"
##        print jk
##        for item in jk:
##            print item
##            print goto1(item)
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####
####c.append(setofitems)
####
####while True:
####    if len(setofitems) == 0:
####        break
####
####    else:
####        jk=setofitems.pop(0)
####        print "jk is"
####        print jk
####        print" \n\n"
####        print "c is"
####        print c
####        print "\n"
####        print len(jk)
####        for item in jk:
####            print "item"
####            print item
####            print "\n\n"
####            if item.index(".") != len(item)-1:
####                jl=goto1(item)
####                print "jl is"
####                print jl
####                print "\n\n"
####                if jl not in setofitems:
####                    if jl.index(".") != len(jl)-1:
####                        setofitems.append(jl)
####                    else :
####                        c.append(jl)
####                        print "set is"
####                        print setofitems
####                        print "\n\n"
####
####
####print setofitems
####
####
####print "\n\n\n\n"
####
####
####print c
####
####
####
####
####
####
####
####
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####while True:
####    if len(setofitems) == 0:
####        break
####    else:
####        print "Set"
####        print setofitems
####              
####        jk=setofitems.pop(0)
####        print "jk is"
####        print jk
####        if jk not in c:
####            c.append(jk)
####            for item in jk:
####                if item.index(".") != len(item)-1:
####                    print "item s"
####                    print item
####                
####                    jl=goto1(item)
####                    print "s s"
####                    print setofitems
####                    if jl not in setofitems:
####                        setofitems.append(jl)
####                        c.append(jl)
####                        print jl
####                else:
####                    c.append(item)
####            
####print c
####
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####
######for i in range(len(setofitems)):
######    print i
######    for j in range(len(setofitems[i])):
######        j=goto1(setofitems[i][j])
######        if j not in setofitems:
######            setofitems.append(j)
####print setofitems
####jkl=setofitems
####print "____________----------------------------________________________"
####
####while True:
####    if len(setofitems) == 0:
####        break
####    else:
####        print setofitems
####        jj=setofitems.pop(0)
####        print jj,len(setofitems)
####
####
####        for item in jj:
####            jk=goto1(item)
####            if jk not in jkl:
####                setofitems.append(jk)
####                print jk
####
####
####
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####
####j=setofitems[2:3]
####for item in j:
####    for i in range(len(item)):
####        print item[i]
####        if goto1(item[i]) not in setofitems:
####            print goto1(item[i])
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
###=0
####while i < length:
####    jj=j[i:i+1]
####    for i in range(len(jj)):
####        print len(jj)
####        print "item is"
####        print jj[i]
####        jk=goto1(jj[i])
####        print jk
####        j.append(jk)
####    i=i+1;
####    length=len(j)
####    print "len is"
####    print length
####    
##    
##    
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
####ii=0
####jj=0
####lee=len(setofitems)
####while ii < lee:
####    while jj < len(setofitems[ii]):
####         print setofitems[ii][jj]
####         kk = (goto1(setofitems[ii][jj]))
####         if kk not in setofitems:
####             setofitems.append(kk)
####             print setofitems
####             jj+=1
####    ii+=1
####
####print len(setofitems)
####jjk=setofitems[3:4]
####print goto1(jjk[0][1])
##
##           
