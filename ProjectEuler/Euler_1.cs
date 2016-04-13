using System;

namespace euler_1
{
	public class Euler_1
	{
		public static void Main(string[] args)
		{
			Console.WriteLine (sum35 (999));
			Console.ReadLine(); // wait to close window
		}

		public static int sum35(int n)
		{
			if (n < 3)
			{
				return 0;

			} else if((n % 3 == 0) || (n % 5 == 0))
			{
				return n + sum35 (n - 1);  // yay recursion
			} else {
				return sum35(n - 1);
			}
		}
	}
}

