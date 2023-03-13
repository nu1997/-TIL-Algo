#include <iostream>
using namespace std;

int main() {
  cout << fixed;
  int i = 13;
  double d = 0.165;
  double ans = i * d;
  cout.precision(6);
  cout << i << " * " << d << " = " << ans;
  return 0;
}