/* 

Topic : 10001st prime
Problem Statement : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
                    we can see that the 6th prime is 13. What is the 10_001st prime number?
*/

function is_prime(num) {
  for (let i = 2; i < Math.sqrt(num) + 1; i++) {
    if (num % i === 0) {
      return false;
    }
  }
    return true;
}

while (true){
    let num = 0;
    let count = 0;
    while (count < 10001){
        num++;
        if (is_prime(num)){
        	count++;
        }
    }
    console.log(`${num} is the ${count}st prime number`);
    break;
}