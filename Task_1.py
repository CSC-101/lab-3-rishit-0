more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step.
print()                           # more=[2,3,4,5]


def square(n:int) -> int:
   return n * n                           # Call 1: n=1, returns 1. Call 2: n=2, returns 4. Call 3: n=3, returns 9. Call 4: n=4, returns 16
squares = [square(x) for x in [1,2,3,4]]   # Squares is a list of the return values for each call of the function
print()


def check(n:int) -> bool:
   return n > 2                             # Call 1: n=0, returns False. Call 2: n=1, returns False. Call 3: n=2, returns False. Call 4: n=3, returns True. Call 5: n=4, returns True
answer = [x for x in range(5) if check(x)]   # answer=[3,4]
print()


def inc(m:int) -> int:
   return m + 1                             # Call 1: m=3, returns 4. Call 2: m=4, returns 5.
def check(n:int) -> bool:
   return n > 2                             # Call 1: n=0, returns False. Call 2: n=1, returns False. Call 3: n=2, returns False. Call 4: n=3, returns True. Call 5: n=4, returns True
answer = [inc(x) for x in range(5) if check(x)]   # answer=[4,5]
print()
