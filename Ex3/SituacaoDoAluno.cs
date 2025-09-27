using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("\nDigite a nota do aluno:");
			int nota = Convert.ToInt32(Console.ReadLine());
			
			if (nota <= 5) {
			  Console.Write("\nReprovado");
			}
			else if (nota <= 6) {
			  Console.Write("\nEm recuperação");
			}
			else {
			  Console.Write("\nAprovado");
			}
		}
	}
}