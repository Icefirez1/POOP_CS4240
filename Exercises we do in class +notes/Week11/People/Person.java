public abstract class Person
{
    private String lastName;
    private String firstName;
    private final String ID;
    //getter functions
    public Person(String lastName, String firstName, String ID)
    {
        this.lastName = lastName;
        this.firstName = firstName;
        this.ID = ID;
    }
}