/*
 * This is a class of 3D immutible vectors.
 */
public class Vectorz3D implements IVector3D
{
    //initialize in a static block
    public static final Vectorz3D I = null;
    public static final Vectorz3D J = null;
    public static final Vectorz3D K = null;
    public final int a;
    public final int b;
    public final int c; 
    /*
     * @param a coefficient of I
     * @param b coefficient of J
     * @param c coefficient of K
     * This makes ai + bj + ck
     */
    public Vectorz3D(int a, int b, int c)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    /**
     * This makes the zero vector
     */
    public Vectorz3D()
    {
        this(0,0,0);
    }
    /**
     * @param that another Vector3D
     * @return  the dot product of this vector and that.
     */
    public int dot(Vectorz3D that)
    {
        return a*that.a + b*that.b + c*that.c;
    }
    /**
     * @param that another Vector3D
     * @return  the cross product of this vector and that.
     */
    public Vectorz3D cross(Vectorz3D that)
    {
        return new Vectorz3D(b*that.c - c*that.b, c*that.a-a*that.c, a*that.b-b*that.a);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return  the that*this
     */
    public Vectorz3D scalarMultiply(int scalar)
    {
        return new Vectorz3D(a*scalar, b*scalar, c*scalar);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this + that
     */
    public Vectorz3D add(Vectorz3D that)
    {
        return new Vectorz3D(a + that.a, b + that.b, c+that.c);
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this - that
     */
    public Vectorz3D subtract(Vectorz3D that)
    {
        return new Vectorz3D(a - that.a, b - that.b, c-that.c);
    }
    /**
     * @return the length of this vector
     */
    public double magnitude()
    {
        double num1 = Math.pow(a, 2);
        double num2 = Math.pow(b, 2);
        double num3 = Math.pow(c, 2);
        return Math.sqrt(num1 + num2 + num3);
    }
    /**
     * @param that another vector
     * @return the angle between this and that in radians in [0,&pi;]
     */
    public double angleBetween(Vectorz3D that)
    {
        double dotp = this.dot(that);
        double mags = this.magnitude() * that.magnitude();
        return  Math.acos(dotp/mags);
    }
    /**
     * @return A string representation of the form ai + bj + ck.
     * Make sure you have negative terms not looking like crap.
     */
    @Override 

    public String toString()
    {
        return String.format("s%i%+s%j%+s%k%", a, b, c);
    }
    @Override 
    public boolean equals(Object o)
    {
        
        if (o == this) {
            return true;
        } else if (!(o instanceof Vectorz3D)) {
            return false;
        }
        Vectorz3D other = (Vectorz3D) o;
        return other.a == a && other.b == b && other.c == c;
    }
