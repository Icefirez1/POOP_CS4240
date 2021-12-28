package Week12;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Crawler 
{
    public static void main(String[] args) throws IOException
    {
        String dirName = args[0];
        String extension = args[1];
        if (args.length < 2)
        {
            System.err.println("Malfromed request!");
            System.out.println("usage: java Craw;er directory extension");
            System.exit(1);
        }
        /*search dirName and list all files having the specidied extension*/
        //create a path to the directory 
        Path pathToDir = Path.of(dirName);
        if (!Files.isDirectory(pathToDir))
        {
            System.err.printf("Bestie File %s is nonexistant or not a direcotry", pathToDir );
            System.exit(1);             
        }
        try{

            Files.list(pathToDir)
                .filter(e -> e.toString().endsWith("." + extension))
                .forEach(System.out::println);        
        }
        catch(IOException ex) 
        {
        }
    }
}
