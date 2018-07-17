#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

double Trape(       //積分計算
    double a,      /* 入力: 積分区間の左端 */
    double b,      /* 入力: 積分区間の右端 */
    int n,         /* 入力: 台形の数 */
    double h     /* 入力: 台形の幅 */
    )
    {

    double integral; /* 積分値 */
    double x;
    int i;
    double f(double x); /* 被積分関数 */

    integral = 0.0;

    for (i = 1; i <= n - 1; i++)
        {  /* {f(a+h)+f(a+2h)+ ... +f(b-h)} */
            x = a + i * h;
            integral = integral + f(x);
        }
    integral = integral + (f(a) + f(b)) / 2.0; /* {f(a)+f(b)}/2 */
    integral = integral * h;                   /* 最後にまとめて 幅h を掛ける */
    return integral;
}

double f(double x)      //x^3計算
{
    return x * x * x;
}

int main(int argc, char **argv)
{
    double a = 0.0; /* 全積分区間の左端            */
    double b = 1.0; /* 全積分区間の右端            */
    int n = 100000;   /* 台形の個数                 */
    double h;       /* 台形の底辺の長さ            */
    double myres;   //プロセスごとの積分結果
    double res;     //myresの合計値
    double share;   //分担する積分区間の大きさ
    int num_PE;     //PE数
    int myid;       //各プロセスのランク

    h = (b - a) / n;    //分割された台形幅

    MPI_Init(&argc, &argv);     //全プロセス初期化
    MPI_Comm_size(MPI_COMM_WORLD, &num_PE); //num_PEにPE数
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);   //myidにランク

    n = n / num_PE;     //プロセスごとの台形の個数
    share = (b - a) / num_PE;   //積分区間をプロセス数で割って各区間の大きさ

    if (share == 0){
        res = 0;
    }
    else{
        a = myid * share;   //idごとに担当する区間を割り振る
        b = a + share;
        myres = Trape(a, b, n, h); /* 台形積分の実行       */

        //各プロセスの担当区間、積分値、idを表示
        printf("x = %lf ~ %lf sum is %lf, id = %d.\n", a, b, myres, myid);

        //各プロセスで求めた積分値を合計
        MPI_Reduce(&myres, &res, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    }

    if (myid == 0){
        printf("The sum is %lf.\n", res);
    }

    MPI_Finalize();
}
