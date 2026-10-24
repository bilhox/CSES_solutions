#include <bits/stdc++.h>

class A {
    int q;
    public:
        A(int k) {q = k;}
};

class B {
    int p;
    public:
        B(int k) {p = k;}
        operator A() {return A(2 * p);}
};



int main(){
    return 0;
}