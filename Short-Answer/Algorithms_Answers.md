#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n<sup>3</sup>), since the while loop counts up from 0 to n \* n \* n.  The line inside the loop is a single O(1) operation.

b) This is O(n<sup>2</sup>).  The outer for loop goes from 0 to n, and the inner one goes from 1 to n.  Each of the operations inside the loops are O(1).

c) This recursive function is O(n).  Each recursive call is made with n-1, with a base case of n=0.  This means we would get n+1 calls to the function.

## Exercise II

This can be solved with binary search.  First go to the middle floor of the building, and drop an egg.  If the egg breaks, then we need to consider the lower half of the floors.  If the egg doesn't break, then we would consider the upper half of the floors.  We would then repeat this process until we have found adjacent floors where the egg breaks and doesn't break.  That adjacent floor where it breaks is f.  This solution would use log(n) eggs, meaning it runs in O(log n) time.
