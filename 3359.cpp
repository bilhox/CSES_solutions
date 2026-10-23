#include <bits/stdc++.h>

using namespace std;

using ul = unsigned long long;

int main(){
    int n;

    cin >> n;

    vector<string> grid(n);

    for (int i = 0; i < n; i++)
        cin >> grid[i];

    vector<vector<int>> dp_to(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (i == n - 1 && j == n - 1) continue;

            int dist = i + j;
            int where = 0;
            ul score = numeric_limits<int>::max();
            if (j < n - 1){
                score = dp[i][j + 1];
                where = 1;
            }

            if (i < n - 1){
                if (dp[i + 1][j] < score){
                    score = dp[i + 1][j];
                    where = 2;
                }
            }

            dp[i][j] = score + (2 * n - dist) * (2 * n - dist) * (grid[i][j] - 'A' + 1);
            dp_to[i][j] = where;
        }
    }

    // for (int i = 0; i < n; i++){
    //     for (int j = 0; j < n; j++){
    //         cout << dp_to[i][j];
    //     }

    //     cout << "\n";
    // }

    // cout << "huh ?" << endl;

    stringstream ss;
    int cx = n - 1, cy = n - 1;
    while (dp_to[cy][cx] != 0){
        ss << grid[cy][cx];
        if (dp_to[cy][cx] == 1)
            cx -= 1;
        else
            cy -= 1;
    }

    ss << grid[0][0];

    std::cout << ss.str() << std::endl;
}