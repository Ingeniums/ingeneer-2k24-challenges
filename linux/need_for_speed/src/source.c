#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>


void disable_buffering(void)
{
    setbuf(stdout, NULL);
}

int main() {

    disable_buffering();

    FILE *p = fopen("password.txt", "w+");
    fprintf(p, "nonono\n");
    fclose(p);

    // read 6 bytes from password.txt
    p = fopen("password.txt", "r");
    char buf[7];
    fread(buf, 1, 6, p);
    fclose(p);

    if (strncmp(buf, "hacker", 6) == 0) {
        FILE *flag = fopen("flag.txt", "r");
        char flag_buffer[100];
        fgets(flag_buffer, 100, flag);
        printf("%s", flag_buffer);
    } else {
        puts("seems impossible right?");
    }

}