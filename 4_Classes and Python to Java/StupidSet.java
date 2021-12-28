
import java.util.ArrayList;

public class StupidSet<T>
{
    private ArrayList<T> elements;
    private int size;


    /**
     * @param items is an array list of items to
     * put in our StupidSet without duplicates
     */
    public StupidSet(ArrayList<T> items) /*works*/
    {
        elements = new ArrayList<T> ();
        size = 0;
        for (T item: items)
        {
            if(! elements.contains(item)){
                elements.add(item);
                size ++;
            }
        }

    }
    public ArrayList<T> getElements(){ /*works*/
        return elements;
    }

    /**
     * This makes an empty StupidSet
     */
    public StupidSet() /*works*/
    {
        this(new ArrayList<T>());
    }
    /**
     * This adds a new item to our StupidSet and returns
     * <code>false</code> if the item is already present.
     * @param newItem the new item we are adding
     * @return false if the new item is not added and
     * <code>true</code> otherwise.
     */
    public boolean add(T newItem) /*works*/
    {
        if(! elements.contains(newItem)){
            elements.add(newItem);
            size ++;
            return true;
        }
        return false;
    }    
    /**
     * This checks for the presence of <code> item</code>
     * in this StupidSet.
     * @param item the new item we are checking for
     * @return false if the item is not present
     * <code>true</code> otherwise.
     */
    public boolean contains(T newItem) /*works*/
    {
        return elements.contains(newItem);
    }    
    /**
     * This checks to see if <code>other</code> is
     * a subset of this StupidSet.
     * @param item a Stupidset
     * @return <code>true</code> if every element of 
     * <code>other</code> belongs to this StupidSet
     * and <code>false</code> otherwise.
     */
    public boolean containsAll(StupidSet<T> other) /*works*/
    {
        ArrayList<T> otherArray = other.getElements(); 
        if (other.size == 0)
        {
            return false;
        }
        for (T item: otherArray)
        {
            if(!elements.contains(item))
            {
                return false;
            }
            
        }
        return true;
    }    
    /**
     * This removes <code>item</code> if it is present
     * @param item the item we are trying to remove
     * @return false if the item is not present
     * <code>true</code> if the item got removed.
     */
    public boolean remove(T item) /*works*/
    {
        if(elements.contains(item)){
            int place = elements.indexOf(item);
            elements.remove(place);
            size --;
            return true;
        }
        return false;
        
    }    
    /**
     * This adds all items in moreStuff to this StupidSet
     * @param moreStuff a StupidSet
     * @return <code>true</code> if at least one item
     * is added
     */
    public boolean addAll(StupidSet<T> moreStuff) /*working*/ 
    {
        ArrayList<T> morez = moreStuff.getElements();
        boolean gotNew = false;
        for(T thing: morez)
        {
            if(! elements.contains(thing))
            {
                elements.add(thing);
                size ++;
                gotNew = true;
            }
        }
        return gotNew;
    }
    /**
     * This makes a Python-list style representation of 
     * our StupidSet.
     * @return a representation of the form
     * <pre>[one, two, three .... last]</pre>
     */
    @Override
    public String toString() /*works*/
    {
        String results = "[";
        if (elements.size() == 0)
        {
            return "[]";
        }
        for (int i = 0; i < size -1 ; i++)
        {
            results += String.format("%s, ", elements.get(i));
        }
        results += String.format("%s]", elements.get(size -1));
        return results; 
    }
    public int size() /*works*/
    {
        return size;
    }
    public static void main(String[] args) 
    {
        StupidSet <Integer> uhm = new StupidSet<>(); /* test of making stupid set */ 
        uhm.add(1);
        uhm.add(2);
        uhm.add(3);
        uhm.add(4);
        uhm.add(3);
        uhm.add(0);
        String stupidstring = uhm.toString(); /*test of printing stupid set*/
        System.out.println(stupidstring);

        int size = uhm.size(); /*test of size method*/
        System.out.println(size); 

        StupidSet <Integer> another = new StupidSet<>();
        another.add(5);
        another.add(6);
        another.add(7);
        another.add(8);
        another.add(9);
        String eloel = another.toString();
        System.out.println(eloel);



        uhm.addAll(another); /*test of addAll*/
        stupidstring = uhm.toString();
        System.out.println(stupidstring);

        boolean inHere = uhm.contains(9); /*test of contains*/
        System.out.println(inHere);
        boolean notHere = uhm.contains(10); 
        System.out.println(notHere);

        StupidSet <Integer> anotherOne = new StupidSet<>(); //test of conatinsAll
        anotherOne.add(5);
        anotherOne.add(6);
        anotherOne.add(7);
        anotherOne.add(8);
        anotherOne.add(1013212);

        boolean yuh = uhm.containsAll(anotherOne);
        System.out.println("hey all");
        System.out.println(yuh); 

        
        uhm.remove(9); /*test of remove*/ 
        stupidstring = uhm.toString();
        System.out.println(stupidstring);




        System.out.println("el o el"); /*finished statement*/
    }
    
}
