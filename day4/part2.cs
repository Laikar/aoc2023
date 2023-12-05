public class part2
{
    private static void IncrementCardNum(Dictionary<int, int> cardnums, int cardToIncrement, int amount)
    {
        if (cardnums.ContainsKey(cardToIncrement))
        {
            cardnums[cardToIncrement] += amount;
        }
        else
        {
            cardnums[cardToIncrement] = amount;
        }
    }
    public static int Solve(List<string> input)
    {
        int output = 0;
        Dictionary<int, int> cardCount = new Dictionary<int, int>();
        foreach (string line in input)
        {
    
            string[] split = line.Split("|");
            string cardstring = split.Last();

            int cardId = int.Parse(split.First()
                .Split(":").First()
                .Split(" ").Last());
            string winstring = split.First().Split(":").Last();
            
            List<int> winningNumbers = new List<int>();
            IncrementCardNum(cardCount, cardId, 1);

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
                    score += 1;
                    IncrementCardNum(cardCount, cardId+score, cardCount[cardId]);
                }
            }
            
            output += cardCount[cardId];
        }

        return output;
    } 
}