#include <iostream>
using namespace std;

int main() 
{
  int n;
  cout << "Digite um número inteiro positivo: ";
  cin >> n;
  
  while (n > 0) {
    cout << n << "\n";
    n--;
    
  }
  return 0;
}