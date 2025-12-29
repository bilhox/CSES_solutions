#include <iostream>
#include <set>
#include <vector>
#include <limits>
#include <algorithm>
 
#define M 1000000000

constexpr long long mod(long long a, long long m) {
    return (a % m + m) % m;
}

void print_list(std::vector<int> & v){
    for (int val : v){
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

void print_list(std::set<int> & v){
    for (int val : v){
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main(){

    // std::ios::sync_with_stdio(false);
    // std::cin.tie(NULL);

    int n;
    long long k;
    std::cin >> n >> k;

    std::set<int> a {};

    for (int i = 1; i <= n; i++) a.emplace(i);

    std::vector<int> result (n);
    long long increment = k % n;
    long long remaining = n;
    
    int start_offset = 0;

    while (remaining > 0){
        int passed = 0;
        std::set<int> removal {};
        auto it = a.begin();
        // std::cout << remaining << " " << increment << " " << start_offset << std::endl;
        // print_list(a);
        // print_list(result);
        int i = 0;
        while (it != a.end()){
            std::advance(it, mod((increment - start_offset), remaining));
            passed += mod((increment - start_offset), remaining) + 1;
            start_offset = 0;

            int j = *it;

            result[n - remaining + removal.size()] = j;
            removal.emplace(j);

            it ++;

            int remaining_after = remaining - passed;
            if (remaining_after < k + 1){
                start_offset = remaining_after;
                break;
            }
            i ++;
        }

        remaining -= removal.size();
        if (remaining != 0) increment = k % remaining;

        for (auto k : removal){
            a.erase(k);
        }
    }

    for (int el : result){
        std::cout << el << " ";
    }

    std::cout << std::endl;
}