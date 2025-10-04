#include <stdio.h>
int main()
{
  int n;
  printf("\nDigite um número: ");
  scanf("%d", &n);
  int i;
    for (i = 1; i < 11; ++i){
      printf("%d ", n*i);
    }
    return 0;
}