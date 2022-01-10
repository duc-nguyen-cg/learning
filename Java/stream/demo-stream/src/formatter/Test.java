package formatter;

import java.text.NumberFormat;

public class Test {
    public static void main(String[] args) {
        Double d = new Double(21.099);

        NumberFormat nf = NumberFormat.getInstance();
        nf.setMaximumFractionDigits(2);
        nf.setMinimumFractionDigits(2);
        System.out.println(nf.format(d));
    }
}
