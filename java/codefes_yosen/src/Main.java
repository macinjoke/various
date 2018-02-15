import java.util.HashMap;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args){
        int N = 0;
        int D[] = new int[0];
        int M = 0;
        int T[] = new int[0];

        Scanner in = new Scanner(System.in);
        for(int i=0; i < 4; i++) {
            String s = in.nextLine();
            String[] split = s.split(" ");
            switch (i) {
                case 0:
                    N = Integer.parseInt(split[0]);
                    D = new int[N];
                    break;
                case 1:
                    D = Stream.of(split).mapToInt(Integer::parseInt).toArray();
                    break;
                case 2:
                    M = Integer.parseInt(split[0]);
                    break;
                case 3:
                    T = Stream.of(split).mapToInt(Integer::parseInt).toArray();
            }
        }

        HashMap<Integer,Integer> DD = new HashMap<Integer,Integer>();
        for (int i = 0; i < D.length; i++) {
            try {
                int a = DD.get(D[i]);
                DD.put(D[i], a + 1);
            } catch (Exception e) {
                DD.put(D[i], 1);
            }
        }

        System.out.println();

        HashMap<Integer,Integer> TT = new HashMap<Integer,Integer>();
        for (int i = 0; i < T.length; i++) {
            try {
                int a = TT.get(T[i]);
                TT.put(T[i], a + 1);
            } catch (Exception e) {
                TT.put(T[i], 1);
            }
        }

        for (Integer key : TT.keySet()) {
            int d, t;
            try {
                d = DD.get(key);
                t = TT.get(key);
            } catch (Exception e) {
                System.out.println("NO");
                return;
            }
            if(d < t) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
