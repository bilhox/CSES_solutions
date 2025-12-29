#include <stdio.h>
#include <stdlib.h>

int a[200001];
int removed[200001];

int main(){

    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) a[i] = i;

    int lastly_removed = 1;
    int removed_count = 0;

    while (removed_count != n){
        for (int i = 1; i <= n; i++){
            if (a[i] == -1) continue;

            if (!lastly_removed){
                removed[removed_count] = a[i];
                a[i] = -1;
                removed_count ++;
            }

            lastly_removed = !lastly_removed;
        }
    }

    for (int i = 0; i < n; i++)
        printf("%d ", removed[i]);

    printf("\n");
    return 0;
}