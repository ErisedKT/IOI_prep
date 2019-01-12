#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int min(int a[], int size)
{
	int x = a[0];
	for (int i = 0; i < size; ++i)
		if (a[i] < x)
			x = a[i];
	return x;	
}
int main()
{	
	int T;
	cin >> T;
	int min_diffs[T];	
	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		int diff[N-1], a[N];
		for (int j = 0; j < N; ++j)
			cin >> a[j];
		sort(a, a+N);
		for (int k = 0; k < N-1; ++k)
			diff[k] = abs(a[k+1] - a[k]);
		min_diffs[i] = min(diff, N-1);
	}
	for (auto diff : min_diffs)
		cout << diff << endl;
	return 0;
}
