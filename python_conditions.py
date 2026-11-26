import math as m

def tabei(x):
    if (x > 0):
        return m.sqrt(x**3)
    elif (x < 0):
        return (x / 2) + 1
    else:
        return 0

def tabeii(x):
    if (x % 2 == 0):
        return "این عدد زوج می باشد."
    else:
        return "این عدد فرد می باشد."

def tabeiii(x):
    if (x < 0):
        return -1 * (x)
    else:
        return x

print(tabei(64))

print(tabeii(8))
print(tabeii(7))

print(tabeiii(-1))
print(tabeiii(-2))
print(tabeiii(1))
print(tabeiii(2))

a = 1
if (a >= 0):
    print(a)

b = -1
if (b >= 0):
    print(b)
else:
    print("خنثی")

c = 15
if (c > 0):
    print("عدد شما در محور اعداد مثبت ها قرار دارد")
elif (c == 0):
    print("عدد شما خنثی و در مرکز محور اعداد قرار دارد و صفر است")
elif (c < 0):
    print("عدد شما در محور اعداد منفی ها قرار دارد")
else:
    print("خطا در تشخیص")