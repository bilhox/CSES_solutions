#include <bits/stdc++.h>

using ul = unsigned long;

int main(){

    int n, m;
    std::cin >> n >> m;

    std::multiset<ul> a {};
    std::unordered_map<ul, std::deque<int>> ind {};
    for (int i = 0; i < n; i++){
        ul r = 0;
        std::cin >> r;
        a.emplace(r);
        if (ind.find(r) == ind.end())
            ind[r] = {};
        
        ind[r].push_front(i);
    }

    for (int i = 0; i < m; i++){
        ul r;
        std::cin >> r;
        auto l = a.lower_bound(r);
        if (l == a.end()){
            std::cout << 0 << " ";
        } else {
            ul vl = *l;
            auto index = ind[vl].back();
            ind[vl].pop_back();
            a.extract(vl);
            if (ind.find(vl - r) == ind.end())
                ind[vl - r] = {};
            
            ind[vl - r].push_front(index);
            std::cout << index + 1 << " ";
        }
    }

    std::cout << std::endl;
    return 0;
}