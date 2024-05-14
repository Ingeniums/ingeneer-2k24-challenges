#include <stdlib.h>
#include <stdio.h>

char flag[100];

void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
    disable_buffering();
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("flag file is missing.\n");
        exit(1);
    }
    // replace the flag.txt woth "no flag anymore"
    fgets(flag, 100, f);
    fclose(f);

    f = fopen("flag.txt", "w");
    fprintf(f, "no flag anymore\n");
    fclose(f);

    // make the program segfault to generate a core dump
    char *ptr = NULL;
    *ptr = 0;
}