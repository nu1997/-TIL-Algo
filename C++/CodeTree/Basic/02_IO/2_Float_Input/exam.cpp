// 실수 입력받아 계산 2

#include <iostream>
using namespace std;

int main() {
  float a;
  cin >> a;
  cout << fixed;
  cout.precision(2);
  cout << a + 1.5;
}