#include <iostream>
#include <vector>
using namespace std;

int main() 
{
	int x;
	vector<int> ivec;
	while (cin >> x)
		ivec.push_back(x);
	for (int i : ivec)
		if (i == 42)
			break;
		else
			cout << i << endl;
	return 0;
}
