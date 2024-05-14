#include <sys/mman.h>
#include <stdio.h>

volatile int auth = 0;

void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main () {
    disable_buffering();
    mprotect((void*)((unsigned long)main & ~0xFFF), 4096 * 4, PROT_READ | PROT_WRITE | PROT_EXEC);
    
    unsigned int offset;
    printf("offset: ");
    scanf("%d", &offset);

    unsigned char new_bytes[2];
    printf("bytes: ");
    scanf("%2s", &new_bytes);

    *(unsigned short*)(offset) = *(unsigned short*)new_bytes;

    puts("procceeding with execution...");
    

    if (auth == 0xbeef) {
        FILE *f = fopen("flag.txt", "r");
        char flag[64];
        fgets(flag, 64, f);
        printf("%s\n", flag);
    } else {
        printf("git gud\n");
    }
}