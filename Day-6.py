#INTRODUCTION TO STRING,LIST,TUPLES.
s="sundram"
print(type(s))



y="""jirjfirfjormfofm
jgijgirjgirgmi
yrhurh"""
print(type(y))




print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])


#Reverse of string

print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print(s[-7])



#string slicing


s="This is an intresting pythonworkshop."
print(s[11::1])
print(s[-25::])
print(s[-25::])

#Inbuilt function


x="Sharat"
s="sundram"
print(x+s)

#format specifier
p="GECVaishali"
print("My college name is %s"%p)



s="{} is state college".format("GECVaishali")
print(s)



#LIST




l=["sundram",True,3.1415,False]
print(type(l))

l[3]=True
print(l)


l=["sundram",True,3.1415,False,79,7,8737,938,]


l.append(65)
print(l)

l.insert(5,"python")

print(l)

l.pop(2)#jo hatana h uska index dalo inside paranthesis.
print(l)

l.remove(938)#jo value hataani h wo likna h paranthesis me.
print(l)



#comparision of list


a=[2,3,4,5,6]
b=[2,3,5,4,6]
print(a==b)



#operation on list

l=[2,3,4,5,6,7]
x=l*2
print(x)

print(len(l))

for i in l:
    
    print(i)
    

    print("Maximum in the list is",max(l))
    print("Maximum in the list is",min(l))


#TUPLES(TUPLE HAI TOH PRIVACY HAI)(IMMUTABLE DATA TYPE)


P=(1,2,3,4,5,"list")
print(type(P))
print(P[0])
print(P[-5:])

#SET



s={2,3,4,5,6,7,"TUESDAY",9.85,"wednesday"}
print(type(s))

print(s)
    
#another way of declaring set
#We can only add and update set
#There is no concept of indexing


p=set([1,2,3,"hello"])
print(type (p))

set={1,2,3,4,6,7}
set.add(5)
print(set)




































































