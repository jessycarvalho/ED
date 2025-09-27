#include <stdio.h>
int main()
{
    int idade;
    printf("\nDigite sua idade");
    scanf("%d", &idade);
    if(idade < 18) {
      printf("\nVocê é menor de idade!");
    }
    else {
      printf("\nVocê é maior de idade!");
    }
    return 0;
}