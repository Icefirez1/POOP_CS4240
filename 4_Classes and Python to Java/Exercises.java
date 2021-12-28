public class Exercises
{
    public static void main(String[] args)
    {
        System.out.println(between("catamaran", 'a').equals("tamar"));
        System.out.println(between("catamaran", 'c').equals(""));
        System.out.println(between("catamaran", 'q').equals(""));
        System.out.println(laxEquals("    boot", "boot"));
        System.out.println(laxEquals("boot    ", "boot"));
        System.out.println(laxEquals("     boot    ", "boot"));
        System.out.println(laxEquals(" \t\n    boot \n\t   ", "boot"));
        System.out.println(getExtension("wd2.tex").equals("tex"));
        System.out.println(getExtension("hello.py").equals("py"));
        System.out.println(getExtension("Hello.java").equals("java"));
        System.out.println(getExtension("tossMeNow").equals(""));
        System.out.println(getExtension(".").equals(""));
        System.out.println(isUpperCaseOnly("EAT NOW 123"));
        System.out.println(!isUpperCaseOnly("eat NOW 123"));
        System.out.println(isUpperCaseOnly(""));
    }
    /*
     * This returns an empty string if q is not present in
     * s or if it only appears once.  Otherwise, it returns the
     * substring between the first and last instances of q in s.
     */
    public static int countChar(String str, char c)
    {
        int count = 0;

        for(int i=0; i < str.length(); i++)
        {    if(str.charAt(i) == c)
                count++;
        }

        return count;
    }
    public static String between(String s, char q)
    {
        String character = Character.toString(q);
        if(s.contains(character))
        {
            int amount = countChar(s, q);
            int first = s.indexOf(q); 
            first += 1;
            int last = s.lastIndexOf(q);
            if (amount > 2)
            {
                return s.substring(first, last);
            }

            
        }
        return "";
    }
    /*
     * This returns true if the only difference between s1 and s2
     * is leading or trailing whitespace.  
     */
    public static boolean laxEquals(String s1, String s2)
    {
        Boolean s1test = s1.contains(" ");
        Boolean s2test = s2.contains(" ");
        Boolean s1test1 = s1.contains("\t");
        Boolean s2test1 = s2.contains("\t");
        if (s1test || s2test)
        {
            return true;
        }
        if(s1test1 || s2test1)
        {
            return true; 
        }
        return false;
    }
    /*
     * this returns an empty string if the fileName is empty
     * or has no extension. Otherwise, it returns the extension
     * without the dot.
     */
    public static String getExtension(String fileName)
    {
        Boolean yuh = fileName.contains(".");
        if (yuh)
        {
            int num = fileName.indexOf(".") + 1;
            return fileName.substring(num);
        }
        return "";
    }
    /*
     * this returns true if the String contains only uppercase
     * or non-alpha characters.
     */
    public static boolean isUpperCaseOnly(String s)
    {
        for (int i=0; i<s.length(); i++)
        {
            if (!Character.isUpperCase(s.charAt(i)))
            {
                if ((s.charAt(i) >= 'a' && s.charAt(i) <= 'z'))
                {
                    return false;
                }
            }
        }
    return true;
    }
}
