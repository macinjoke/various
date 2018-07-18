// MPIを用いて計算を行う
// 実行環境
// macOS High Sierra
// 3.3 GHz Intel Core i7 2コア/4スレッド, メモリ16GB
// openmpi
// コンパイル、起動コマンド
// $ mpic++ pd_mpi.cpp && mpirun -np 2 a.out
// -np 2 の部分でプロセッサー数を指定している。
// MPI_Init をすることで並列処理が走り、MPI_Reduceでそれぞれのプロセスが計算した積分値を合計している

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    double a = 0.0; /* 全積分区間の左端            */
    double b = 1.0; /* 全積分区間の右端            */
    int n = 100000; /* 台形の個数                 */
    double h;       /* 台形の底辺の長さ            */
    double size;    //それぞれの積分区間のサイズ
    double each_result;   //プロセスごとの積分結果
    double result;  //合計値
    int num_PE;     //プロセッサーの数
    int rank;       //ランク
    int nn;         //プロセスごとの台形の個数

    h = (b - a) / n;    //分割された台形幅

    double Trape(double a, double b, int n, double h);

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_PE);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    nn = n / num_PE;
    size = (b - a) / num_PE;
    if (size == 0){
        result = 0;
    }
    else{
        a = rank * size;   //idごとに担当する区間を割り振る
        b = a + size;
        each_result = Trape(a, b, nn, h);

        //それぞれのプロセスの担当区間と積分値、rankを表示
        printf("x: %lf ~ %lf, sum: %lf, rank: %d.\n", a, b, each_result, rank);

        //それぞれのプロセスで求めた積分値を合計
        MPI_Reduce(&each_result, &result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);
    }

    if (rank == 0) {
        printf("Total sum: %lf.\n", result);
    }

    MPI_Finalize();
}

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

    for (i = 1; i <= n - 1; i++) {  /* {f(a+h)+f(a+2h)+ ... +f(b-h)} */
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

