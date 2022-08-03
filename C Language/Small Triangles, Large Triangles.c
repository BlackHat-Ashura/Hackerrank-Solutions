#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

float get_area(triangle tr) {
    float p = (tr.a + tr.b + tr.c)/2.0;
    float s2 = p * (p-tr.a) * (p-tr.b) * (p-tr.c);
    return sqrt(s2);
}

void sort_by_area(triangle* tr, int n) {
    float *areas = (float *)malloc(n * sizeof(float));
    for(int i = 0; i < n; i++) {
        areas[i] = get_area(tr[i]);
    }
    for(int i = 0; i < n-1; i++) {
        int sorted = 1;
        for(int j = 0; j < n-1; j++) {
            if(areas[j+1] < areas[j]) {
                float tmp = areas[j+1];
                areas[j+1] = areas[j];
                areas[j] = tmp;
                triangle tmp_tr = tr[j+1];
                tr[j+1] = tr[j];
                tr[j] = tmp_tr;
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
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
