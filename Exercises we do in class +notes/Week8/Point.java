package Week8;
public class Point
{
    private final int x; // final means "Not reassignable "
    private final int y; 
    public Point(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    public Point()
    {
       this(0,0); //calls sibling constructor 
    }
    @Override 
    public String toString()
    {
        return String.format("(%s, %s)", x, y);
    }
    @Override 
    public boolean equals(Object o)
    {
        if(!(o instanceof Point))
        {
            return false;
        }
        if(this == o)
        {
            return true; 
        }
        Point that = (Point) o;
        return x == that.x && y == that.y;

    }
    public int getX()
    {
        return x;
    }
    public int getY()
    {
        return y;
    }
    public double distanceTo(Point q)
    {
        return Math.hypot(x - q.x, y - q.y);
    }
    public Point reflectionAcrossX()
    {
        return new Point(x, -y);
    }
    public Point reflectionAcrossY()
    {
        return new Point(-x, y);
    }
    public Point reflectionAcrossYequalsX()
    {
        return new Point(y, x);
    }
    public static void main(String[] args)
    {
        Point p = new Point(3,4);
        Point q = new Point();
        Point z = new Point(3,4);
        System.out.println(p.distanceTo(q));
        System.out.println(p.x);
        System.out.println(p.y);
        System.out.println(p);
        System.out.println(p.reflectionAcrossX());
        System.out.println(p == z);  //false
        System.out.println(p.equals(z));  //True
    }
}
