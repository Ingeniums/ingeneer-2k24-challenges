#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* FUN_22384(char* s, int num) {
    int i;
    int k;
    int d;
    for (i = 0; i < strlen(s); i++) {
        if (isalpha(s[i])) {
            if (islower(s[i])) {
                k = ('z' - s[i]);
                d = num;
                if (s[i] > ('z' - num)) {
                    s[i] = '0' - 1 - k + d;
                } else {
                    s[i] += d;
                }
            } else if (isupper(s[i])) {
                k = ('Z' - s[i]);
                d = num;
                if (s[i] > ('Z' - num)) {
                    s[i] = 'a' - 1 - k + d;
                } else {
                    s[i] += d;
                }
            }
        } else if (isdigit(s[i])) {
            d = ('9' - s[i]);
            k = num;
            if (s[i] > ('9' - num)) {
                s[i] = 'A' - 1 - d + k;
            } else {
                s[i] += k;
            }
        }
    }
    return s;
}

int main() {
    char key[100];
    printf("gimme license key: ");
    fgets(key, sizeof(key), stdin);
    key[strcspn(key, "\n")] = '\0'; // remove trailing newline character
    
    char* b = FUN_22384(key, 8);

    if (strcmp(b, "OpWz0oQvXRNxRFGoW4GmzTujfeXIwr") != 0) {
        printf("invalid key\n");
    } else {
        printf("you shall pass!\n");
    }

    return 0;
}
