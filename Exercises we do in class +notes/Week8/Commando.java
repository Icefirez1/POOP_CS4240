package Week8;
public class Commando {
    public static void main(String[] args)
    {
        for(int k = 0; k < args.length; k++)
        {
            System.out.printf("args[%s} = %s\n", k , args[k]);
        }
    }
}