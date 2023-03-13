#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int n;
    long l;
    char s;
    float f;
    double db;
    
    scanf("%d %ld %c %f %lf", &n, &l, &s, &f, &db);
    printf("%d\n%ld\n%c\n%f\n%lf\n", n, l, s, f, db);
    return 0;
}