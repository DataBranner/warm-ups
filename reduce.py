import collections
import operator

def reduce(fn, iterable, initializer=None):
    # Add other functions later.
    functions = {'+': (operator.add, 0), '*': (operator.mul, 1)} 
    if fn not in functions:
        return
    iterable = collections.deque(iterable) # Use deque so we have popleft.
    if initializer:
        running = functions[fn][0](initializer, iterable.popleft())
    else:
        running = functions[fn][1]
    while iterable:
        running = functions[fn][0](running, iterable.popleft())
    return running
