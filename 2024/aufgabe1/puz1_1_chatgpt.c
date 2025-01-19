#include <stdio.h>
#include <stdlib.h>
#include <math.h>  // Für die Funktion abs()

// Funktion zum Vergleichen von zwei Zahlen (für die Sortierung)
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    FILE *file;
    int **array = NULL;  // Dynamisches 2D-Array
    int rows = 0;        // Zähler für die Anzahl der Zeilen
    int capacity = 10;   // Anfangskapazität des Arrays
    int num1, num2;

    // Öffne die Datei im Lesemodus
    file = fopen("puz1_1.txt", "r");
    if (file == NULL) {
        perror("Fehler beim Öffnen der Datei");
        return 1;
    }

    // Allokiere Speicher für das Array (beginnend mit einer Kapazität)
    array = (int **)malloc(capacity * sizeof(int *));
    if (array == NULL) {
        perror("Fehler bei der Speicherzuweisung");
        fclose(file);
        return 1;
    }

    // Lese die Datei Zeile für Zeile
    while (fscanf(file, "%5d %5d", &num1, &num2) == 2) {
        // Wenn die Anzahl der Zeilen die Kapazität überschreitet, Speicher vergrößern
        if (rows >= capacity) {
            capacity *= 2;  // Verdopple die Kapazität
            array = (int **)realloc(array, capacity * sizeof(int *));
            if (array == NULL) {
                perror("Fehler bei der Speichervergrößerung");
                fclose(file);
                return 1;
            }
        }

        // Allokiere Speicher für die beiden Zahlen in jeder Zeile
        array[rows] = (int *)malloc(2 * sizeof(int));
        if (array[rows] == NULL) {
            perror("Fehler bei der Speicherzuweisung für eine Zeile");
            fclose(file);
            return 1;
        }

        // Speichere die eingelesenen Zahlen im Array
        array[rows][0] = num1;
        array[rows][1] = num2;
        rows++;
    }

    // Datei schließen
    fclose(file);

    // Sortiere die beiden Spalten
    int *column1 = (int *)malloc(rows * sizeof(int));
    int *column2 = (int *)malloc(rows * sizeof(int));

    // Spalten in temporäre Arrays kopieren
    for (int i = 0; i < rows; i++) {
        column1[i] = array[i][0];
        column2[i] = array[i][1];
    }

    // Sortiere die beiden Spalten separat
    qsort(column1, rows, sizeof(int), compare);
    qsort(column2, rows, sizeof(int), compare);

    // Berechne die absolute Differenz und summiere sie auf
    int total_diff = 0;
    for (int i = 0; i < rows; i++) {
        total_diff += abs(column1[i] - column2[i]);
    }

    // Gib das Ergebnis aus
    printf("Die summierte absolute Differenz ist: %d\n", total_diff);

    // Speicher freigeben
    free(column1);
    free(column2);
    for (int i = 0; i < rows; i++) {
        free(array[i]);  // Speicher für jede Zeile freigeben
    }
    free(array);  // Speicher für das 2D-Array freigeben

    return 0;
}
