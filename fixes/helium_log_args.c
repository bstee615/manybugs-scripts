void helium_log_argv(int argc, char **argv) {
    FILE *fp = fopen("run.sh", "a");
    for (int i = 0; i < argc; i ++) {
        fprintf(fp, " %s", argv[i]);
    }
    fprintf(fp, "\n");
}
