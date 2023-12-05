
using System.Diagnostics;

class SlidingWindowTechnique
{
    public string LargestGoodInteger(string num)
    {
        int first_ptr = 0, last_ptr = 0;
        double result = -1;
        while (last_ptr < num.Length)
        {
            while (last_ptr < num.Length && num[first_ptr] == num[last_ptr])
                last_ptr++;
            if ((last_ptr - 1) - first_ptr >= 2)
                result = result > Char.GetNumericValue(num[first_ptr]) ? result : Char.GetNumericValue(num[first_ptr]);
            first_ptr = last_ptr++;
        }
        return result == -1 ? "" : $"{result}{result}{result}";
    }

    public static void Main(string[] args)
    {

    }
}