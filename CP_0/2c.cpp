#include<stdio.h>
#include<math.h>

int main(){

    float n = 1.0;
    float i = 1.0;
    while(pow(n,i) < 1e100){
        i++;
        if(i > 100){
            printf("no se pudo encontrar el valor, se sale de los rangos de float");
            return 0;
        }
            
    }
    printf("%d", i);
        
    return 0;
}
