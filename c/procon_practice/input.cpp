#include<iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int x[N];
    int i = 0;
    for(i=0; i < N; i++) {
        cin >> x[i];
        // if (x == 0) break;
        cout << "Case " << i << ": " << x << endl;
    }
    return 0;
}
