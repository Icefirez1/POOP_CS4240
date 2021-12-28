public abstract class Employee extends Person
{
    private String title;
    public Employee(String lastName, String firstName, 
        String ID, String title)
    {
        super(lastName, firstName, ID);
        this.title = title;
    }
    public abstract double computePay();
}