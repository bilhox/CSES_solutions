#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
#include <cstdint>

int main(){
    int n;
    std::cin >> n;

    std::vector<uint64_t> rooms (2*n);
    uint64_t n_dim = 2 * (uint64_t) n;
    uint64_t i_dim = n;
    for (int i = 0; i < n; i++){
        unsigned int a, b;
        std::cin >> a >> b;
        rooms[2 * i] = n_dim * a + i;
        rooms[2 * i + 1] = n_dim * b + i_dim + i;
    }

    std::sort(rooms.begin(), rooms.end());

    // for (auto val : rooms) std::cout << "(" << val[0] << ", " << val[1] << ", " << val[2] << ") ";
    // std::cout << std::endl;

    std::vector<int> assigned (n);
    int room_n = 0;
    std::deque<int> available{};

    for (auto room : rooms){
        uint64_t val = room % n_dim;
        uint64_t index = val % i_dim;
        uint64_t is_departure = val / i_dim;

        if (is_departure){
            available.push_back(assigned[index]);
        } else {
            if (available.size() == 0){
                room_n ++;
                available.push_back(room_n);
            }
            assigned[index] = available.back();
            available.pop_back();
        }
    }

    std::cout << room_n << '\n';
    for (auto val : assigned) std::cout << val << " ";
    std::cout << std::endl;
}