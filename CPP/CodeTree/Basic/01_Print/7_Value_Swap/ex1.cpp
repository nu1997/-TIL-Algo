// 변수값 교체하기 3

#include <iostream>
using namespace std;

int main() {
  int a = 3, b = 5, temp;
  temp = a;
  a = b;
  b = temp;
  cout << a << endl << b;
  return 0;
}