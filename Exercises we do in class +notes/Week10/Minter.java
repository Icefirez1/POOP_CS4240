package Week10;

public class Minter
{
    //generate objects with a serial number.
    private static int idWell;
    static
    {
        idWell = 1;
    }
    private final int id;
    public Minter()
    {
        id = idWell;
        idWell++;
    }
    @Override
    public String toString()
    {
        return String.format("Minter with id = %s", id);
    }
    public static void main(String[] args)
    {
        for(int k = 0; k < 20; k++)
        {
            System.out.println(new Minter());
        }
    }

}