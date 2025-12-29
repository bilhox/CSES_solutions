#include <iostream>
#include <vector>
#include <cmath>

bool is_prime(int k, std::vector<int> & primes){
    if (k < 2)
        return false;
    
    for (int p : primes){
        if (k % p == 0) return false;
    }

    return true;
}

int paddic(int v, int p){
    int r = 0;
    while(v % (int) std::pow(p, r) == 0){
        r += 1;
    }

    return r - 1;
}

int count_divisors(int k, std::vector<int> & primes){
    int count = 1;
    int r = (int) std::pow(k, 0.5);

    for (int i = 0; i < primes.size(); i++){
        int vp = paddic(k, primes[i]);
        k /= (int) std::pow(primes[i], vp);
        count *= (vp + 1);

        if (primes[i] > r) break;
        if (k == 1) break;
    }

    if (k != 1) count *= 2;

    return count;
}

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::vector<int> primes {};
    for (int k = 2; k < 1000; k++){
        if (is_prime(k, primes)) primes.push_back(k);
    }

    int n;
    std::cin >> n;

    while(n--){
        int x;
        std::cin >> x;
        std::cout << count_divisors(x, primes) << "\n";
    }

    std::cout << std::endl;

    return 0;
}