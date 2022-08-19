# 피보나치 / 재귀

def fib(n):
  if n <=1:
    return n
  return fib(n-1) + fib(n-2)

print(fib(8))