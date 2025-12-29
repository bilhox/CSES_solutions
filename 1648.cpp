#include <iostream>
#include <vector>
#include <limits>

class SegTree{

public:

    SegTree(size_t n){
        size = 1;
        while(size < n) size *= 2;
        sums.assign(2 * size, 0ll);
    }

    void set(long long val, size_t i){
        set(val, i, 0, 0, size);
    }

    long long sum(size_t sx, size_t sy){
        return sum(0, sx, sy, 0, size);
    }

    // void print(){
    //     std::cout << "\nSegment tree : " << std::endl;
    //     for (int i = 0; i < 2 * size - 1; i++){
    //         std::cout << "(" << sums[i].first << ", " << sums[i].second << ")" << "\n";
    //     }

    //     std::cout << "\n" << std::endl;
    // }

private:
    long long sum(size_t x, size_t sx, size_t sy, size_t lx, size_t rx) {
        if (rx < sx || lx >= sy){
            return 0;
        }

        if (sx <= lx && rx <= sy){
            return sums[x];
        }

        size_t m = (lx + rx) / 2;

        if (sy < m){
            return sum(2 * x + 1, sx, sy, lx, m);
        } else if (sx >= m){
            return sum(2 * x + 2, sx, sy, m, rx);
        } else {
            auto a = sum(2 * x + 1, sx, sy, lx, m);
            auto b = sum(2 * x + 2, sx, sy, m, rx);

            return a + b;
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
            sums[x] = val;
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            set(val, i, 2 * x + 1, lx, m);
        } else {
            set(val, i, 2 * x + 2, m, rx);
        }

        sums[x] = sums[2 * x + 1] + sums[2 * x + 2];
    }

    size_t size;
    std::vector<long long> sums;

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
        long long a, b, c;
        std::cin >> a >> b >> c;
        if (a == 2){
            std::cout << tree.sum(b - 1, c) << "\n";
        } else {
            tree.set(c, b - 1);
        }
    }
    std::cout << std::endl;
}