# hàm tính giai giai thừa
def factorial(n):
  if n <= 0:
    print("Input must be a positive integer")

  else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

# hàm sin
def sin(x, n):
  result = 0
  for i in range(n):
    A = ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
    result += A

  return result

# hàm cosin
def cos(x, n):
  result = 0
  for i in range(n):
    A = ((-1)**i)*(x**(2*i))/factorial(2*i)
    result += A
    
  return result

# hàm sinh
def sinh(x, n):
  result = 0
  for i in range(n):
    A = (x**(2*i+1))/factorial(2*i+1)
    result += A
    
  return result

# hàm cosh
def cosh(x, n):
  result = 0
  for i in range(n):
    A = (x**(2*i))/factorial(2*i)
    result += A
    
  return result

n = int(input("n = "))
x = float(input("x = "))
ham = input("hàm muốn tính ( sin | cos | sinh | cosh ): ")
if ham == "sin":
  result = sin(x, n)
elif ham == "cos":
  result = cos(x, n)
elif ham == "sinh":
  result = sinh(x, n)
elif ham == "cosh":
  result = cosh(x, n)
else:
  print("không tính được giá trị này")

print(f'{ham}(x = {x}, n = {n}) = {result}')
