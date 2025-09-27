#include <iostream>
using namespace std;

int main() 
{
    double vcompra;
    cout << "\nDigite o valor de sua compra";
    cin >> vcompra;
    
    if(vcompra>=100){
      cout << "\nFrete grátis";
    }
    else{
      int vsoma;
      vsoma = vcompra + 15;
      cout << "\nValor com frete:" << vsoma;
    }
    return 0;
}