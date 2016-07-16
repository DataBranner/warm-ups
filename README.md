## Warm-ups

Some short warm-up programs attempted in Python 3.

 * `convert_to_binary.py`. Time to write and test: 8:24. Usage: `convert_to_binary(integer, base=2)` (integer bases other than 2 are allowed). Examples (Ipython):

   ```python
   In [1]: import convert_to_binary as C

   In [2]: C.convert(3)
   Out[2]: (3, '11')

   In [3]: C.convert(5)
   Out[3]: (5, '101')

   In [4]: C.convert(8)
   Out[4]: (8, '1000')

   In [5]: C.convert(5, 3)
   Out[5]: (5, '12')

   In [6]: C.convert(39, 19)
   Out[6]: (39, '21')
   ```

 * `reduce.py`. Time to write and test: 9:58. Usage: `reduce(fn, iterable, initializer=None)`. Currently handles only functions `'+'` and `'*'`. Examples (Ipython):

   ```python
   In [1]: import reduce as R

   In [2]: R.reduce('+', [1, 2, 3])
   Out[2]: 6

   In [3]: R.reduce('*', [1, 2, 3])
   Out[3]: 6

   In [4]: R.reduce('*', [1, 2, 3], 2)
   Out[4]: 12

   In [5]: R.reduce('+', [1, 2, 3], 2)
   Out[5]: 8
   ```

[end]
