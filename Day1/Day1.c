#include <stdlib.h>
#include <stdio.h>

int main(){
    FILE *filePointer;
    filePointer = fopen("adventofcode.com_2023_day_1_input.txt", "r");

    char myString[255];

    if (filePointer != NULL)
    {
        while (fgets(myString,255, filePointer))
        {
            int value1 = 0;
            int value2 = 0;
            int stringLen = sizeof(myString);
            printf("%s", stringLen);
            for (int i = 0; i < stringLen; i++)
            {
                printf("%s", myString[i]);
            }
            break;
        }
        
    }
    else{
        printf("Not able to open the file.");
    }
    
    fclose(filePointer);
    getchar();
    return 0;
}
