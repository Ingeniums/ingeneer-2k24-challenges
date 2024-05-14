#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <time.h> 

#define MAX_FILENAME_LEN 256
#define BUFFER_SIZE 4096
 
char *generate_random_filename() {
    char *filename = malloc(MAX_FILENAME_LEN);
    if (!filename) {
        perror("Failed to allocate memory for filename");
        exit(EXIT_FAILURE);
    }

    srand(time(NULL));

    snprintf(filename, MAX_FILENAME_LEN, "/tmp/copy_%d", rand());
    return filename;
}

void copy_file(const char *src_filename, const char *dst_filename) {
    int src_fd, dst_fd;
    ssize_t bytes_read;
    char buffer[BUFFER_SIZE];

    src_fd = open(src_filename, O_RDONLY);
    if (src_fd == -1) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    dst_fd = open(dst_filename, O_WRONLY | O_CREAT | O_TRUNC, 0666);
    if (dst_fd == -1) {
        perror("Error opening destination file");
        exit(EXIT_FAILURE);
    }

    while ((bytes_read = read(src_fd, buffer, BUFFER_SIZE)) > 0) {
        if (write(dst_fd, buffer, bytes_read) != bytes_read) {
            perror("Error writing to destination file");
            exit(EXIT_FAILURE);
        }
    }

    if (bytes_read == -1) {
        perror("Error reading from source file");
        exit(EXIT_FAILURE);
    }

    if (close(src_fd) == -1 || close(dst_fd) == -1) {
        perror("Error closing files");
        exit(EXIT_FAILURE);
    }

    if (chown(dst_filename, 0, 0) == -1) { // change owner to root
        perror("Error changing owner of destination file");
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <source_filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char *src_filename = argv[1];

    char *dst_filename = generate_random_filename();

    copy_file(src_filename, dst_filename);

    printf("File copied successfully as: %s\n", dst_filename);

    free(dst_filename);

    return 0;
}
