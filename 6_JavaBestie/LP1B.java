import java.util.ArrayList;
import java.math.BigInteger;
import java.util.Collections;
import java.util.Arrays;
/*
 * Useful hints:
 * You can use the static service class Arrays if you wish.  
 * It's java.util.Arrays.   It can be handy.
 * Arrays has a static service method for sorting
 *
 * to split as in python, use .split("\\s+") on the string you wish
 * to split on whitespace
 *
 * Collections.sort() will sort an arraylist in place.
 * Arrays.sort() will sort an array in place.
 * 
 * DO NOT COMPARE DOUBLES FOR EQUALITY!!!
 * Use the function closeEnough I have provided for free.  It will
 * work nicely here.  Just use closeEnough(a, b) instead of a == b.
 */
public class LP1B
{
    /**
     * This is our tolerance for fuzziness in checking equality of doubles.
     */
    public static final double TINY = 1e-6;
    /** 
     * Da main
     */
    public static void main(String[] args)
    {   
        //use this for any test code.  You WANT to write test code.
        System.out.println(prepareAnagram("Mississippi").equals("iiiimppssss"));
        System.out.println(initially("Eat my shorts").equals("EMS"));
        System.out.println(isAFactorial(BigInteger.valueOf(720)));
        System.out.println(isAFactorial(BigInteger.valueOf(5040)));
        System.out.println(!isAFactorial(BigInteger.valueOf(59)));

    }   
    /**
     * free function to compare doubles for near equality.
     * @param a one double to be compared
     * @param b another double to be compared
     * @return true if Math.abs(a - b) &lt; 1e-6.
     */
    public static boolean closeEnough(double a, double b)
    {
        return Math.abs(a - b) < TINY;
    }
	/**
	* This lower-cases a string of letters, and returns a new string
    * with its characters sorted in alphabetical order 
    * @param s a string 
    * @return a string containing the letters of s in alphabetical 
    * order.
	*/
	public static String prepareAnagram(String s)
	{
        s = s.toLowerCase();
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
	}
	/**
    * This takes a string consisting of letters and returns a string containing
    * all of the first letters of the words in the string.
    * @param s a string
    * @return a string containing the first letters of S in upper-case
	*/
	public static String initially(String s)
	{
        s = s.toUpperCase();
        String[] words = s.split("\\s+"); // same as python's .split()
        StringBuffer out = ""
        for(String q: words)
        {
            out.append(q[0]);
        }
        return out.toString();
	}
    public static BigInteger factorial(int n)
    {
        BigInteger out = BigInteger.ONE;
        for(int k = 1; k <= n; k++)
        {
            out = out.multiply(BigInteger.valueOf(k));
        }
        return out;
    }
    /**
     * This tests to see if a BigInteger is the factorial of some positive integer.
     * @param b a BigInteger
     * @return true if b is the factorial of some nonnegative integer n.
     */
	public static boolean isAFactorial(BigInteger b)
	{
        int k = 1;
        while(factorial(k).compareTo(b) < 0)
        {
            k++;
        }
        return b.equals(factorial(k));
	}
    /**
     * This lops the largest and smallest entries off an ArrayList of doubles
     * and, averages the rest, and returns that average.
     * @param a is an ArrayList of Doubles
     * @param trimmed is an even nonnegative integer.  As a precondition,
     * 2*timmmed &lt; a.size().  This is the total number of entries to be
     * trimmed off.
     * @return the mean of the values in the array list with the 
     * smallest trimmed/2 and largest trimmed/2 elements removed.
     */
	public static double trimmedMean(ArrayList<Double> a, int trimmed)
	{
        Collections.sort(a);
        int lop = trimmed/2;
        double total = 0;
        for(int k = lop; k < a.size() - lop; k++)
        {
            total += a.get(k);
        }
        return total;
	}
    /**
     * This creates a letter-frequency table for a string in the form of an
     * ArrayList.  Note that the letter frequencies are relative to the number
     * of <em>alphabetical</em> characters. All non-alpha characters are ignored.
     * @param s is a string
     * @return The relative frequency of each letter in the alphabet
     * in an array list of Doubles, where the frequency for 'a' is stored at
     * entry 0, 'b' is stored at entry 1, usw.  This should be case insensitive.
     * The relative frequency should ignore all non-alpha characters.
     */
    public static ArrayList<Double> charFreq(String s)
    {
        ArrayList<Double> freqTable = new ArrayList<>();
        for(int k = 0; k < 26; k++)
        {
            freqTable.add(0.0);
        }
        s = s.toLowerCase();
        int chocula = 0;
        for(int k = 0; k < s.length(); k++)
        {
            char ch  = s.charAt(k);
            if(Character.isAlphabetic(ch))
            {
                int gap = ch - 'a';
                freqTable.set(gap, 1 + freqTable.get(gap));
                chocula++;
            }
        }
        for(int k = 0; k < freqTable.size(); k++)
        {
            freqTable.set(k, freqTable.get(k)/chocula);
        }
        return freqTable;
        }
    }
    /**
     * This finds the number of times a specified digit
     * appears in decimal representation of n!
     * This should work for 10000!.
     * @param n is a nonnegative integer
     * @return the number of times the digit <code>digit</code>
     * appears in the decimal representation of n!
     */
    public static int factorialDigit (int n, int digit)
    {
        String facString = factorial(n).toString();
        int out = 0;
        for(int k = 0; k < facString.length(); k++)
        {
            if((int)facString.charAt(k) - (int)'0' == digit)
            {
                out++;               
            }
        }
        return out;
    }
}
