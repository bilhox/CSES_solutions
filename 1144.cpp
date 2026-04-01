#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using ll = unsigned long long;

#define ordered_set tree<ll, null_type, std::less<ll>, rb_tree_tag, tree_order_statistics_node_update>

#define DEFAULT 1000000000
#define KEY 31443539979727

void print_m(std::unordered_map<ll, ll> & m){
    std::cout << "{";
    bool first = true;
    for (auto p : m){
        if (!first){
            std::cout << ", ";
        }
        std::cout << "(" << p.first << ", " << p.second << ")";
        first = false;
    }

    std::cout << "}" << std::endl;
}

int main() {

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, q;
    std::cin >> n >> q;

    std::vector<ll> values (n);

    ordered_set svalues {};
    std::unordered_map<ll, ll> mult {};

    for (int i = 0; i < n; i++){
        std::cin >> values[i];
        if (mult.find(values[i] ^ KEY) == mult.end())
            mult[values[i] ^ KEY] = 0;
        svalues.insert((values[i] << 31) + mult[values[i] ^ KEY]);
        mult[values[i] ^ KEY] ++;
    }

    while (q--){
        char op;
        ll a, b;
        std::cin >> op >> a >> b;
        if (op == '!'){
            mult[values[a - 1] ^ KEY] --;
            ll actual_value = (values[a - 1] << 31) + mult[values[a - 1] ^ KEY];
            svalues.erase(svalues.find(actual_value));
            values[a - 1] = b;
            if (mult.find(values[a - 1] ^ KEY) == mult.end())
                mult[values[a - 1] ^ KEY] = 0;
            svalues.insert((values[a - 1] << 31) + mult[values[a - 1] ^ KEY]);
            mult[values[a - 1] ^ KEY] ++;
        } else {
            int count = svalues.order_of_key((b + 1) << 31) - svalues.order_of_key(a << 31);
            std::cout << std::max(0, count) << '\n';
        }
    }

    std::cout << std::endl;

    return 0;
}