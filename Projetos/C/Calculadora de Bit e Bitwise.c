#include <string.h>
#include <stdio.h>
#include <ctype.h>

void titulo(void){
    printf("+---------------------------------+\n");

    printf("\tCalculadora Bitwise\n");

    printf("+---------------------------------+\n");
}

int verificaInput(int *num_s1){

    int i;
    // colocar um if para pular essa parte caso esteja alocada na memoria
    for(*num_s1; sizeof(*num_s1), i++){

        if(!isalnum(i)){

            printf("Digite numeros nao letras ou simbolos\n");
            return 0;
        }
        else{

            printf("Numero valido: %p\n", num_s1);
            
            return num_s1;
        }
    }

}


int pedir_numero(int *num1, int *num2){


    
    if (fgets(num_s1, sizeof(num_s1), stdin) != NULL && !isalnum) {

        num_s1[strcspn(num_s1, "\n")] = '\0';

    } 





}    

void tituloOperadores(void){
    printf("+---------------------------------+\n");
    printf("|      Operadores Disponiveis      |\n");
    printf("+---------------------------------+\n");
    printf("|  1 - AND (&)                     |\n");
    printf("|  2 - OR  (|)                      |\n");
    printf("|  3 - XOR (^)                     |\n");
    printf("|  4 - NOT (~)                     |\n");
    printf("|  5 - SHL (<<)                    |\n");
    printf("|  6 - SHR (>>)                    |\n");
    printf("+---------------------------------+\n");
}



int main(void){
    
    int num1;
    int num2;
    
    char num_s1[10];
    char num_s2[10];

    int loop = 0;
    while (loop == 0){


    
        loop += 1;
    }   
    
    return 0;
}
