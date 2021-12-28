public class Driver
{
    public static void main(String[] args)
    {
        Shape s = new Square(10);
        System.out.println(s.area());
        System.out.println(s.perimeter());
        System.out.println(s.diameter());
        System.out.println(s);
    }
}