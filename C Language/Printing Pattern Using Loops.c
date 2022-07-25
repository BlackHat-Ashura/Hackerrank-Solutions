#include <stdio.h>


int main() 
{
    int n;
    scanf("%d", &n);
    
    int len = 2*n - 1;
    for(int i = 0; i < len; i++) {
	    for(int j = 0; j < len; j++) {
		    int min1 = i < len-1-i ? i : len-1-i;
		    int min2 = j < len-1-j ? j : len-1-j;
     		    int min = min1 < min2 ? min1 : min2;
                    printf("%d ", n - min);
	    }
    	    printf("\n");
    }
    return 0;
}
