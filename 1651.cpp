#include <vector>
#include <array>
#include <iostream>

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
 
    long long get(size_t i){
        return get(0, i, 0, 0, size);
    }
 
    void set(size_t sx, size_t sy, long long val){
        set(0, sx, sy, 0, size, val);
    }
 
    // void print(){
    //     std::cout << "\nSegment tree : " << std::endl;
    //     for (int i = 0; i < 2 * size - 1; i++){
    //         std::cout << "(" << sums[i].first << ", " << sums[i].second << ")" << "\n";
    //     }
 
    //     std::cout << "\n" << std::endl;
    // }
 
private:
    void set(size_t x, size_t sx, size_t sy, size_t lx, size_t rx, long long val) {

        if (rx < sx || lx >= sy){
            return;
        }
 
        if (sx <= lx && rx <= sy){
            // std::cout << "hum ?" << std::endl;
            sums[x] += val;
            return;
        }
 
        size_t m = (lx + rx) / 2;
 
        if (sy < m){
            set(2 * x + 1, sx, sy, lx, m, val);
        } else if (sx >= m){
            set(2 * x + 2, sx, sy, m, rx, val);
        } else {
            set(2 * x + 1, sx, sy, lx, m, val);
            set(2 * x + 2, sx, sy, m, rx, val);
        }
    }
 
    long long get(long long val, size_t i, size_t x, size_t lx, size_t rx){
        /*
        lx, ly : boundaries of segment
        i : target index of the element to place
        x : recursive index
        val : the actual value
        */
        if (rx - lx == 1){
            return val + sums[x];
        }
 
        size_t m = (lx + rx) / 2;
        if (i < m){
            return get(val + sums[x], i, 2 * x + 1, lx, m);
        } else {
            return get(val + sums[x], i, 2 * x + 2, m, rx);
        }
    }
 
    size_t size;
    std::vector<long long> sums;
 
};

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, q;
    std::cin >> n >> q;

    SegTree tree (n);

    std::vector<long long> vals(n);
    for (int i = 0; i < n; i++){
        std::cin >> vals[i];
    }

    while(q--){
        int a;
        std::cin >> a;
        if (a == 1){
            int l, r;
            long long u;
            std::cin >> l >> r >> u;
            // std::cout << l << " " << r << std::endl;
            tree.set(l - 1, r, u);
        } else {
            int k;
            std::cin >> k;

            long long val = vals[k - 1] + tree.get(k - 1);

            std::cout << val << std::endl;
        }
    }

    std::cout << std::endl;
}