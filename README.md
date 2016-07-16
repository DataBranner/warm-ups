## Warm-ups

Some short warm-up programs attempted in Python 3.

 * `convert_to_binary.py`. Time to write and test: 8:24. Usage: `convert_to_binary.convert(integer, base=2)` (integer bases other than 2 are allowed). Examples (Ipython):

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

 * `reduce.py`. Time to write and test: 9:58. Usage: `reduce.reduce(fn, iterable, initializer=None)`. Currently handles only functions `'+'` and `'*'`. Examples (Ipython):

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

 * `index_n_grams.py`. Time to write and test core: 7:51; time till output formatting correct: 10:32. Usage: `index_n_grams.index(word_list, n_gram_length=3)`. Examples (Ipython):

   ```python
   In [1]: import index_n_grams as I
   
   In [2]: I.index(['apple', 'happen'])
   {
     app: ['apple', 'happen'],
     hap: ['happen'],
     pen: ['happen'],
     ple: ['apple'],
     ppe: ['happen'],
     ppl: ['apple'],
   }
   
   In [3]: I.index(['apple', 'happen'], 2)
   {
     ap: ['apple', 'happen'],
     en: ['happen'],
     ha: ['happen'],
     le: ['apple'],
     pe: ['happen'],
     pl: ['apple'],
     pp: ['apple', 'happen'],
   }
   ```

[end]
