#include <bits/stdc++.h>

using ll = long long;
using cand_t = std::array<int, 4>;
int X = 970592641;

cand_t solve() {
    int n;
    std::cin >> n;

    std::map<int, std::pair<int, int>> seen {};

    for (int i = 0; i < 2400; i++){
        for (int j = 0; j < 2400; j++){
            int diff = n - i * i - j * j;
            if (seen.find(diff ^ X) != seen.end()){
                auto u = seen[diff ^ X];
                return {u.first, u.second, i, j};
            }
            seen[(i * i + j * j) ^ X] = {i, j};
        }
    }

    return {0, 0, 0, 0};
}

int main() {
    int t;
    std::cin >> t;

    while(t--){
        cand_t u = solve();
        std::cout << u[0] << " " << u[1] << " " << u[2] << " " << u[3] << "\n";
    }
    std::cout << std::endl;
    return 0;
}