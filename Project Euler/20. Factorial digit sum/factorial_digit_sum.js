/* 


Problem Statement: Factorial Digit Sum
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/
function factorial_num(num){
    let rval = 1;
    for (let i = 2; i <= num; i++)
        rval = rval * i;
    return BigInt(rval);
}

function factorial_digit_sum(num){
    factorial = factorial_num(num);
    sum = 0;
    for(let i=0; i<factorial.toString().length; i++){
        sum += +factorial.toString()[i];
    }
    return sum;
}

result = factorial_digit_sum(10);
console.log(result);