#generators are functions that behave like iterators
#gen_range(stop, start=1, step=1):
#    num = start
 #   while num <= stop:
  #      yield num
   #     num += stop

# new 
def gen_fib():
    a,b = 0, 1
    while True:
        a, b = b, a + b
        yield a
