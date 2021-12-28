import java.util.ArrayList;
import java.util.Arrays;
import java.math.BigInteger;
import java.time.LocalDate;
/**
*  Glorious Lab Practical on Java
*/
public class LP1
{
    /** 
     * This computes  the sum of a list of BigIntegers
     * @param a an array list of BigIntegers
     * @return the sum of the BigIntegers in a
     */
    public static BigInteger sum(ArrayList<BigInteger> a) //works
    {   
        BigInteger out = BigInteger.ZERO;
        for(int k = 0; k < a.size(); k++)
        {
            out = out.add(a.get(k));
        }
        return out;
    }   
	/**
	* This plucks out entries of a string at indices divisible by p.
    * in a string.  
    * @param s a string
    * @param p a nonnegative integer.  
    * @return a string that has entries p, 2p, 3p,   etc of the
    * string s.
    *  Examples:
    * aerate("aardwolf" 2) -&gt; "arwl"
    * aerate("bacchanalia" 3) -&gt; "bcni"
    */    
	public static String aerate(String s, int p) //works
	{
        String out = "";
        for (int i=0; i<s.length(); i++)
        {
            if (i%p == 0)
            {
                out += s.charAt(i);
            }
        }
        return out;
	}
    /**
     * This makes a string echoy.  See the example
     * @param s is a string
     * @return a string with the nth character repeated n times.  
     * example:  echoy("cowpie") &rarr; coowwwppppiiiiieeeeee
     * if the string passed is empty, return an empty string
     */
    public static String echoy(String s) //works
    {
        String out = "";
        for (int i=0; i<s.length(); i++)
        {
            for (int j = 0; j < i +1; j++)
            {
                out += s.charAt(i);
            }
        }
        return out;
    }
    /** 
     * This computes the product of the non-zero elements of
     * a and returns the sum of its digits.
     * @param a an array list
     * @return the sum of the digits in the product of the 
     * non-zero entries in a
     */
    public static int  finger(ArrayList<BigInteger>  a)  //works
    {   
        BigInteger product = BigInteger.ONE;
        for(int k = 0; k < a.size(); k++)
        {
            if (a.get(k).compareTo(BigInteger.ZERO) != 0)
            {
                product = product.multiply(a.get(k));
            }
        }
        String bigstring = product.toString();
        int sum = 0;
        for (int i = 0; i < bigstring.length(); i++ )
        {
            sum += bigstring.charAt(i) - '0';
        }
        return sum;
    }   
    /**
     * This filters strings for a specified substring
     * @param al is an array list of strings.
     * @param s is a search string
     * @return an array list of striings containing all those strings
     * in the array list <code>al</code> having <code>s</code> as a substring.
     */
     public static ArrayList<String> pseudoGrep(ArrayList<String> al, String s) 
     {
        ArrayList <String> out = new ArrayList<String>(); 
        for (int i=0; i<al.size(); i++)
        {
            if (al.get(i).contains(s))
            {
                out.add(al.get(i));
            }
        }
         return out;
     }
    /**
    *  This finds the date n days from today.  If n is negative
    *  find the date -n days ago.
    *  @param n the number of days from today
    *  @return the date n days from today.  
    *  Sample:  10000 days from this lab prac is 29 March 2049.
    *  Today is 11 November 2021
    *  Sample:  10000 days ago is 1994-06-26
    */
    public static LocalDate daysFromNow(int n) //Works
    {
        //Dr. Morrison if i dont get to this one its cuz I was lazy lolol 
        // okay so i did get to this one but this library is weirddddd and coool 
        // OHH i use the current dateeee okayyyyy 
        // Dr. Morrison imma use local date now() which gives the current local date right now 
        LocalDate today = LocalDate.now();
        Long todayEPOCH = today.toEpochDay();
        todayEPOCH += n;
        LocalDate out = LocalDate.ofEpochDay(todayEPOCH);
        return out;
    }
    /** 
    *  Here is your testing ground.
    *  @param args command-line arguments. You won't have any.
    */
    public static void main(String[] args)
    {
        System.out.println("___Testing sum____");
        ArrayList<BigInteger> nums = new ArrayList<>();
        nums.add(BigInteger.ONE);
        nums.add(BigInteger.valueOf(2));
        nums.add(BigInteger.valueOf(3));
        nums.add(BigInteger.valueOf(4));
        nums.add(BigInteger.valueOf(5));
        System.out.println(nums.toString());
        System.out.println(sum(nums));
        System.out.println("___Testing aerate____");
        System.out.println(aerate("aardwolf", 2));
        System.out.println(aerate("bacchanalia", 3));
        System.out.println("___Testing echoy____");
        System.out.println(echoy("cowpie"));
        System.out.println("___Testing finger____");
        nums.add(BigInteger.ZERO);
        System.out.println(finger(nums));
        System.out.println("___Testing PseudoGrip____");
        ArrayList<String> words = new ArrayList<>();
        words.add("hello");
        words.add("helloo");
        words.add("hello");
        System.out.println(pseudoGrep(words, "loo").toString());
        System.out.println("___Testing daysfromNOw____");
        System.out.println(daysFromNow(0));    
        System.out.println(daysFromNow(2));
        System.out.println(daysFromNow(-2));    
    }
}