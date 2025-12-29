#include <iostream>
#include <vector>

struct seg_item{
    long long seg, pref, suf, sum;
};

#define MIN_BOUND -1000000000

struct SegTree{

    long long size;
    std::vector<seg_item> values;

    seg_item NEUTRAL_ELEMENT {MIN_BOUND, MIN_BOUND, MIN_BOUND, 0};

    void init(int n){
        size = 1;
        while(size < n) size *= 2;
        values.assign(2 * size, NEUTRAL_ELEMENT);
    }

    seg_item single(int val){
        return {val, val, val, val};
    }

    seg_item merge(seg_item a, seg_item b){
        return {
            std::max(a.seg, std::max(b.seg, a.suf + b.pref)),
            std::max(a.pref, a.sum + b.pref),
            std::max(b.suf, b.sum + a.suf),
            a.sum + b.sum
        };
    }

    void build(std::vector<long long> & vals, size_t x, size_t lx, size_t rx) {
        if (rx - lx == 1){
            if (lx < vals.size()){
                values[x] = single(vals[lx]);
            }
            return;
        }

        size_t m = (lx + rx) / 2;
        build(vals, 2 * x + 1, lx, m);
        build(vals, 2 * x + 2, m, rx);

        values[x] = merge(values[2 * x + 1], values[2 * x + 2]);
    }

    void build(std::vector<long long> & vals){
        return build(vals, 0, 0, size);
    }

    void set(long long val, size_t i, size_t x, size_t lx, size_t rx){
        /*
        lx, ly : boundaries of segment
        i : target index of the element to place
        x : recursive index
        val : the actual value
        */
        if (rx - lx == 1){
            values[x] = single(val);
            return;
        }

        size_t m = (lx + rx) / 2;
        if (i < m){
            set(val, i, 2 * x + 1, lx, m);
        } else {
            set(val, i, 2 * x + 2, m, rx);
        }

        values[x] = merge(values[2 * x + 1], values[2 * x + 2]);
    }

    void set(long long val, size_t i){
        set(val, i, 0, 0, size);
    }

    seg_item calc(size_t l, size_t r, size_t x, size_t lx, size_t rx){
        if (lx >= r || l >= rx) return NEUTRAL_ELEMENT;
        if (lx >= l && rx <= r) return values[x];

        size_t m = (lx + rx) / 2;
        auto i1 = calc(l, r, 2 * x + 1, lx, m);
        auto i2 = calc(l, r, 2 * x + 2, m, rx);

        return merge(i1, i2);
    }

    long long calc(){
        return calc(0, size, 0, 0, size).seg;
    }

};

int main(){
    int n;
    std::cin >> n;
    std::vector<long long> vals(n);
    SegTree tree {};
    tree.init(n);

    for (int i = 0; i < n; i++){
        std::cin >> vals[i];
    }

    tree.build(vals);

    std::cout << tree.calc() << std::endl;
}