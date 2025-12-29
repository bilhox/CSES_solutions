#include <iostream>
#include <vector>
#include <limits>

class SegTree{

public:

    SegTree(size_t n){
        size = 1;
        while(size < n) size *= 2;
        xors.assign(2 * size, 0ll);
    }

    void set(long long val, size_t i){
        set(val, i, 0, 0, size);
    }

    long long calc_xor(size_t sx, size_t sy){
        return calc_xor(0, sx, sy, 0, size);
    }

private:
    long long calc_xor(size_t x, size_t sx, size_t sy, size_t lx, size_t rx) {
        if (rx < sx || lx >= sy){
            return 0;
        }

        if (sx <= lx && rx <= sy){
            return xors[x];
        }

        size_t m = (lx + rx) / 2;

        if (sy < m){
            return calc_xor(2 * x + 1, sx, sy, lx, m);
        } else if (sx >= m){
            return calc_xor(2 * x + 2, sx, sy, m, rx);
        } else {
            auto a = calc_xor(2 * x + 1, sx, sy, lx, m);
            auto b = calc_xor(2 * x + 2, sx, sy, m, rx);

            return a ^ b;
        }
    }

    void set(long long val, size_t i, size_t x, size_t lx, size_t rx){
        /*
        lx, ly : boundaries of segment
        i : target index of the element to place
        x : recursive index
        val : the actual value
        */
        if (rx - lx == 1){
            xors[x] = val;
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            set(val, i, 2 * x + 1, lx, m);
        } else {
            set(val, i, 2 * x + 2, m, rx);
        }

        xors[x] = xors[2 * x + 1] ^ xors[2 * x + 2];
    }

    size_t size;
    std::vector<long long> xors;

};

int main(){
    int n, q;
    std::cin >> n >> q;
    SegTree tree(n);

    for (int i = 0; i < n; i++){
        long long val;
        std::cin >> val;
        tree.set(val, i);
    }

    while(q--){
        long long a, b;
        std::cin >> a >> b;
        std::cout << tree.calc_xor(a - 1, b) << "\n";
    }
    std::cout << std::endl;
}