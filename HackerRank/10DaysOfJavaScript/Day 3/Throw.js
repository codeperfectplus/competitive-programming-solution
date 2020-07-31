function isPositive(a) {
    if (a == 0) {
        throw new Error("Zero Error");
    }
    if (a < 0) {
        throw new Error("Negative Error");
    }
    return 'YES';
}
console.log(isPositive(-10))