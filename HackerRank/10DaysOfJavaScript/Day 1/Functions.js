/*
 * Create the function factorial here
 * Recursion : To call itself is called recursion.
 */
function factorial(n) {
    if (n === 0) {
        return 1;
    }
    return n * factorial(n - 1);
}
