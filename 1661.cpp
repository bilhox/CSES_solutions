#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    long long x;
    
    std::cin >> n >> x;

    std::vector<long long> pref (n);

    for (int i = 0; i < n; i++) {
        long long v;
        std::cin >> v;
        if (i != 0)
            pref[i] = pref[i - 1] + v;
        else
            pref[i] = v;
    }

    std::map<long long, int> subed {};
    subed[0] = 1;
    long long counter = 0;

    for (auto val : pref){
        if (subed.find(val - x) != subed.end()){
            counter += subed[val - x];
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