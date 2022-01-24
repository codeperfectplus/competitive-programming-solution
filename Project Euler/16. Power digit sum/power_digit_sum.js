/* 

Problem Statement: Power Digit Sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
*/

function power_digit_sum(num, power){
    let sum = 0;
    
    let multiply = BigInt(Math.pow(num, power));

    for(let i=0; i<multiply.toString().length; i++){
        sum += +multiply.toString()[i];
    }
    return sum;
    
}

result = power_digit_sum(2, 1000);
console.log(result);