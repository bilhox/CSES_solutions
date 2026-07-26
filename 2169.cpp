#include <bits/stdc++.h>

using ll = long long;
using segmentbuffed_t = std::array<ll, 3>;
using segment_t = std::pair<ll, ll>;
using bit_t = std::vector<int>;

int query(bit_t &bit, int index){
    int ans = 0;
    while (index > 0) {
        ans += bit[index];
        index -= index & (-index);
    }
    return ans;
}

void update(bit_t &bit, int index, int delta){
    while (index < bit.size()){
        bit[index] += delta;
        index += index & (-index);
    }
}

int main() {

    std::ios_base::sync_with_stdio(false);
    std::cout.tie(NULL);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::vector<segment_t> data (n);
    std::vector<ll> ends(n);
    for (int i = 0; i < n; i++){
        std::cin >> data[i].first >> data[i].second;
        ends[i] = data[i].second;
    }

    std::sort(ends.begin(), ends.end());
    std::map<ll, int> comp {};
    for (int i = 0; i < n; i++) comp[ends[i]] = i;

    std::vector<segmentbuffed_t> segments (n);

    for (int i = 0; i < n; i++){
        segments[i] = {data[i].first, (ll) comp[data[i].second], i};
    }

    std::sort(segments.begin(), segments.end(), [&] (segmentbuffed_t a, segmentbuffed_t b){
        return (a[0] == b[0]) ? a[1] >= b[1] : a[0] < b[0];
    });

    std::vector<int> bit(n + 1, 0);
    std::vector<int> result (n, 0);

    for (int i = n - 1; i >= 0; i--){
        result[segments[i][2]] = query(bit, segments[i][1] + 1);
        update(bit, segments[i][1] + 1, 1);
    }

    for (int i = 0; i < n; i++) std::cout << result[i] << ' ';
    std::cout << '\n';
    std::fill(result.begin(), result.end(), 0);
    std::fill(bit.begin(), bit.end(), 0);

    for (int i = 0; i < n; i++){
        result[segments[i][2]] = i - query(bit, segments[i][1]);
        update(bit, segments[i][1] + 1, 1);
    }

    for (int i = 0; i < n; i++) std::cout << result[i] << ' ';
    std::cout << std::endl;

    return 0;
}