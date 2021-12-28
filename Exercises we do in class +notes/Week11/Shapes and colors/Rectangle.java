

public class Rectangle implements Polygon
{
    private double height;
    private double width;
    public Rectangle(double width, double height)
    {
        this.width = width;
        this.height = height;
    }
    public double area()
    {
        return width*height;
    }
    public double diameter()
    {
        return Math.hypot(width, height);
    }
    public double perimeter()
    {
        return 2*(height + width);
    }
    public int numSides()
    {
        return 4;
    }
    @Override
    public String toString()
    {
        return String.format("Rectangle(%s, %s)", width, height);
    }

    public static void main(String[] args)
    {
        System.out.println("Hello World");
    }
}