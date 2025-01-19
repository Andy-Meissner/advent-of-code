#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "../common/file.h"
#include <string.h>



int* convert_to_nmbr_arr(char* report, int* reportsize)
{
    int size = 0;
    size_t len = strlen(report);
    int* nbmr_arr = malloc((len / 2) * sizeof(int));

    if (nbmr_arr == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    
    char* token = strtok(report, " ");
    
    while (token != NULL)
    {
        nbmr_arr[size] = atoi(token);;
        size++;
        token = strtok(NULL, " ");
    }
    *reportsize = size;
    return nbmr_arr;
}


bool is_report_safe(int* report, int report_size)
{
    bool is_positive = (report[1] - report[0]) > 0;

    for (int i = 1; i < report_size; i++)
    {
        int diff = report[i] - report[i-1];
        bool diff_positive = diff > 0;

        if (diff_positive ^ is_positive || abs(diff) > 3 ||  abs(diff) < 1)
        {
            return false;
        }
    }

    return true;
}

int* remove_at(int* line, int size, int index)
{    
    int* new_array = malloc((size-1) * sizeof(int));
    for (int i = 0; i < size; i++)
    {
        if (i < index)
        {
            new_array[i] = line[i];
        }
        else if (i > index)
        {
            new_array[i-1] = line[i];
        }

    }

    return new_array;
}

int main() {
    const char* filename = "puz2.txt";
    int line_count;
    char** lines = read_file_lines(filename, &line_count);


    int safe_reports = 0;
    int safe_reports_with_problem_dampener = 0;

    for (int i = 0; i < line_count; i++)
    {
        int reportsize;
        int* report = convert_to_nmbr_arr(lines[i], &reportsize);
        safe_reports += is_report_safe(report, reportsize);

        for (int j = 0; j < reportsize; j++)
        {
            int* small_report = remove_at(report, reportsize, j);

            if (is_report_safe(small_report, reportsize-1))
            {
                safe_reports_with_problem_dampener++;
                break;
            }
            
        }
    }

    printf("Safe reports %d\n", safe_reports);
    printf("Safe reports %d\n", safe_reports_with_problem_dampener);
    return 0;
}