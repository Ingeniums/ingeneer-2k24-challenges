#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int flagInName(char *name) {
    if (strstr(name, "flag") != NULL) {
        return 1;
    }
    return 0;
}

int main() {
    disable_buffering();
    puts("");
    int flag = open("flag.txt", 0);
    if (flag == -1) {
        printf("err opening flag file hh\n");
        exit(1);
    }
    char buffer[20];
    char data[100];
    while(1) {
        printf("gimme file to read>");
        fgets(buffer, 20, stdin);
        // remove newline
        buffer[strcspn(buffer, "\n")] = 0;
        if (flagInName(buffer)) {
            printf("cmon, ez but not that ez\n");
            exit(1);
        }
        FILE *fp = fopen(buffer, "r");
        if (fp == NULL) {
            printf("file not found\n");
            continue;
        }
        fread(data, 1, 100, fp);
        printf("file content: %s\n", data);
    }
}