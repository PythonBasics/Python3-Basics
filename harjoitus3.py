def sayhi(name, age):
    print("HI "+ name + " You are " + age)

sayhi("mike", "30")

def cube(num):
    return num*num*num

print(cube(3))


def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(6,6,66))


numero1 = float(input("Anna eka numero: "))
numero2 = float(input("Anna toka numero: "))
op = input("Anna operaattori: ")

if op == "+":
    print(numero1 + numero2)
elif op == "-":
    print(numero1 - numero2)
elif op == "*":
    print(numero1 * numero2)
elif op == "/":
    print(numero1/numero2)
else:
    print("Virhe")



