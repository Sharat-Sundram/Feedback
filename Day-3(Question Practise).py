#Question Practice


#Que=>6



values=input("Input some comma-seprated numbers:")
list=values.split(",")
tuple=tuple(list)
print(tuple)
print(list)



#Que=>7




filename=input("Input the Filename:")


f_extns=filename.split(".")
print(filename)

print("The extension of the file is:",(f_extns[-1]))


#Que=>8





color_list=["RED","GREEN","WHITE","YELLOW"]
print("%s %s"%(color_list[0],color_list[-1]))



#Que=>9


exam_st_date=(11,12,2014)



print("The examination will start from:%i/%i/%i"%exam_st_date)



#Que=>10


n=int(input("Enter a number:"))

p=n+((n*10)+n)+((((n*10)+n)*10)+n)

print(p)



#Que=>11



print(abs.__doc__)




#Que=>12



import calendar


y=int(input("Input the year:"))
m=int(input("Input the month:"))


print(calendar.month(y,m))


#Que=>13


print("""
a string that you "don't" have to escape
This is a....... multi-line heredoc string -------> example""")



#Que=>14




from datetime import date


f_date=date(2014,7,2)
l_date=date(2014,7,11)

delta= l_date-f_date

print(delta.days)


#Que=>15



r=float(input("Enter the radius:"))
pi=3.1415
volumeS=(4/3)*pi*r**3
print("The volume of sphere is",volumeS)



#Que=>16


def difference(n):
    if n<=17:
        return 17-n
    else:
        return (n-17)*2
    

print(difference(int(input("Enter the no.:"))))
print(difference(14))



























































