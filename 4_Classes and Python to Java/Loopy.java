import java.util.ArrayList;
import java.util.Arrays;
import java.lang.reflect.Array;
import java.math.BigDecimal;
import java.math.BigInteger;
public class Loopy
{
    public static void main(String[] args)
    {
        //test your stuff here.
    }
    /**
     * produce a table of values for the square function starting
     * at start, ending before end, and whhich increments the x-value
     * by increment. Return this in a string.
     */
    public static String tableOfSquares(double start, double end, double increment)
    {
        ArrayList<Double> values = new ArrayList<Double>();
        for (int i=(int)start; i < (int)end; i++ )
        {
            Double num = Math.pow(i, increment);
            values.add(num);
        }

        return values.toString();
    }
    /**
     * @param roster a list of email names
     * @return an ArrayList of names in the first half of the alphabet, case insensitive
     */
    public static ArrayList<String> firstHalf(ArrayList<String> roster)
    {
        ArrayList<String> output = new ArrayList<String>();
        for (int i = 0; i < roster.size(); i++) {
            String s = roster.get(i).toLowerCase();
            String a = "a";
            if (a.compareTo(s) > -12)
            {
                output.add(roster.get(i));
            } 
          }
        
        return output;
    }
    /**
     * @param roster a list of email names
     * This has the side-effect of filtering in all elements in the
     * first half of the alphabet, case insensitive.
     */
    public static void firstHalfInPlace(ArrayList<String> roster)
    {
    }
    /**
     * @param n the size of the population
     * @param k the size of the sample
     * @return the number of ordered samples of size k 
     * in the population. This is n(n-1)(n-2).....  (n-k+1).
     */
    public static BigInteger permutations(int n, int k)
    {
        /*double last = 1;
        for (int i = 0; i < k + 1; i++)
        {   
            double num = (double)(n-i);
            last *= num;

        }
        BigInteger output = BigDecimal.valueOf(last).toBigInteger();
        */
        BigInteger output = BigInteger.ONE;
        for (int i = 0; i < k; i++)
        {
            output = output.multiply(BigInteger.valueOf(n-i));
        }
        return output;
    }
    /**
     * @param n the size of the population
     * @param k the size of the sample
     * @return the number of ordered samples of size k 
     * in the population. This is 
     * n(n-1)(n-2).....  (n-k+1)/k!.
     * Be smart:  the product  of any k consecutive integers
     * is divisible by k.  You should be able to compute
     * choose(1000000000, 3).  hint: ZIPPER
     */
    public static BigInteger choose(int n, int k)
    {
        BigInteger output = BigInteger.ONE;
        /*num = permutations(n,k);
        int res = 1;
        for (int i = k; i >= 0; i = i-1)
        {
            num = num.multiply();
        }
        BigInteger num2 = BigInteger.valueOf(res);
        */
        for (int i = 0; i < k; i++)
        {
            output = output.multiply(BigInteger.valueOf(n-i)).divide(BigInteger.valueOf(i+1));
        }
         
        return output;
    }
}