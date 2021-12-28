
public class Square extends Rectangle
{
    public double side;
    public Square(double side) {
        super(side, side);
        //TODO Auto-generated constructor stub
    }

    @Override 
    public String toString()
    {
        return String.format("Square(%s)", side);
    }
    
}
