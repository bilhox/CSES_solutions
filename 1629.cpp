#include <iostream>
#include <vector>
#include <algorithm>

using t_movie = std::pair<unsigned int, unsigned int>;

int main(){
    int n;
    std::cin >> n;

    std::vector<t_movie> movies (n);

    for (int i = 0; i < n; i++){
        std::cin >> movies[i].first >> movies[i].second;
    }

    std::sort(movies.begin(), movies.end(), [](t_movie & l, t_movie & r){
        return l.first <= r.first && (l.second - l.first) <= (r.second - r.first);
    });

    int curr_v = 0;
    t_movie current_movie {0, 0};

    for (auto movie : movies){
        if (current_movie.first == 0 || current_movie.second <= movie.first || current_movie.first >= movie.second){
            curr_v ++;
            current_movie = movie;
        }
    }

    std::cout << curr_v << std::endl;
}