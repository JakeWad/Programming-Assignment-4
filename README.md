Lewis University SP23-CPSC-46000-LT1-Programming Languages

Programming-Assignment-4


1. Let’s assume that there are many points in 3-D space.  Each point has its coordinate as (x, y, z).   All x, y, z are floating point value.
 
		Anyway, can you sort these 3-D point by an sorting order string “xyz”?  

		That’s means x coordinate is primary, y is secondary, z is last priority?
	
		The order string can be of any combination of “xyz”, “xzy”, “yxz”, “yzx”, “zxy”, “zyx”

 		Hint: using lambda expression and Python sorted function
		Sample Inputs:
		[(2, 1, 2), (2, 1, 3), (1, 2, 3), (1, 2, 2), (3, 1, 2), (3, 3, 1), (2, 3, 1), (1, 3, 3), (2, 4, 1)]
	
		Sample output:

		Original:           [(2, 1, 2), (2, 1, 3), (1, 2, 3), (1, 2, 2), (3, 1, 2), (3, 3, 1), (2, 3, 1), (1, 3, 3), (2, 4, 1)]

		Sorted by xyz:  [(1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 1, 2), (2, 1, 3), (2, 3, 1), (2, 4, 1), (3, 1, 2), (3, 3, 1)]

		Sorted by zyx:  [(2, 3, 1), (3, 3, 1), (2, 4, 1), (2, 1, 2), (3, 1, 2), (1, 2, 2), (2, 1, 3), (1, 2, 3), (1, 3, 3)]


2. Using inner function, function chain rules, currying, and high order function to design an add function so that the chain function calls can collect the sum at the variable z.
 
	Sample Output :

	>>z = 0

	>>add(1)

	>>print(z)

	1

	>>z = 0

	>>add(1)(2)(3)(4)(5)

	>>print(z)

	15

	>>z = 0

	>>add(2)(4)(6)(8)(10)

	>>print(z)

	30

	>>z = 0

	>>add(3)(1)(5)(2)(7)

	>>print(z)

	18
