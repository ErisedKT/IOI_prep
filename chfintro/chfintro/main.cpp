// Problem Code: CHFINTRO
#include <iostream>
using namespace std;

int main()
{
    int N, r, R;
    cin >> N >> r;
    while (cin >> R)
    {
        if (R >= r)
            cout << "Good boi" << endl;
        else
            cout << "Bad boi" << endl;
    }
    return 0;
}
