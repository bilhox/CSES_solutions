#include <bits/stdc++.h>
using namespace std;

long long n, k;
vector<long long> a;

bool check(long long x) {
    long long current_sum = 0;
    long long counter = 0;

    for (long long v : a) {
        current_sum += v;

        if (current_sum >= x) {
            counter++;
            if (current_sum == x) {
                current_sum = 0;
            } else {
                current_sum = v;  // reset to v
            }
            if (current_sum > x) {
                return false;
            }
        }
    }

    if (current_sum > 0)
        counter++;

    return counter <= k;
}

long long dicho() {
    long long left = -1;
    long long right = 1000000000000000LL; // 1e15

    while (left + 1 < right) {
        long long middle = (left + right) / 2;
        if (check(middle)) {
            right = middle;
        } else {
            left = middle;
        }
    }

    return right;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    a.resize(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    cout << dicho() << "\n";
    return 0;
}
