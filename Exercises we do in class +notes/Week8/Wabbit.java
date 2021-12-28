package Week8;
public class Wabbit
{
    public static void main(String[] args)
    {
        // Integer.parseInt converts a string to an integer 
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        System.out.printf("%s*%s = %s\n", a, b, a*b);
    }
}
