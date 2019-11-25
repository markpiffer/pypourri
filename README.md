# pypourri
A collection of Python code that proved useful over the years

- **permutordered**: Partially ordered permutation

  From a list of elements [a,b,c,1,2] create all permutations where a,b,c,d assume arbitrary positions and 1,2 assume positions so that their (1,2's) relative position is preserved. E.g. [c,1,2,a,b] or [1,a,2,b,c] but *never* [**2,1**,a,b,c]
  
- **kickout_unordered**: Shrink (delete parts of an) array

  When deleting elements from a list in Python, the built-in `del` function usually copies later elements over the deleted element, thus yielding O(k\*n) performance for k non-adjacent deletions: in list [0,1,2,3,4,5] when deleting 1 and 3, copy [2,3,4,5] over [1,2,3,4] and then [4,5] over [3,4]. In the special case where the resulting list doesn't need to be ordered, it is possible to use this O(n) algorithm to overwrite elements 1 and 3 selecetively with 4 and 5. This is an optimization routine where you sacrifice list order for speed.

- **mixin**: Mixing two lists while keeping their relative orders

  From two lists e.g. [1,2,3] and [a,b,c] create all permutations where 1 *never* comes after 2, a *never* after b, etc.: [1,a,2,3,b,c], [1,a,b,2,c,3],...

- **binom_combi**: Generate the binomial coefficient combinations (or just the deltas) in a special order, avoiding big jumps in source set

  'n over k': Generate binomial combinations like itertools.combinations, but in a order where two consecutive combinations will differ for each place in at most one position. I.e. for a 3-combination out of string "abcdef" you get "abc", "abd", "abe" etc. and no position
in the 3-character string will jump more than +/-1 in the source set - you will get "abf", "acf" instead of the lexical sort order "abf", "acd" of itertools.combinations.
