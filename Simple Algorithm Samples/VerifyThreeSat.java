import java.util.*;
public class VerifyThreeSat {
    /*
     * Input :
     *
     * -boolean array X of length n
     *
     * -2d boolean array Y with m rows and 3 columns
     *
     * -2d int array Z with m rows and 3 columns,
     *  where each element is between 1 and n (inclusive)
     *
     * Output: return true if all constraints are satisfied with the
     * specified variable settings; false otherwise
     */
    public static boolean verify(boolean[] X, boolean[][] Y, int[][] Z) {
        boolean first = false;
        boolean check = false;
        int len = Y.length;
        for (int i = 0; i<len; i++) {
            if (i == 0) {
                first = (X[Z[i][0] - 1] == Y[i][0]||X[Z[i][1] - 1] == Y[i][1]||X[Z[i][2] - 1] == Y[i][2]);
            } else if (i == 1) {
                check = (X[Z[i][0] - 1] == Y[i][0]||X[Z[i][1] - 1] == Y[i][1]||X[Z[i][2] - 1] == Y[i][2]);
                //Both
                check = first && check;
            } else {
                check = check && (X[Z[i][0] - 1] == Y[i][0]||X[Z[i][1] - 1] == Y[i][1]||X[Z[i][2] - 1] == Y[i][2]);
            }
        }
        return check;
    }

    /*
     * A couple of test cases are provided to help you see what the input and output
     * look like :)
     *
     * You can also modify the provided main method for your own test cases. The main
     * method will not be graded. You'll only be graded on VerifyThreeSat.
     */
    public static void main (String[] args) {
        final boolean T = true;
        final boolean F = false;

        // impossible to satisfy
        boolean[][] Y1 = {{T, T, T},
                {F, F, F}};

        int[][] Z1 = {{1, 1, 1},
                {1, 1, 1}};

        System.out.println(verify(new boolean[] {T}, Y1, Z1)); // false
        System.out.println(verify(new boolean[] {F}, Y1, Z1)); // false

        // satisfied if and only if x_2 and x_3 are true
        boolean[][] Y2 = {{T, T, T},
                {F, F, T},
                {T, T, T}};

        int[][] Z2 = {{1, 1, 2},
                {1, 1, 2},
                {3, 3, 3}};

        System.out.println(verify(new boolean[] {F, T, T}, Y2, Z2)); // true
        System.out.println(verify(new boolean[] {T, T, T}, Y2, Z2)); // true
        System.out.println(verify(new boolean[] {T, T, F}, Y2, Z2)); // false
        System.out.println(verify(new boolean[] {T, F, T}, Y2, Z2)); // false
    }
}
