#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char **s, int x, int y) {
	char *tmp = s[x];
	s[x] = s[y];
	s[y] = tmp;
}

void reverse(char **s, int start, int end) {
	while(start < end) {
		swap(s, start, end);
		start++;
		end--;
	}
}

int next_permutation(int n, char **s)
{
	int i, pivot = -1;
	for(i = n-1; i > 0; i--) {
		if(strcmp(s[i], s[i-1]) > 0) {
			pivot = i-1;
			break;
		}
	}
	if(pivot == -1) return 0;
	for(i = n-1; i > pivot; i--) {
		if(strcmp(s[i], s[pivot]) > 0) {
			swap(s, i, pivot);
			break;
		}
	}
	reverse(s, pivot+1, n-1);
	return 1;
}

int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}
