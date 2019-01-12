// Problem Code: MAXEP
#include <iostream>
using namespace std;

int main()
{
    int N, y = 1, res = 0, c, skip, lg = 0, bad = N;
    cin >> N >> c;
    skip = max(1, N/100);
    while (true)
    {
		if (y >= bad)
		{
			if (skip == 1)
			{
				cout << 3 << " " << bad << endl;		
				break;
			}
			skip /= 10;
			skip = max(1, skip);
			y = min(lg + skip, N);
		}
        cout << 1 << " " << y << endl;
        cin >> res;
        if (res == 0)
        {
            lg = y;
            y += skip;
        }
        else
        {
            if (skip == 1)
            {
                cout << 3 << " " << y << endl;
                break;
            }
            cout << 2 << endl;
            skip /= 10;
            skip = max(1, skip);
            y = min(lg + skip, N);
        }
    }
    cout << 3 << " " << y << endl;
    return 0;
}
