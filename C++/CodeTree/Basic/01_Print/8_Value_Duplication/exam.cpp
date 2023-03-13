// 합을 복사하기

#include <iostream>
using namespace std;

int main() {
  int a = 1, b = 2, c = 3, s;
  s = a + b + c;
  a = b = c = s;
  cout << a << " " << b << " " << c;
  return 0;
}