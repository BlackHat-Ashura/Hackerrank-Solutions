#include <stdio.h>


int main() {
    int nums[10] = {0};
    char c;
    while(scanf("%c", &c) == 1) {
        if(c >= '0' && c <= '9') {
            nums[c - '0']++;
        }
    }
    for(int i = 0; i < 10; i++) {
        printf("%d ", nums[i]);
    }
    return 0;
}
