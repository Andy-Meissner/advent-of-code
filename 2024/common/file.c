#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char** read_file_lines(const char* filename, int* line_count) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Could not open file");
        return NULL;
    }

    // Allocate initial space for the array of strings
    int capacity = 10;
    char** lines = malloc(capacity * sizeof(char*));
    if (!lines) {
        perror("Failed to allocate memory");
        fclose(file);
        return NULL;
    }

    char buffer[256];
    *line_count = 0;

    while (fgets(buffer, 256, file)) {
        // Remove newline character at the end of the line
        size_t length = strlen(buffer);
        if (length > 0 && buffer[length - 1] == '\n') {
            buffer[length - 1] = '\0';
        }

        // Dynamically allocate memory for the line and store it
        lines[*line_count] = malloc((length + 1) * sizeof(char));
        if (!lines[*line_count]) {
            perror("Failed to allocate memory for a line");
            fclose(file);
            return NULL;
        }
        strcpy(lines[*line_count], buffer);

        (*line_count)++;

        // Resize the array if needed
        if (*line_count >= capacity) {
            capacity *= 2;
            char** temp = realloc(lines, capacity * sizeof(char*));
            if (!temp) {
                perror("Failed to resize the array");
                fclose(file);
                return NULL;
            }
            lines = temp;
        }
    }

    fclose(file);
    return lines;
}