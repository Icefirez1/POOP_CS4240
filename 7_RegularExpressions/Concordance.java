//package 7_RegularExpressions;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.TreeMap;

public class Concordance {
    public static void main(String[] args)
    {
        Path input = Path.of(args[0]);
        Path output = Path.of(args[1]);
        // try with resources 
        try (
            BufferedReader reader = Files.newBufferedReader(input);
            BufferedWriter writer = Files.newBufferedWriter(output); )
        {
            //dictionary in python is called a map 
            Map <String, Integer> items = new TreeMap<String, Integer>(); //Hashmaps dont sort 
            reader.lines()
                .forEach(line -> {
                    String words = line;
                    //ArrayList<String> arrOfstr = new ArrayList<String>();
                    String[] arrOfStr = words.split(" ");
                    for (int k = 0; k < arrOfStr.length; k++ )
                    {
                        arrOfStr[k] = arrOfStr[k].replaceAll("[\\p{P}&&[^\u0027]]","").toLowerCase();
                    }

                    for (int i = 0; i < arrOfStr.length; i++ )
                    {
                        if (items.containsKey(arrOfStr[i]))
                        {
                            items.replace(arrOfStr[i], items.get(arrOfStr[i]) + 1);
                        }
                        else
                        {
                            items.put(arrOfStr[i], 1);
                        }
                    }
                });
            
            for (Map.Entry<String, Integer> entry : items.entrySet())
            {
                writer.write(entry.getKey() + "     " + entry.getValue() + "\n");
            }
        } 
        catch(IOException ex)
        {
            System.err.println("You have been mooned by IOException");
        }
    }
}
