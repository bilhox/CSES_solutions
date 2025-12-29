#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

int bin_search(std::vector<unsigned int> & l, unsigned int v, std::vector<bool> & visited){

    int left = -1;
    int right = l.size();
    int middle = 0;

    while (left + 1 < right){
        middle = (left + right) / 2;
        if (l[middle] <= v){
            left = middle;
        } else {
            right = middle;
        }
    }

    int a = left;
    while (a >= 0 && visited[a]){
        a -= 1;
    }

    if (a < 0){
        return -1;
    } else {
        visited[a] = true;
        return l[a];
    }
}

int main(){
    unsigned int n, m;
    std::cin >> n >> m;

    std::vector<unsigned int> h(n);
    std::vector<unsigned int> t(m);
    std::multiset<int> hm;

    for (unsigned int i = 0; i < n; i++) {
        std::cin >> h[i];
        hm.insert(h[i]);
    }
    for (unsigned int i = 0; i < m; i++) std::cin >> t[i];

    for (unsigned int tv : t){
        auto it = hm.upper_bound(tv);
        if (it == hm.begin()){
            std::cout << -1 << '\n';
        } else {
            std::cout << *(--it) << '\n';
            hm.erase(it);
        }
    }

    std::cout << std::endl;
}