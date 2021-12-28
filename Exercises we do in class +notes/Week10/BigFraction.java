package Week10;

/**
 * This is a class of immutible object that support extended-precision
 * rational arithmetic.  All of the usual arithmetic operations are
 * supported.
 */
import java.math.BigInteger;
public class BigFraction
{
    /**
     * This is the BigFraction 0/1
     */
    public final static BigFraction ZERO;
    /**
     * This is the BigFraction 0/1
     */
    public final static BigFraction ONE;
    /**
     * This is the BigFraction 1/2
     */
    public final static BigFraction HALF;
    //static block.
    static 
    {
        ZERO = new BigFraction();
        ONE = BigFraction.valueOf(1,1);
        HALF = BigFraction.valueOf(1,2);
    }

    private final BigInteger num;
    private final BigInteger denom;
    /**
     * This creates a BigFraction with the specified numerator and 
     * denominator
     * @param num this is the numerator we are specifying
     * @param denom this is the denominator we are specifying
     */
    public BigFraction(BigInteger num, BigInteger denom)
    {
        if(denom.equals(BigInteger.ZERO))
        {
            throw new IllegalArgumentException();
        }
        BigInteger d = denom.gcd(num);
        num = num.divide(d);
        denom = denom.divide(d);
        if(denom.compareTo(BigInteger.ZERO) < 0)
        {
            num = num.negate();
            denom = denom.negate();
        }
        this.num = num;
        this.denom = denom;
    }
    /**
     * This creates the BigFraction 0/1, which is the same as BigFraction.ZERO.
     */
    public BigFraction()
    {
        this(BigInteger.ZERO, BigInteger.ONE);
    }
    /**
     * This gives a string represention of the form numerator/denominator.
     * @return a string representation of the form numerator/denominator.
     */
    @Override
    public String toString()
    {
        return String.format("%s/%s", num, denom);
    }
    /**
     * This checks if this BigFraction has the same numerical value as
     * the object o.
     * @param o the object we are comparing this BigFraction to.
     * @return true if o is a BigFraction and if it is numerically
     * equal to this BigFraction
     */
    @Override
    public boolean equals(Object o)
    {
        if(o == this)
        {
            return true;
        }
        //species test
        if( !(o instanceof BigFraction))
        {
            return false;
        }
        BigFraction that = (BigFraction) o;
        return num.equals(that.num) && denom.equals(that.denom);
    }
    /**
     * This computes this + that.
     * @param that the BigFraction we are adding this BigFraction to.
     * @return this + that
     */
    public BigFraction add(BigFraction that)
    {
        BigInteger top = num.multiply(that.denom).add(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    /**
     * This computes this - that.
     * @param that the BigFraction we are subtracting this BigFraction from.
     * @return this - that
     */
    public BigFraction subtract(BigFraction that)
    {
        BigInteger top = num.multiply(that.denom).subtract(denom.multiply(that.num));
        BigInteger bottom = denom.multiply(that.denom);
        return new BigFraction(top, bottom);
    }
    /**
     * This computes this*that.
     * @param that the BigFraction we are multiplying this BigFraction by.
     * @return this*that
     */
    public BigFraction multiply(BigFraction that)
    {
        BigInteger top = num.multiply(that.num);
        BigInteger bottom = denom.multiply(that.num);
        return new BigFraction(top, bottom);
    }
    /**
     * This computes this/that.
     * @param that the BigFraction we are dividing this BigFraction by.
     * @return this/that
     */
    public BigFraction divide(BigFraction that)
    {
        BigInteger top = num.multiply(that.denom);
        BigInteger bottom = denom.multiply(that.num);
        return new BigFraction(top, bottom);
    }
    /**
     * This is a static factory method that allows a BigFraction to 
     * specified by longs in the numerator and the denominator.
     * @param num the numerator we are specifying
     * @param denom the denominator we are specifying
     * @return the BigFraction num/denom.
     */
    public static BigFraction valueOf(long num, long denom)
    {
        return new BigFraction(BigInteger.valueOf(num), BigInteger.valueOf(denom));
    }
    /*
     * This is where test code is dumped.
     */
    public static void main(String[] args)
    {
        BigFraction boo = BigFraction.valueOf(3,4);
        System.out.println(boo);
        boo = BigFraction.valueOf(-3, -4);
        System.out.println(boo);
        boo = BigFraction.valueOf(6,8);
        System.out.println(boo);
        boo = BigFraction.valueOf(1048576, 7776);
        System.out.println(boo);
        BigFraction total = new BigFraction();
        for(long k = 1; k <= 1000; k++)
        {
            total = total.add(BigFraction.valueOf(1, k));
        }
        System.out.println(total);  
    }
}