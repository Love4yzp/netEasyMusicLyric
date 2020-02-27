#include <stdio.h>
#include <stdlib.h>
int main(int argc,char *argv[])
{
        double unitPrince = 3.5;
        double discount1 = 0.05;
        double discount2 = 0.1;
        double discount3 = 0.15;
        double total_price = 0.0;
        int quantity = 0;

    if (argc ==2)
    {
        quantity =atoi(argv[1]);
    }


       total_price = quantity*unitPrince*( 1.0-(quantity>50?discount3:(quantity>20?discount2:(quantity>10?discount1:0.0))));
       printf("%5.2lf\n",total_price);


       return 0;
}

