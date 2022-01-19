# Egyptian Fraction

Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if the numerator is 1 and denominator is a positive number.

for example: 1/2 is a unit fraction.

## Approach Used:

Greedy Algorithm:

for a given number of the form n/d, we d > n. first find the greatest possible unit fraction, then recur for the remaining part.