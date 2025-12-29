#include <iostream>
#include <vector>
#include <limits>

class SegTree{

public:

    SegTree(size_t n){
        size = 1;
        while(size < n) size *= 2;
        mins.assign(2 * size, std::numeric_limits<long long>::max());
    }

    void set(long long val, size_t i){
        set(val, i, 0, 0, size);
    }

    long long min(size_t sx, size_t sy){
        return min(0, sx, sy, 0, size);
    }

private:
    long long min(size_t x, size_t sx, size_t sy, size_t lx, size_t rx) {
        if (rx < sx || lx >= sy){
            return std::numeric_limits<long long>::max();
        }

        if (sx <= lx && rx <= sy){
            return mins[x];
        }

        size_t m = (lx + rx) / 2;

        if (sy < m){
            return min(2 * x + 1, sx, sy, lx, m);
        } else if (sx >= m){
            return min(2 * x + 2, sx, sy, m, rx);
        } else {
            auto a = min(2 * x + 1, sx, sy, lx, m);
            auto b = min(2 * x + 2, sx, sy, m, rx);

            return std::min(a, b);
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
            mins[x] = val;
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            set(val, i, 2 * x + 1, lx, m);
        } else {
            set(val, i, 2 * x + 2, m, rx);
        }

        mins[x] = std::min(mins[2 * x + 1], mins[2 * x + 2]);
    }

    size_t size;
    std::vector<long long> mins;

};

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n, q;
    std::cin >> n >> q;
    SegTree tree(n);

    for (int i = 0; i < n; i++){
        long long val;
        std::cin >> val;
        tree.set(val, i);
    }

    while(q--){
        long long a, b, c;
        std::cin >> a >> b >> c;
        if (a == 2){
            std::cout << tree.min(b - 1, c) << "\n";
        } else {
            tree.set(c, b - 1);
        }
    }
    std::cout << std::endl;
}