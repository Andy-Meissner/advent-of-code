#include <stdio.h>
#include <ctype.h> 
#include <stdlib.h> 

int convert_str_to_number(int* arr)
{    
    int num = 0;

    for (int i = 0; i < 5; i++) {
        num = num * 10 + (arr[i] - '0'); // '0' konvertiert das Zeichen zur Ziffer
    }
    return num;
}

void sort_array(int* array_ref, int arr_len)
{
    char matched = 1;

    while (matched == 1) {
        matched = 0;
        for (int i = 0; i < arr_len-1; i++)
        {
            int temp;
            if (array_ref[i] > array_ref[i+1])
            {
                temp = array_ref[i];
                array_ref[i] = array_ref[i+1];
                array_ref[i+1] = temp;
                matched = 1;
            }
        }
    }
}


int partition(int* array_ref, int lower_bound, int upper_bound)
{
    int pivot = array_ref[upper_bound];
    
    int i = lower_bound -1;

    for (int j = lower_bound; j < upper_bound; j++)
    {
        if (array_ref[j] <= pivot)
        {
            i++;
            int temp = array_ref[j];
            array_ref[j] = array_ref[i];
            array_ref[i] = temp;
        }
    }

    int temp = array_ref[i+1];
    array_ref[i+1] = pivot;
    array_ref[upper_bound] = temp;

    return i+1;
}

void quicksort(int* array_ref, int lower_bound, int upper_bound)
{
    if (lower_bound < upper_bound)
    {
        int pivot_index = partition(array_ref, lower_bound, upper_bound);
        quicksort(array_ref, lower_bound, pivot_index-1);
        quicksort(array_ref, pivot_index+1, upper_bound);
    }
}

int main() {
    FILE *file;

    file = fopen("puz1_1.txt", "r");

    int no_of_blocks = 1;
    int array_size = 500;

    int *left_arr = calloc(array_size, sizeof(int));
    int *right_arr = calloc(array_size, sizeof(int));

    int ch; // `int`, da EOF (End of File) auch geprüft wird
    int line_ctr = 0;

    int number_max_length = 5;
    int next_number[number_max_length];

    int current_number_length = 0;
    char left_right_toggle = 0;

    while ((ch = fgetc(file)) != EOF) {
        if (isdigit(ch))
        {
            next_number[current_number_length] = ch;
            current_number_length++;
        }
        if (current_number_length == number_max_length)
        {
            if (left_right_toggle == 0)
            {
                left_arr[line_ctr] = convert_str_to_number(next_number);
                left_right_toggle = 1;
            }
            else
            {
                right_arr[line_ctr] = convert_str_to_number(next_number);
                line_ctr++;
                left_right_toggle = 0;
            }
            current_number_length = 0;
        }
        
        if (line_ctr == no_of_blocks * array_size)
        {
            no_of_blocks++;
            left_arr = (int *)realloc(left_arr, no_of_blocks * array_size * sizeof(int));
            right_arr = (int *)realloc(right_arr, no_of_blocks * array_size * sizeof(int));
        }
    }

    quicksort(left_arr, 0, line_ctr-1);
    quicksort(right_arr, 0, line_ctr-1);

    int final_sum = 0;

    for (int i = 0; i < line_ctr; i++)
    {
        final_sum += abs(left_arr[i] - right_arr[i]);
    }

    printf("Das Ergebnis ist %d\n", final_sum);

    final_sum = 0;
    for (int i = 0; i < line_ctr; i++)
    {
        int search_nr = left_arr[i];
        int occurrences = 0;
        for (int j = 0; j < line_ctr; j++)
        {
            if (right_arr[j] > search_nr)
            {
                break;
            }
            if (right_arr[j] == search_nr)
            {
                occurrences++;
            }
        }
        final_sum += search_nr * occurrences;
    }

    printf("Das Ergebnis ist %d\n", final_sum);
    free(left_arr);  
    free(right_arr);  
    return 0;
}
