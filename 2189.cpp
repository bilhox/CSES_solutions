#include <iostream>
#include <array>

class Point{

public:
    long long x;
    long long y;
    Point(long long vx, long long vy) : x(vx), y(vy) {}
    Point() : x(0), y(0) {}
};

std::array<long long, 3> line_eq(Point & a, Point & b){
    std::array<long long, 3> coefs;

    coefs[0] = a.y - b.y;
    coefs[1] = b.x - a.x;
    coefs[2] = -coefs[0] * a.x - coefs[1] * a.y;

    return coefs;
}

long long test_equation(std::array<long long, 3> coefs, Point & c){
    return coefs[0] * c.x + coefs[1] * c.y + coefs[2];
}

void solve(){
    Point a;
    Point b;
    Point c;

    long long ax, ay, bx, by, cx, cy;

    std::cin >> ax >> ay >> bx >> by >> cx >> cy;
    
    a = Point(ax, ay);
    b = Point(bx, by);
    c = Point(cx, cy);

    auto equation = line_eq(a, b);
    long long val = test_equation(equation, c);

    if (val == 0){
        std::cout << "TOUCH" << std::endl;
    } else if (val < 0){
        std::cout << "RIGHT" << std::endl;
    } else {
        std::cout << "LEFT" << std::endl;
    }
}

int main(){
    int t;
    std::cin >> t;
    while(t--) solve();

    return 0;
}