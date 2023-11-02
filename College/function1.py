'''
def f1(x,y):
    return x+y
def f2(x,y):
    return x-y
def f3(x,y):
    return x*y
def f4(x,y):
    return x/y

a=20
b=10
print(f1(a,b))
print(f2(a,b))
print(f3(a,b))
print(f4(a,b))
'''
'''
def func(name, *fav): # * is used to indicate multiple values
    print(name, "likes to read: ")
    for subject in fav:
        print(subject)
func("Student 1", "Maths", "Android Programming")
func("Student 2", "Data Structures", "Design")
func("Student 3")
'''
sum= lambda x,y: x+y
print ("Sum= ", sum(3,5))

