#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

constexpr long long mod(long long a, long long m) {
    return (a % m + m) % m;
}

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;

    std::cin >> n;

    std::vector<long long> pref (n);

    for (int i = 0; i < n; i++) {
        long long v;
        std::cin >> v;
        if (i != 0)
            pref[i] = mod(pref[i - 1] + v, n);
        else
            pref[i] = mod(v, n);
    }

    std::map<long long, int> subed {};
    subed[0] = 1;
    long long counter = 0;

    for (auto val : pref){
        if (subed.find(mod(val - n, n)) != subed.end()){
            counter += subed[mod(val - n, n)];
        }

        if (subed.find(val) == subed.end()){
            subed[val] = 1;
        } else {
            subed[val] += 1;
        }
    }

    std::cout << counter << std::endl;

    return 0;
}