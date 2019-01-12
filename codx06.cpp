#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int T, i;
	for (i = 0; i < T; ++i)
	{
		long long N, S, k, j, A[100000], sum = 0;
		cin >> N;
		cin >> S >> k;
		for (j = 0; j < N; ++j)
		{
			cin >> A[j];
			sum += A[j];
		}
		if (sum >= S)
		{
			cout << 0 << endl;
			continue;
		}
		else
		{
			double val = (S - sum)/(double) k;
			cout << ceil(val) << endl;
		}
	}
	return 0;
}

