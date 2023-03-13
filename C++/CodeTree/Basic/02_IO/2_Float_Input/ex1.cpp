// 실수 받아 그대로 출력
#include <iostream>
using namespace std;

int main() {
  double n;
  cin >> n;
  cout << fixed;
  cout.precision(2);
  cout << n;
}