#include <string.h>
#include <stdio.h>
#include <ctype.h>

void titulo(void){
    printf("+---------------------------------+\n");

    printf("\tCalculadora Bitwise\n");

    printf("+---------------------------------+\n");
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

int verificaInput(int *num_s1){

    int i;
    int valido = 1; // if (valido) ele e true se der certo e true == 1
    // colocar um if para pular essa parte caso esteja alocada na memoria
    for(int i; num_s1[i] != '\0'; i++){
        if(!isalnum(num_s1[i])){
            
            valido = 0;
            break;
        }     
    }
    if (valido){
        
        printf("O numero é valido: %s\n", num_s1);
        return 1;
    }else{

        printf("Voce deve digitar numeros\n");
        return 0;
    }
}

int pedir_numero1(char num_s1[], int tam, int *num1){

    while (1){
         
        printf("Digite um numero\n");
        if (fgets(num_s1, tam, stdin) != NULL){
            
            num_s1[strcspn(num_s1, "\n")] = '\0';
            if (verificaInput(num_s1)){

                sscanf (num_s1, "%d", num1);
            }
        }
        else{
            
            printf("Digite algo\n");
            return 0;
        }
    }   
}    


int main(void){
    
    int num1;
    int num2;
    
    char num_s1[10];
    char num_s2[10];

    
    while (1){


    
        
    }   
    
    return 0;
}
