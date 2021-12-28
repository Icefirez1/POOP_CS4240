/*
 * This is a class of 3D immutible vectors.
 */
public class Vector3D implements IVector3D
{
    //initialize in a static block
    public static final Vector3D I = null;
    public static final Vector3D J = null;
    public static final Vector3D K = null;
    /*
     * @param a coefficient of I
     * @param b coefficient of J
     * @param c coefficient of K
     * This makes ai + bj + ck
     */
    public Vector3D(int a, int b, int c)
    {
    }
    /**
     * This makes the zero vector
     */
    public Vector3D()
    {
        
    }
    /**
     * @param that another Vector3D
     * @return  the dot product of this vector and that.
     */
    public int dot(Vector3D that)
    {
        return 0;
    }
    /**
     * @param that another Vector3D
     * @return  the cross product of this vector and that.
     */
    public Vector3D cross(Vector3D that)
    {
        return null;
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return  the that*this
     */
    public Vector3D scalarMultiply(int scalar)
    {
        return null;
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this + that
     */
    public Vector3D add(Vector3D that)
    {
        return null;
    }
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this - that
     */
    public Vector3D subtract(Vector3D that)
    {
        return null;
    }
    /**
     * @return the length of this vector
     */
    public double magnitude()
    {
        return 0;
    }
    /**
     * @param that another vector
     * @return the angle between this and that in radians in [0,&pi;]
     */
    public double angleBetween(Vector3D that)
    {
        return 0.0;
    }
    /**
     * @return A string representation of the form ai + bj + ck.
     * Make sure you have negative terms not looking like crap.
     */
    @Override 

    public String toString()
    {
        return "";
    }
    @Override 
    public boolean equals(Object o)
    {
        return false;
    }

}
