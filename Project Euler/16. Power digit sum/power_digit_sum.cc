/* 

Problem Statement: Power Digit Sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

 */
#include <iostream>
#include <cmath>
#include <string>

int power_digit_sum(int num, int power){
    int sum = 0;
    int multiply = pow(num, power);

    std::string range = std::to_string(multiply);

    for(int i =0; i<range.length(); i++){
        sum += range[i] - '0';
    }
    return sum;
}

int main(){
    int num = 2;
    int power = 15;
    std::cout << power_digit_sum(num, power) << std::endl;
    return 0;
}