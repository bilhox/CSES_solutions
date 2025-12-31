#include <iostream>
#include <vector>

int main(){
    int n, x;

    std::cin >> n >> x;

    std::vector<int> h(n);
    std::vector<int> s(n);

    for (int i = 0; i < n; i++) std::cin >> h[i];
    for (int i = 0; i < n; i++) std::cin >> s[i];

    std::vector<int> dp(x + 1);
    int max_val = 0;

    for (int i = 0; i < n; i++){
        for (int j = x; j >= h[i]; j--){
            dp[j] = std::max(dp[j], dp[j - h[i]] + s[i]);
            max_val = std::max(max_val, dp[j]);
        }
    }

    std::cout << max_val << std::endl;
}