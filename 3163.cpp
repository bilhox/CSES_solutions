#include <bits/stdc++.h>

using op_t = std::array<int, 3>;

void update(std::vector<int> &bit, int index, int delta){
    index ++;
    while(index < bit.size()){
        bit[index] += delta;
        index += index & (-index);
    }
}

int query(std::vector<int> &bit, int index){
    int total = 0;
    index++;
    while(index > 0){
        total += bit[index];
        index -= index & (-index);
    }
    return total;
}

 
int main() {
 
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
 
    int n, m;
    std::cin >> n >> m;
 
    std::vector<int> values (n);
    for (int i = 0; i < n; i++) std::cin >> values[i];

    std::vector<int> bit(n + 1, 0);
    std::map<long long, int> comp {};

    std::sort(values.begin(), values.end());

    int ind = -1;
    for (int i = 0; i < n; i++){
        if (comp.find(values[i]) == comp.end()){
            ind++;
            comp[values[i]] = ind;
        }
    }

    std::vector<op_t> ops1(m);
    std::vector<op_t> ops2(m);

    for (int i = 0; i < m; i++){
        int a, b;
        long long c, d;
        std::cin >> a >> b >> c >> d;
        ops1[i][0] = a; ops1[i][1] = b; ops1[i][2] = c;
        ops2[i][0] = a; ops1[i][1] = b; ops1[i][2] = d;
    }

    std::cout << std::endl;
 
    return 0;
}