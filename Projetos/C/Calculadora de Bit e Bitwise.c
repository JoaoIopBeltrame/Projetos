#include <string.h>
#include <stdio.h>
#include <ctype.h>

// add a parte la da divisao de restos e o proprio num por ele mesmo n = n/2 dentro de um while(num>=0)
// add os & | e ^ ~ ! >> << bitwise
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

int verificaInput(char *num_s){
    int i;
    int valido = 1; // if (valido) ele e true se der certo e true == 1
    // colocar um if para pular essa parte caso esteja alocada na memoria
    for(int i = 0; num_s[i] != '\0'; i++){
        if(!isalnum(num_s[i])){
            
            valido = 0;
            break;
        }     
    }
    if (valido){
        
        printf("O numero é valido: %s\n", num_s);
        return 1;
    }else{

        printf("Voce deve digitar numeros\n");
        return 0;
    }
}

int pedir_numero(char num_s[], int tam, int *num, int qualRep){

    while (1){
         
        printf("Digite %dº numero\n", qualRep);
        if (fgets(num_s, tam, stdin) != NULL){
            
            num_s[strcspn(num_s, "\n")] = '\0';
            if (verificaInput(num_s)){

                sscanf (num_s, "%d", num);
                return 1;
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

    pedir_numero(num_s1, 10, &num1, 1);
    pedir_numero(num_s2, 10, &num2, 2);
    
    return 0;
}
