#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void win() {
    puts("gg");
    FILE *fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("flag.txt not found\n");
        exit(1);
    }

    char flag[100];
    fgets(flag, 100, fp);
    printf("%s\n", flag);
    fclose(fp);
}


int main() {
    char buffer[16];
    disable_buffering();
    puts("a bof challenge for everyone!!");
    printf("pay>");
    fgets(buffer, 100, stdin);

    char b = buffer[0];
    return 0;
}