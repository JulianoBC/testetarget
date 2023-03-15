def fibonacci(n):
  a = 0
  b = 1
  c = 0
  while c < n:
    c = a + b
    a = b
    b = c
  if c == n:
    print(n, "pertence a Fibonacci")
  else:
    print(n, "nao pertence a Fibonacci")

n = int(input("Digite um numero: "))
fibonacci(n)