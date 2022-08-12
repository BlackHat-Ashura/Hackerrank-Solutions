#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b){
    return strcmp(b, a);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int distinct(const char *a) {
        int dist = 0;
        int len = strlen(a);
        int characters[26] = {0};
        for(int i = 0; i < len; i++) characters[a[i] - 'a']++;
        for(int i = 0; i < 26; i++) if(characters[i]) dist++;
        return dist;
    }

   int res = distinct(a) - distinct(b);
    return res ? res : lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    int res = strlen(a) - strlen(b);
    return res ? res : lexicographic_sort(a, b);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int sorted = 0;
    for(int i = 0; i < len-1; i++) {
        sorted = 1;
        for(int j = 0; j < len-1-i; j++) {
            if(cmp_func(arr[j], arr[j+1]) > 0) {
                char *tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
                sorted = 0;
            }
        }
        if(sorted == 1) break;
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
