#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h> // For strlen

char* get_keyword(char ch, char** keywords, size_t keywords_len, int keywords_ctrs[])
{
    for (int i = 0; i < keywords_len; i++)
    {
        size_t keyword_len = strlen(keywords[i]);
        if (ch == keywords[i][keywords_ctrs[i]])
        {
            keywords_ctrs[i]++;
        }
        else
        {
            keywords_ctrs[i] = 0;
        }
        if (keywords_ctrs[i] == keyword_len)
        {
            return keywords[i];
        }
    }
    return NULL;
}

int main()
{
    FILE* file = fopen("puz3.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(-1);
    }

    char* keywords[] = {"mul(", "do(", "don't("};
    size_t length = sizeof(keywords) / sizeof(keywords[0]);
    int keyword_ctrs[] = {0,0,0};
    
    char* active_keyword = NULL;
    int sum = 0;
    int sum2 = 0;
    char ch;
    char nr1[4];
    char nr2[4];


    int nr_len = 0;
    bool sep = false;
    bool do_active = true;


    while ((ch = fgetc(file)) != EOF) { // Read one character at a time
        if (active_keyword == NULL)
        {
            active_keyword = get_keyword(ch, keywords, length, keyword_ctrs);
            continue;
        }
        if(active_keyword == "mul(" && isdigit(ch) && nr_len < 3)
        {
            if (sep)
            {
                nr2[nr_len] = ch;
            }
            else
            {
                nr1[nr_len] = ch;
            }
            nr_len++;
            continue;
        }
        if(ch == ',' && nr_len > 0)
        {
            sep = true;
            nr1[nr_len] = '\0';
            nr_len = 0;
            continue;
        }
        if (ch == ')')
        {
            if (active_keyword == "mul(")
            {
                if(sep && nr_len > 0)
                {
                    nr2[nr_len] = '\0';
                    int one = atoi(nr1);
                    int two = atoi(nr2);
                    sum += one * two;
                    
                    if(do_active)
                    {
                        sum2 += one * two;
                    }
                }
            }
            if (active_keyword == "do(")
            {
                do_active = true;
            }  
            if (active_keyword == "don't(")
            {
                do_active = false;
            } 

            for (int i = 0; i < length; i++)
            {
                keyword_ctrs[i] = 0;
            }
            active_keyword = NULL;
            nr_len = 0;
            sep = false;     
        }
        for (int i = 0; i < length; i++)
        {
            keyword_ctrs[i] = 0;
        }
        active_keyword = NULL;
        nr_len = 0;
        sep = false; 
    }

    printf("Sum is %d\n", sum);

    printf("Sum2 is %d\n", sum2);
    fclose(file); // Close the file when done
    return 0;
}