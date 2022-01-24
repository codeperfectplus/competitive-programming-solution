#include <iostream>
#include <cmath>

using namespace std;

int sum_of_primes(int num){
    int sum = 0;
    int half = int(sqrt(num)) +1;
    
    for (int i =2;i < num + 1; i++){
        for (int j=2; j < half; j++){
            if (i % j == 0){
                break;
            }
        cout << i << " ";
        sum += i;
        }
    }
    return sum;
}


int main(){
    int num = 10;
    cout << "\n10001st prime number is " << sum_of_primes(num) << "." << endl;
    return 0;
}