#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void calcula_bases(int op_base);
void menu_conversor(int base_origem);
void tabela_op_base(void);

int main(void) {
    int op_base;
    tabela_op_base();
    printf("Digite a base para a conversao\n>> ");
    
    if (scanf("%d", &op_base) == 1) {
        calcula_bases(op_base);
    } else {
        printf("Entrada invalida!\n");
    }

    return 0;
}

void calcula_bases(int op_base) {
    switch (op_base) {
        case 2:  menu_conversor(2);  break;
        case 8:  menu_conversor(8);  break;
        case 10: menu_conversor(10); break;
        case 16: menu_conversor(16); break;
        case 32: menu_conversor(32); break;
        case 64: menu_conversor(64); break;
        default:
            printf("Digite uma opção valida\n");
            break;
    }
}

void menu_conversor(int base_origem) {
    int base_valida[] = {2, 8, 10, 16, 32, 64};
    int tamanho_array = sizeof(base_valida) / sizeof(base_valida[0]);
    
    bool base_suporte = false;
    for (int i = 0; i < tamanho_array; i++) {
        if (base_valida[i] == base_origem) {
            base_suporte = true;
            break;
        }
    }
    
    if (!base_suporte) {
        printf("Digite uma base valida\n");
        return;
    }

    printf("\nQual operação deseja fazer?\n");
    int op = 1;
    for (int i = 0; i < tamanho_array; i++) {
        int base_escolha = base_valida[i];
        if (base_escolha != base_origem) {
            printf("%d: %d -> %d\n", op++, base_origem, base_escolha);
        }
    }

    int opcao_escolhida;
    printf("\nEscolha a opcao desejada\n>> ");
    if (scanf("%d", &opcao_escolhida) != 1) {
        printf("Opcao invalida!\n");
        return;
    }

    int base_destino = -1;
    int contador_op = 1;

    for (int i = 0; i < tamanho_array; i++) {
        if (base_valida[i] != base_origem) {
            if (contador_op == opcao_escolhida) {
                base_destino = base_valida[i];
                break;
            }
            contador_op++;
        }
    }

    if (base_destino != -1) {
        printf("\n--> Perfeito! Vamos converter da Base %d para a Base %d.\n", base_origem, base_destino);
    } else {
        printf("Opcao fora do menu!\n");
    }
}

void tabela_op_base(void) {
    printf("=========================================\n");
    printf("     BASES SUPORTADAS PARA ENTRADA       \n");
    printf("=========================================\n");
    printf("  [ 2  ]  Binario                        \n");
    printf("  [ 8  ]  Octal                          \n");
    printf("  [ 10 ]  Decimal                        \n");
    printf("  [ 16 ]  Hexadecimal                    \n");
    printf("  [ 32 ]  Base32                         \n");
    printf("  [ 64 ]  Base64                         \n");
    printf("=========================================\n");
}
