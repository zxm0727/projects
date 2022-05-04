public class Fibonacci {
    /*
     * Returns the nth term in the Fibonacci Sequence, with
     * F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
     *
     * @param n The term index
     *
     * @return The nth Fibonacci number
     */
    public static int F(int n) {
        int first = 0;
        int second = 1;
        int[] result = new int[n+2];
        result[0] = first;
        result[1] = second;
        for (int i = 2; i <= n; i++)
   			{
        		result[i] = result[i-1] + result[i-2];
    		}
        return result[n];
    }

    /*
     *  If you want to write your own tests, put them here.
     */
    public static void main(String[] args) {
		for(int i = 0;i < 10;i++){
            System.out.println(F(i) + " ");
        }
    }
}
