// 길이 단위 변환하기

#include <iostream>
using namespace std;

int main() {
  double x = 9.2, y = 1.3, ft = 30.48, mi = 160934;
  cout << fixed;
  cout.precision(1);
  cout << x << "ft" << " = " << x * ft << "cm" << endl;
  cout << y << "mi" << " = " << y * mi << "cm";
  return 0;
}