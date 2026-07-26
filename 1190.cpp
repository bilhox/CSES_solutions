#include <bits/stdc++.h>

using ll = long long;
using pair = std::array<ll, 4>;

pair operation(pair u, pair v){
    return {
        std::max({0ll, u[0], v[0], u[2] + v[1]}),
        std::max({0ll, u[1], u[3] + v[1]}),
        std::max({0ll, v[2], u[2] + v[3]}),
        u[3] + v[3]
    };
}

pair make_pair(ll v){
    ll u = std::max(v, 0ll);
    return {u, u, u, v};
}

template<typename T>
struct SegTree{

    unsigned long long size;
    T neutral;
    T (* op) (T, T);
    std::vector<T> data;

    void init(int n, T (* op)(T, T), T neutral){
        size = 1;
        while(size < n) size *= 2;
        data.assign(2 * size, neutral);
        this->neutral = neutral;
        this->op = op;
    }

    T query(size_t x, size_t xi, size_t yi, size_t xj, size_t yj) {
        if (yj < xi || xj >= yi){ // Completely outside
            return neutral;
        }

        if (xi <= xj && yj <= yi){ // Completely inside
            return data[x];
        }

        size_t m = (xj + yj) / 2;

        if (yi < m){
            return query(2 * x + 1, xi, yi, xj, m);
        } else if (xi >= m){
            return query(2 * x + 2, xi, yi, m, yj);
        } else {
            return op(query(2 * x + 1, xi, yi, xj, m), query(2 * x + 2, xi, yi, m, yj));
        }
    }

    T query(size_t sx, size_t sy){
        return query(0, sx, sy, 0, size);
    }

    void update(T val, size_t i, size_t x, size_t lx, size_t rx){
        /*
        lx, ly : boundaries of segment
        i : target index of the element to place
        x : recursive index
        val : the actual value
        */
        if (rx - lx == 1){ // We found the place
            data[x] = val;
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            update(val, i, 2 * x + 1, lx, m);
        } else {
            update(val, i, 2 * x + 2, m, rx);
        }

        data[x] = op(data[2 * x + 1], data[2 * x + 2]);
    }

    void update(T val, size_t i){
        update(val, i, 0, 0, size);
    }

};

int main() {

    std::ios_base::sync_with_stdio(false);
    std::cout.tie(NULL);
    std::cin.tie(NULL);

    int n, m;
    std::cin >> n >> m;

    std::vector<ll> values (n);

    SegTree<pair> st {};
    st.init(n, operation, make_pair(0));

    for (int i = 0; i < n; i++){
        std::cin >> values[i];
        st.update(make_pair(values[i]), i);
    }

    while (m--){
        long long k, x;
        std::cin >> k >> x;
        st.update(make_pair(x), k - 1);
        std::cout << st.query(0, n)[0] << '\n';
    }

    std::cout << std::endl;
    return 0;
}