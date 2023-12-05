// See https://aka.ms/new-console-template for more information

string inputpath = "input.txt";

List<string> input = File.ReadLines(inputpath).ToList();

Console.WriteLine("First part: {0}", part1.Solve(input));
Console.WriteLine("Second part: {0}", part2.Solve(input));
