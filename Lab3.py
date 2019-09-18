def student_info(firstname, lastname, major):
        print("firstname is", firstname)
        print("lastname is", lastname)
        print("major is", major)
student_info("Jonathan", "Mao", "Physics")

def sum(num1, num2):
        print(num1+num2)
        return(num1+num2)
sum(20,27)

def addfunc(x, y):
    return x + y
x = int(input("Enter a first num: "))
y = int(input("Enter a second num: "))
z = addfunc(x, y)
print(x, "+", y, "=", z)

