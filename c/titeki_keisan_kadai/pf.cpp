/* 台形積分
 *
 * 入力：区間分割数 n
 * 出力：f(x) の a=0 から b=1 までの積分の, n個の台形を用いた近似値
 *
 * アルゴリズム：
 *    1.  積分区間をn個の台形に分解し，それらの面積の合計を計算する。
 *    2.  各threadはこの積分区分数n で並列処理を行う。
 *    3.  計算終了後，計算結果と誤差(真の値との差)をプリントする。
 * 注意:
 *    A. f(x)=x^3, a=0, b=1 は全て固定されている。
 *    B. 精度を考察するため，各threadでの積分は敢えて単精度浮動小数
 *       点数(float)で行い、集計は倍精度浮動小数点数(float)で行う。
 */

/*
 * program usage: $ programname arg1 arg2
 *      arg1: num of trapezoids
 *             recomend from 1,000 to 400,000,000
 *      arg2: num of loops for measure
 *            to get sufficient presition
 *             recomend from 1,000 to 10
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

#define TRUE_VAL 0.25   /* True value of the integral */

int main(int argc, char** argv) {  /* 引数1: 全体の分割数(全体の台形の数) */
                               /* 引数2: 生成するthreadの数 */
    float   a = 0.0;   /* 全積分区間の左端            */
    float   b = 1.0;   /* 全積分区間の右端            */
    int      n;         /* 台形の個数                  */
    float   h;         /* 台形の底辺の長さ            */
    double  error;     /* 誤差                        */

    double  start;     /* 開始時間 (msec)              */
    double  end;       /* 終了時間 (msec)              */
    float   total;     /* 全積分値                     */

    int lp;
    int measure_lp;     /* num of loops for measure     */
    int exec_mode;      /* sequential exec: 0, parallel exec: 1 */

    float Trape(float a, float b, int n, float h, int exec_mode);

    if (argc < 2) {   /* 台形の個数 n の未指定での実行は中断 */
        printf("arg1: Num of trapezoids, arg2: Num of loops for measure\n");
        exit(EXIT_FAILURE);
    }

    n = atoi(argv[1]);
    if (argc < 3)    /* 測定ループ回数未指定の場合は default回数 100 */
           measure_lp = 100;
    else   measure_lp = atoi(argv[2]);

/********** Start of Sequential Execution **********/
    exec_mode = 0;
    printf("Start Sequential trape ....");
    start = omp_get_wtime();

    h = (b-a)/n;                               /* h = 台形1つの幅      */

    for (lp=0 ; lp < measure_lp ; lp++){       /* loop for measurement */

        total = Trape(a, b, n, h, exec_mode);  /* 台形積分の実行       */

    } // endo of loop for measure

    /* end of execution */
    end = omp_get_wtime();
    printf(".... End\n");

    /* 誤差計算 */
    error = total-TRUE_VAL;

    printf("With n = %d trape, integral = %.12f, error = %.12f\n",
                                          n, total, error);
    printf("Elapsted time = %.6f msec\n", (float)(end - start)*1000/measure_lp);

/********** Start of Parallel Execution **********/
    exec_mode = 1;
    printf("\nStart Parallel trape ....");
    start = omp_get_wtime();

    h = (b-a)/n;                               /* h = 台形1つの幅      */

    for (lp=0 ; lp < measure_lp ; lp++){       /* loop for measurement */

        total = Trape(a, b, n, h, exec_mode);  /* 台形積分の実行       */

    } // endo of loop for measure

    /* end of execution */
    end = omp_get_wtime();
    printf(".... End\n");

    /* 誤差計算 */
    error = total-TRUE_VAL;

    printf("With n = %d trape, integral = %.12f, error = %.12f\n",
                                          n, total, error);
    printf("Elapsted time = %.6f msec\n", (float)(end - start)*1000/measure_lp);

    return(0);
}

/* 台形公式
 *
 * 入力：始点 a, 終点 b, 区間分割数 n, 1区間の底辺 h
 * 出力：Trape ... f(x) の a=0 から b=1 までの積分の, n個の台形を用いた近似値
 *
 * Trape(a,b,n,h)=[{f(a)/2+f(a+h)/2}+{f(a+h)/2+f(a+2h)}+ ... +{f(b-h)/2+f(b)/2}]*h
 *               =[f(a)/2+f(a+h)+f(a+2h)+ ... +f(b-h)+f(b)/2]*h
 *               =[{f(a)+f(b)}/2 + {f(a+h)+f(a+2h)+ ... +f(b-h)} ]*h
 */

float Trape(
    float a,         /* 入力: 積分区間の左端 */
    float b,         /* 入力: 積分区間の右端 */
    int    n,         /* 入力: 台形の数 */
    float h,         /* 入力: 台形の幅 */
    int exec_mode)    /* 入力: 逐次実行(0) or 並列実行(1) */

{
    float integral;    /* 積分値 */
    float x;
    int i;
    float f(float x); /* 被積分関数 */

    integral = 0.0;

    if (exec_mode!=0){  /* 並列実行 */


    /* ここを完成させよ  */
        # pragma omp parallel for reduction(+:integral) private(x)
        for (i = 1 ; i <= n-1 ; i++){  /* {f(a+h)+f(a+2h)+ ... +f(b-h)} */
            x = a + i*h;
            integral = integral + f(x);
        }


    }
    else {              /* 逐次実行 */
        for (i = 1 ; i <= n-1 ; i++){  /* {f(a+h)+f(a+2h)+ ... +f(b-h)} */
            x = a + i*h;
            integral = integral + f(x);
        }
    }
    integral = integral + (f(a) + f(b))/2.0;  /* {f(a)+f(b)}/2 */
    integral = integral*h; /* 最後にまとめて 幅h を掛ける */
    return integral;
}

float f(float x){
      /* f(x) を計算する */
    return x*x*x;
}
