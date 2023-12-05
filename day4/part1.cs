public class part1
{
    public static int Solve(IEnumerable<string> input)
    {
        int output = 0;
        foreach (string line in input)
        {
    
            string[] split = line.Split("|");
            string cardstring = split.Last();
            string winstring = split.First().Split(":").Last();
            List<int> winningNumbers = new List<int>();
            foreach (string unparsedNum in winstring.Split(" "))
            {
                int num;
                if (int.TryParse(unparsedNum, out num))
                {
                    winningNumbers.Add(num);
                }
            }

            int score = 0;
            foreach (string unparsedNum in cardstring.Split(" "))
            {
                int num;
                if (int.TryParse(unparsedNum, out num) && winningNumbers.Contains(num))
                {
                    score = (score == 0) ? 1 : score*2;
                }
            }

            output += score;
        }

        return output;
    } 
}
