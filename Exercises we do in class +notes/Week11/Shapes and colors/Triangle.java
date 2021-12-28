
public class Triangle implements Polygon 
{
    private double side_a;
    private double side_b;
    private double side_c;
    public Triangle (double a, double b, double c)
    {
        double s = (side_a+side_b+side_c)/2;
        double yum = s * (s-side_a) * (s-side_b) * (s-side_c);
        if (yum < 0)
        {
            throw new IllegalArgumentException();
        }
        this.side_a = a;
        this.side_b = b;
        this.side_c = c;
    }

    public int numSides() 
    {
        return 3;
    }
    public double area() 
    {
        double s = (side_a+side_b+side_c)/2;
        double yum = s * (s-side_a) * (s-side_b) * (s-side_c);
        if (yum < 0)
        {
            throw new IllegalArgumentException();
        }
        return Math.sqrt(yum);
    }

    public double diameter() 
    {
        if (side_a > side_b && side_a > side_c)
        {
            return side_a;
        } 
        if (side_b > side_a && side_b > side_c)
        {
            return side_b;
        }
        if (side_c > side_b && side_c > side_a)
        {
            return side_a;
        }
        return -1;
    }

    public double perimeter() 
    {
        return side_a + side_b + side_c;
    }
    
}
