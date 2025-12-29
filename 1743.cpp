#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>

int main(){
    int n;
    std::string def;
    std::cin >> def;
    n = def.length();

    std::map<char, int> count {};

    for (auto c : def){
        if (count.find(c) != count.end()){
            count[c] += 1;
        } else {
            count[c] = 1;
        }
    }

    std::string res {};

    for (int i = 0; i < n; i++){
        bool found = false;

        for (auto & c : count){
            if (c.second == 0) continue;
            if (res.length() != 0 && res.back() == c.first) continue;
            c.second -= 1;
            bool is_valid = true;
            for (auto & d : count){
                if (d.second > std::ceil((n - i - 1) / 2.F)){
                    is_valid = false;
                    break;
                }
            }
            if (is_valid){
                res += c.first;
                found = true;
                break;
            } else {
                c.second += 1;
            }
        }

        if (!found){
            std::cout << -1 << std::endl;
            return 0;
        }
    }

    std::cout << res << std::endl;
    return 0;
}