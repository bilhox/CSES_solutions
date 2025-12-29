#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, x;
    std::cin >> n >> x;

    std::vector<int> coins(n);
    std::vector<int> dp(x + 1, x + 2);

    for (int i = 0; i < n; i++) std::cin >> coins[i];

    std::sort(coins.begin(), coins.end());
    dp[0] = 0;

    for (int i = 1; i < x + 1; i++){
        for (int coin : coins){
            if (i - coin < 0){
                break;
            }
            dp[i] = std::min(1 + dp[i - coin], dp[i]);
        }
    }

    if (dp[x] != x + 2){
        std::cout << dp[x] << std::endl;
    } else {
        std::cout << -1 << std::endl;
    }
}