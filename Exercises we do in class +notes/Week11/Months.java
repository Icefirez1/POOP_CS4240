public class Months
{
    private static String[] names;
    public Months()
    {
        names = new String[]{"", "January", "February", "March",
            "April", "May", "June", "July", "August", "September",
            "November", "December"};
    }
    public static void main(String[] args)
    {
        try 
        {
            int month = Integer.parseInt(args[0]);
            Months m = new Months();
            System.out.println(names[month]);
        }
        catch(IndexOutOfBoundsException ex)
        {
            System.err.println("A command-line argument 1-12 is required");
        }
        catch (NumberFormatException ex)
        {
            System.err.println("A numer is required as a command line argument");
        }
        finally 
        {
            System.out.println("Thanks for using my BRILLIANT program");
        }
    }
}