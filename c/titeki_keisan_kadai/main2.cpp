/* Sample Program for OpenMP                        */
/*   usage: $ programname arg1 arg2                 */
/*      arg1: arraysize                             */
/*             recommend from 10,000 to 100,000,000  */
/*      arg2: num of loops for measure              */
/*            to get sufficient presition           */
/*             recommend from 1,000 to 100           */

# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <omp.h>

int main (int argc, char** argv) {

    int i, lp;
    int procs;
    long int res;
    int* data;

    double start, end;      /* start time, end time */

    int array_size;         /* size of array */
    int measure_lp;         /* num of loops for measure */

    array_size = 100000;
    printf("array size = %u\n", array_size);

    data = (int *)malloc(sizeof(int) * array_size);  /* array allocation */
    if(data == NULL) {
        printf("Error: Can not allocate memory\n");
        exit(EXIT_FAILURE);
    }

    measure_lp = 100;   /* set num of loops for measurement */

    for (i = 0; i < array_size; i++){
        data[i] = i % 7;    /* data[] can be anything */
//        printf("%d\n", data[ i ]);
    }

    printf("# of loops for measure = %d\n\n", measure_lp);

// start of Sequential execution

//    printf("Start ....");
    start = omp_get_wtime();

    for (lp=0; lp < measure_lp; lp++){ // loop for measurement
        res = 0;
        for (i=0; i<array_size; i++){
            res += data[ i ];
        }

    } // end of loop for measurement

    end = omp_get_wtime();
//    printf(".... End\n");

//    printf ("The sum is %u\n", res) ;
    double sequential_time = (end - start) / measure_lp;
//    printf ("Sequential execution (CPU time in msec) = %10.10f\n\n", (sequential_time)/measure_lp);
    printf ("%10.10f\n", (sequential_time)/measure_lp);

// start of Parallel execution

    procs = omp_get_num_procs();
//    printf("# of processors = %d\n", procs);

//    printf("Start ....");
    start = omp_get_wtime();

    for (lp=0; lp < measure_lp; lp++){ // loop for measurement
        res = 0;
# pragma omp parallel for reduction(+:res) // num_threads(1) /* for serial execution */
        for (i=0; i<array_size; i++){
            res += data[ i ];
        }

    } // end of loop for measurement

// end of measurement

    end = omp_get_wtime();
//    printf(".... End\n");

//    printf ("The sum is %u\n", res) ;
    double parallel_time = (end - start) / measure_lp;
//    printf ("  Parallel execution (CPU time in msec) = %10.10f\n", (parallel_time)/measure_lp);
    printf ("%10.10f\n\n", (parallel_time)/measure_lp);

    double result = sequential_time / parallel_time;
    printf("%10.10f\n", result);

    free(data);
    return(0);
}
