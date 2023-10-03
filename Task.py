def my_func(fname,lname):
    print(fname + " "+ lname)

my_func("Emil","refsnes")

def my_function(*kids):
    print("The youngest child is "+kids[2])

my_function("Emil","Ref","Linus")


def myFunc(child3,child4,child5):
    print("The youngest child is "+child3)

#my_function(child1 = "Emil",child2 = "Tobais", child = "Linus")


def Func(**kid):
    print("His last name is "+kid["Lname"])

Func(fname="Tobias", Lname = "Refsnes")

def myCountryFunc(country = "Norway"):
    print("I'm from "+country)

myCountryFunc("Sweden")
myCountryFunc("BD")
myCountryFunc("USA")
myCountryFunc("Norway")

print()
def my_Function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
my_Function(fruits)

print()
def myFunctions(x):
    return 5 * x

print(myFunctions(3))
print(myFunctions(2))
print(myFunctions(4))
print(myFunctions(5))

