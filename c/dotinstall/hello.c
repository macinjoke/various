#include <stdio.h>

/*
ポインタ: アドレスを格納するための変数

値渡し
参照渡し

*/

int main(void)
{
	int *data;
    int average = 0,array[10] = {15,78,98,15,98,85,17,35,42,15};

	for (data = array;data != &array[10];data++) {	/* ここに注目 */
		average += *data;
	}

	printf("%d\n",average / 10);
	return 0;
}
