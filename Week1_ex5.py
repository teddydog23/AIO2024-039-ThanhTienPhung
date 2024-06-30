def md_nre_single_sample(a, b, c, d):
  md_nre = ((a**(1/c)) - (b**(1/c)))**d
  return md_nre

y = float(input("y = "))
y_hat = float(input("y_hat = "))
n = int(input("n = "))
p = int(input("p = "))
print(f'md_nre_single_sample(y = {y}, y_hat = {y_hat}, n = {n}, p = {p}) = {md_nre_single_sample(y, y_hat, n, p)}')