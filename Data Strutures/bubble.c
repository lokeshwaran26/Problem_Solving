#include <stdio.h>
int main()
{
    int arr[] ={2, 6, 5, 1, 3, 4};
    int sorted = 1, i;
    int n = sizeof(arr)/sizeof(arr[0]);
    while (sorted)
    {
        sorted = 0;
            for (i = 0; i < n; i++)
            {
                if (arr[i] > arr[i + 1]){
                    sorted = 1;
                    arr[i], arr[i + 1] = arr[i + 1], arr[i];
            }
            }
        
        
    };

    for (i = 0; i < n; i++)
    {
        printf("%d", arr[i]);
    }
}