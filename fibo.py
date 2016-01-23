def fibo(n):
   """
   >>> fibo(0)
   0
   >>> fibo(1)
   1
   >>> fibo(10)
   55
   """
   if n < 2:
      return n
   else:
      return fibo(n-1) + fibo(n-2)

import doctest
doctest.testmod()