#include <stdio.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int maximum = 0;
    int N=0, total=0;
    int arr[10000] = {0,};
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d", &arr[i]);
        if (maximum < arr[i]) {maximum = arr[i];}
    }
    scanf("%d", &total);
    
    int ans = 0;
    int left = 0, right = maximum + 1;

    while (left+1 < right) {
        int mid = (left + right) / 2;
        int t = 0;
        for (int i=0; i<N; i++) {
            t += min(arr[i], mid);
        }
        // printf("%d %d %d %d\n", left, right, mid, t);
        if (t == total) {
            ans = mid;
            break;
        } else if (t > total) {
            right = mid;
        } else if (t < total) {
            left = mid;
            ans = max(ans, mid);
        }
    }
    printf("%d\n", ans);

    return 0;
}