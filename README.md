# pypourri
A collection of Python code that proved useful over the years

- Partially ordered permutation

  From a list of elements [a,b,c,1,2] create all permutations where a,b,c,d assume arbitrary positions and 1,2,3 assume positions so that their (1,2's) relative position is preserved. E.g. [c,1,2,a,b] or [1,a,2,b,c] but *never* [**2,1**,a,b,c]
  
- Shrink (delete parts of an) array

  In a list [0,1,2,3,4,5] when deleting 1 and 3, instead of copying [2,3,4,5] over [1,2,3,4] and then [4,5] over [3,4] (or even creating a new list), overwrite elements 1 and 3 selecetively with 4 and 5. This is an optimization routine where you sacrifice list order for speed.

- Mixing two lists while keeping their relative orders

  From two lists e.g. [1,2,3] and [a,b,c] create all permutations where 1 *never* comes after 2, a *never* after b, etc.: [1,a,2,3,b,c], [1,a,b,2,c,3],...
