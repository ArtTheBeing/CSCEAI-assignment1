# Part 2a: Prolog

my_intersection/3: computes the intersection of two lists
remdups/2: removes duplicates, keeping the last occurrence of each element
factor/2: returns the prime factorization of a number in descending order
my_sqrt/2: computes square root

How to run: swipl -l exercises.pl

?- my_intersection([1,2,3], [2,3,4], X).
?- remdups([1,3,4,2,4,3,6,8,6,5,4,2,3,4,9], X).
?- factor(120, X).
?- my_sqrt(2.0, R).
