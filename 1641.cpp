#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using t_num_ind = std::pair<long long, int>;

std::vector<int> solve(std::vector<t_num_ind> a, long long x){

    int n = a.size();

    for (int i = 0; i < n; i++){
        int left = 0;
        int right = n - 1;
        while (left < right){
            long long val = a[left].first + a[right].first + a[i].first;
            if (val < x || left == i){
                left ++;
            } else if (val > x || right == i){
                right --;
            } else {
                return {a[i].second, a[left].second, a[right].second};
            }
        }
    }

    return {};
}

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    long long x;
    std::cin >> n >> x;

    std::vector<t_num_ind> a (n);

    for (int i = 0; i < n; i++){
        std::cin >> a[i].first;
        a[i].second = i + 1;
    }

    std::sort(a.begin(), a.end(), [](auto a, auto b){
        return a.first < b.first;
    });

    auto result = solve(a, x);
    if (result.size()){
        std::cout << result[0] << " " << result[1] << " " << result[2] << std::endl;
    } else {
        std::cout << "IMPOSSIBLE" << std::endl;
    }

    return 0;
}