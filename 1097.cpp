#include <iostream>
#include <vector>
#include <numeric>


using ll = long long;
using t_scores = std::pair<ll, ll>;

int main() {

    int n;
    std::cin >> n;

    std::vector<std::vector<t_scores>> dp (n, std::vector<t_scores>(n));

    std::vector<ll> x (n);

    for (int i = 0; i < n; i++){
        std::cin >> x[i];
    }

    bool turn = n % 2;

    for (int i = 0; i < n; i++){
        if (turn)
            dp[i][0].first = x[i];
        else
            dp[i][0].second = x[i];
    }

    for (int i = 1; i < n; i ++){
        turn = !turn;
        for (int j = 0; j < n - i; j++){
            if (turn) {
                if (dp[j][i - 1].first + x[j + i] < dp[j + 1][i - 1].first + x[j]){
                    dp[j][i].second = dp[j + 1][i - 1].second;
                    dp[j][i].first = dp[j + 1][i - 1].first + x[j];
                } else {
                    dp[j][i].second = dp[j][i - 1].second;
                    dp[j][i].first = dp[j][i - 1].first + x[j + i];
                }
            } else {
                if (dp[j][i - 1].second + x[j + i] < dp[j + 1][i - 1].second + x[j]){
                    dp[j][i].first = dp[j + 1][i - 1].first;
                    dp[j][i].second = dp[j + 1][i - 1].second + x[j];
                } else {
                    dp[j][i].first = dp[j][i - 1].first;
                    dp[j][i].second = dp[j][i - 1].second + x[j + i];
                }
            }
        }
    }

    std::cout << dp[0][n - 1].first << std::endl;

    return 0;
}