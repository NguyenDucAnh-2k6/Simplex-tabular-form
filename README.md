# The problem of planning n types of plants, maximizing profit while being subjected to m constraints maybe cost limit, growing time... This can be modeled using standard Linear Program 
Solve the LP problem with Simplex method under the Tabular form

         max f(x) = C[1]*X[1] + C[2]*X[2] +  . . . + C[n]*X[n]
s.t.
    A[1,1]*X[1] + A[1,2]*X[2] + . . . + A[1,n]*X[n]   <= b[1] <br />
    A[2,1]*X[1] + A[2,2]*X[2] + . . . + A[2,n]*X[n]   <= b[2] <br />
             . . .
    A[m,1]*X[1] + A[m,2]*X[2] + . . . + A[m,n]*X[n]   <= b[m] <br />
domain of variables:   0 <= X[i], for i = 1, 2, ..., n <br />

Input
Line 1: contains 2 positive integer n and m (1 <= n,m <= 1000) <br />
Line 2: contains C[1], C[2], ..., C[n] <br />
Line n+2+i (i = 1,...,m): contains the ith row of the matrix A: A[i,1], A[i,2], . . ., A[i,n] <br />
Line n+m+2: contains b[1], b[2], ..., b[m] <br />

Output <br />
If the given problem does not have any optimal solution, then write UNBOUNDED. Otherwise, line 1 writes n, and line 2 writes X[1], X[2], ..., X[n] (separated by a SPACE character) <br />

Example <br />
Input <br />
2 3 <br />
3 2 <br />
2 1 <br />
1 2 <br />
1 -1 <br />
7 8 2 <br />
Output <br />
2 <br />
2.0 3.0 <br />


Input <br />
5 3 <br />
2 1 -4 6 -2 <br />
1 1 -1 -1 2 <br />
3 2 4 -1 4 <br />
-2 -3 2 1 1 <br />
7 9 3 <br />

Output <br />
UNBOUNDED

