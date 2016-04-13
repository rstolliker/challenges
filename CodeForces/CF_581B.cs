// Solution to Codeforces 581 B : Luxourious houses
using System;
using System.Linq;

class CF_581B
{
	public static void Main(string[] args)
	{
		// take input
		int n = int.Parse(Console.ReadLine());
		int[] houses = Array.ConvertAll (Console.ReadLine ().Split (), int.Parse); // magic

		// setup
		int[] result = new int[n];
		int m = houses [n - 1];
		result [n - 1] = 0; // No houses to right, always

		// computations
		for (int i = n - 2; i >= 0; i--)
		{
			int h = houses[i];
			// result[i] = h <= m ? m - h + 1 : 0;	// Nice, but not as through
			if (h <= m)
			{
				result [i] = m - h + 1;
			} else {
				result[i] = 0;
				m = h;
			}
		}

		// output
		Console.WriteLine (string.Join (" ", result));
	}
}