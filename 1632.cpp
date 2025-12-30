#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using movie_t = std::pair<long long, long long>;

int main(){

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int k, n;

    std::cin >> n >> k;

    std::vector<movie_t> movies(n);

    for (int i = 0; i < n; i++) std::cin >> movies[i].first >> movies[i].second;

    std::sort(movies.begin(), movies.end(), [&](auto a, auto b){
        return a.second < b.second;
    });

    std::multiset<long long> end_times {};
    int watched = 0;

    for (int i = 0; i < n; i++){

        auto it = end_times.upper_bound(movies[i].first);
        if (it != end_times.begin()){
            end_times.erase(--it);
        }

        if ((int) end_times.size() != k){
            watched ++;
            end_times.emplace(movies[i].second);
        }
    }

    std::cout << watched << std::endl;
}