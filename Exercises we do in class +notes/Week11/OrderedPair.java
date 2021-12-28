import java.util.Comparator;
import java.util.Collections;
import java.util.ArrayList;

public class OrderedPair implements Comparable<OrderedPair>
{
    private final int x;
    private final int y;
    public OrderedPair(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    public int compareTo(OrderedPair q)
    {
        if(x == q.x)
        {
            return y - q.y;
        }
        return x - q.x;
    }
    @Override 
    public String toString()
    {
        return String.format("(%s, %s)", x, y);
    }
    public static void main(String[] args)
    {
        OrderedPair op = new OrderedPair(3,3);
        ArrayList<OrderedPair> pairs = new ArrayList<>();
        Comparator<OrderedPair> bySum = (a, b) ->
        {
            if( a.x + a.y == b.x + b.y)
            {
                return a.x - b.x;
            }
            return a.x + a.y -(b.x + b.y);
        };
        pairs.add(new OrderedPair(1,2));
        pairs.add(new OrderedPair(2,1));
        pairs.add(new OrderedPair(4,5));
        pairs.add(new OrderedPair(5,3));
        pairs.add(new OrderedPair(3,4));
        pairs.add(new OrderedPair(3,5));
        pairs.add(new OrderedPair(3,0));
        pairs.add(new OrderedPair(3,6));
        pairs.add(new OrderedPair(1, -3));
        pairs.add(new OrderedPair(6, 2));
        pairs.add(new OrderedPair(7, -1));
        System.out.println(pairs);
        Collections.sort(pairs);
        System.out.println(pairs);
        Collections.sort(pairs, bySum);
        System.out.println(pairs);
        
    }
}