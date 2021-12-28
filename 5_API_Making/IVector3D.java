/**
 * DO NOT change this interface in any way
 * Your program will be compiled against this interface, so your methods
 * must have exactly these signatures or your program will fail to compile.
 */
public interface IVector3D
{
    /**
     * @param that anohter Vector3D
     * @return  the dot product of this vector and that.
     */
    public int dot(Vector3D that);
    /**
     * @param that anohter Vector3D
     * @return  the cross product of this vector and that.
     */
    public Vector3D cross(Vector3D that);
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return  the that*this
     */
    public Vector3D scalarMultiply(int scalar);
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this + that
     */
    public Vector3D add(Vector3D that);
    /**
     * @param scalar a integer we are scalar multiplying this vector by
     * @return this - that
     */
    public Vector3D subtract(Vector3D that);
    /**
     * @return the length of this vector
     */
    public double magnitude();
    /**
     * @param that another vector
     * @return the angle between this and that in radians in [0,&pi;]
     */
    public double angleBetween(Vector3D that);
}
    

