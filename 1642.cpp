#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using t_num_ind = std::pair<long long, int>;

std::vector<int> solve(std::vector<t_num_ind> & a, long long x){

    int n = a.size();

    for (int r = 0; r < n; r++){
        for (int i = r; i < n; i++){
            if (i == r) continue;
            int left = i;
            int right = n - 1;
            while (left < right){
                long long val = a[left].first + a[right].first + a[i].first + a[r].first;
                if (val < x || left == i || left == r){
                    left ++;
                } else if (val > x || right == i || right == r){
                    right --;
                } else {
                    return {a[i].second, a[r].second, a[left].second, a[right].second};
                }
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
        std::cout << result[0] << " " << result[1] << " " << result[2] << " " << result[3] << std::endl;
    } else {
        std::cout << "IMPOSSIBLE" << std::endl;
    }

    return 0;
}