# RTFM
###  dst_fd = open(dst_filename, O_WRONLY | O_CREAT | O_TRUNC, 0666);

#### solve

umask 002

# now recopy the flag.txt and cat it