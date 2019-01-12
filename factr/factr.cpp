#include <iostream>
#include <vector>
using namespace std;

int Z(int N)
{
	int total = 0;
	while (N != 0)
	{
		N /= 5;
		total += N;
	}
	return total;	
}

int main()
{
	int num_cases;
	cin >> num_cases;
	vector<int> ivec;
	for (int i = 0; i < num_cases; ++i)
	{
		int x;
		cin >> x;
		ivec.push_back(x);
	}
	for (int num : ivec)
		cout << Z(num) << endl;
	return 0;
}	
