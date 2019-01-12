#include <iostream>
using namespace std;

int main()
{
	unsigned A, B, diff;
	cin >> A >> B;
	diff = A - B;
	unsigned new_diff = diff - (diff % 10);
	if (new_diff + 1 != diff)
		cout << new_diff + 1 << endl;
	else
		cout << new_diff + 2 << endl;
	return 0;
}

