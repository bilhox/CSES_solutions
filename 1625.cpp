#include <bits/stdc++.h>
using namespace std;

string s;
bool visited[7][7];

// Directions: R, L, U, D
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dir_index[256];

int dfs(int x, int y, int step) {
    // If at the endpoint (0,6), must have used all steps
    if (x == 0 && y == 6) 
        return step == 48;

    // If out of moves but not at endpoint → fail
    if (step == 48)
        return 0;

    char c = s[step];

    // If instruction is forced (not '?')
    if (c != '?') {
        int d = dir_index[c];
        int nx = x + dx[d], ny = y + dy[d];
        if (nx < 0 || nx >= 7 || ny < 0 || ny >= 7 || visited[ny][nx])
            return 0;
        visited[ny][nx] = true;
        int res = dfs(nx, ny, step + 1);
        visited[ny][nx] = false;
        return res;
    }

    // corridor pruning
    bool block[4] = {0};
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx < 0 || nx >= 7 || ny < 0 || ny >= 7 || visited[ny][nx])
            block[i] = true;
    }

    // horizontal corridor: U and D blocked but L and R free
    if (block[2] && block[3] && !block[0] && !block[1])
        return 0;

    // vertical corridor: L and R blocked but U and D free
    if (block[0] && block[1] && !block[2] && !block[3])
        return 0;

    int res = 0;
    for (int i = 0; i < 4; i++) {
        if (block[i]) continue;
        int nx = x + dx[i], ny = y + dy[i];
        visited[ny][nx] = true;
        res += dfs(nx, ny, step + 1);
        visited[ny][nx] = false;
    }
    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> s;

    // direction mapping
    dir_index['R'] = 0;
    dir_index['L'] = 1;
    dir_index['U'] = 2;
    dir_index['D'] = 3;

    memset(visited, 0, sizeof(visited));
    visited[0][0] = true;

    cout << dfs(0, 0, 0) << endl;
}
