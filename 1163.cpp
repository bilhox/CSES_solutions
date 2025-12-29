#include <iostream>
#include <vector>
#include <set>
#include <unordered_map> 
#include <algorithm>

void incr_map(std::unordered_map<long long, int> & m, long long key, int increment){
    if (m.find(key) == m.end()){
        m[key] = increment;
    } else {
        m[key] += increment;
    }
}

void print_vec(std::vector<long long> & v){
    for (auto val : v){
        std::cout << val << " ";
    }

    std::cout << std::endl;
}

void print_map(std::unordered_map<long long, int> & m){
    for (auto val : m){
        std::cout << val.first << ": " << val.second << ", ";
    }

    std::cout << std::endl;
}

int main(){

    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int n;
    long long x;
    std::cin >> x >> n;

    std::vector<long long> traffic_lights(n);

    for (int i = 0; i < n; i++){
        std::cin >> traffic_lights[i];
    }

    std::set<long long> a {};
    a.emplace(0);
    a.emplace(x);

    std::unordered_map<long long, int> count {};
    std::vector<long long> heap {};
    std::vector<long long> results (n);

    std::make_heap(heap.begin(), heap.end());

    for (int i = 0; i < n; i++){
        auto curr = traffic_lights[i];
        a.emplace(curr);

        auto minv = *(--a.lower_bound(curr));
        auto maxv = *a.upper_bound(curr);

        incr_map(count, maxv - minv, -1);
        incr_map(count, maxv - curr, 1);
        incr_map(count, curr - minv, 1);

        heap.push_back(maxv - curr);
        std::push_heap(heap.begin(), heap.end());
        heap.push_back(curr - minv);
        std::push_heap(heap.begin(), heap.end());


        std::pop_heap(heap.begin(), heap.end());
        auto result = heap.back();
        heap.pop_back();

        while (count[result] == 0){
            std::pop_heap(heap.begin(), heap.end());
            result = heap.back();
            heap.pop_back();
        }

        heap.push_back(result);
        std::push_heap(heap.begin(), heap.end());

        results[i] = result;
    }

    for (auto res : results){
        std::cout << res << " ";
    }

    std::cout << std::endl;
}