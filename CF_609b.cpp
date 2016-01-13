#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	unsigned long long int n, m;
	cin >> n;
	cin >> m;

	unsigned long long int genre [m] = {0};
	/* where i is a genre and genre[i]
	is the number of books in that genre */

	long int b;

	for (long int i = 0; i < n; i++)
	{
		cin >> b;
		genre[b - 1] += 1;
	}

	unsigned long long int ans = (n * (n - 1)) / 2;

	for (int j = 0; j < m; j++)
	{
		ans -= (genre[j] * (genre[j] - 1)) / 2;
	}

	cout << ans << endl;

	return 0;
}