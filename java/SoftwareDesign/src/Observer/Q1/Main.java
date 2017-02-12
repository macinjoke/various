package Observer.Q1;

import Observer.A1.NumberGenerator;
import Observer.A1.Observer;
import Observer.A1.DigitObserver;
import Observer.A1.GraphObserver;
import Observer.A1.IncrementalNumberGenerator;

public class Main {
    public static void main(String[] args) {
        NumberGenerator generator = new IncrementalNumberGenerator(10, 50, 5);  
        Observer observer1 = new DigitObserver();
        Observer observer2 = new GraphObserver();
        generator.addObserver(observer1);
        generator.addObserver(observer2);
        generator.execute();
    }
}
