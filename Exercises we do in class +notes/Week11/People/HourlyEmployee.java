public class HourlyEmployee extends Employee
{
    private double rate;
    public HourlyEmployee(String lastName, String firstName, 
        String ID, String title,
        double rate)
    {
        super(lastName, firstName, ID, title);
        this.rate = rate;
    }
    @Override
    public double computePay()
    {
        return rate*40;
    }
}