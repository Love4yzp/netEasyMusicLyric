#include <stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{
    const char *p[]={"Jan","Feb","May","Apr"};
    int num = atoi(argv[1]);
    printf("%s\n",*(p+num-1));

    return 0;
}
