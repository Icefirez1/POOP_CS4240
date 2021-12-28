
package Week9;

import java.util.ArrayList;

public class Pair <S, T>
{
    private S s;
    private T t;
    public Pair(S s, T t)
    {
        this.s = s;
        this.t = t;

    }
    public S getS()
    {
        return s;
    }
    public T getT()
    {
        return t;
    }
    @Override 
    public String toString()
    {
        return String.format("(%s, %s)", s, t);
    }
    public static void main(String[] args)
    {
        Pair<String, String> phone = new Pair<>("Morrison", "2746");
        System.out.println(phone);
        ArrayList<String> al = new ArrayList<>();
        al.add("Nixon");
        al.add("Colson");
        al.add("Morrison");
        al.add("Davids");
        Pair<String, ArrayList<String>> lists = new Pair<>("enemies", al);
        System.out.println(lists);
    }
        
}
