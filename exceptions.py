try:
   age = int(input("age: "))
   income = 20000
   risk = income / age
   print(age)
except ValueError:
   print('invalid')
except ZeroDivisionError:
   print("Age cannot be 0")

