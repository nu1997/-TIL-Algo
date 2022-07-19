// 길이 단위 환산하기

#include <iostream>
using namespace std;

int main() {
  float ft = 30.48, n;
  cin >> n;
  cout << fixed;
  cout.precision(1);
  cout << ft * n;
}