using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

class CF_1a
{
    public static void Main(string[] args)
    {
        string[] commands = Console.ReadLine().Split(' ');
        int n = Convert.ToInt32(commands[0]);
        int m = Convert.ToInt32(commands[1]);
        int a = Convert.ToInt32(commands[2]);
        int wide = (int)Math.Ceiling((decimal)n / a);
        int high = (int)Math.Ceiling((decimal)m / a);
        Console.WriteLine((ulong)wide * (ulong)high);
    }
}
