// Problem Code: EVENT
#include <iostream>
using namespace std;

int day_number(string str)
{
    if (str == "saturday")
        return 1;
    else if (str == "sunday")
        return 2; //
    else if (str == "monday")
        return 3;
    else if (str == "tuesday")
        return 4; //
    else if (str == "wednesday")
        return 5;
    else if (str == "thursday")
        return 6;
    else
        return 7;
}
int main()
{
    int T, i, L, R, s, e, dur, count;
    string S, E;
    cin >> T;
    for (i = 0; i < T; ++i)
    {
        count = 0;
        cin >> S >> E;
        s = day_number(S);
        e = day_number(E);
        cin >> L >> R;
        if (e < s)
            dur = 8 - s + e;
        else
            dur = e - s + 1;
        while (dur < L)
            dur += 7;
        while (dur <= R)
        {
            count++;
            if (dur + 7 <= R)
                dur += 7;
        }
        if (count == 0)
            cout << "impossible" << endl;
        else if (count > 1)
            cout << "many" << endl;
        else
            cout << dur << endl;
    }
    
}
