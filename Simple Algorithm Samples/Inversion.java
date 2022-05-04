public class Inversion {

    /*
     * Counts the number of count of a given permutation using
     * the Divide and Conquer paradigm.
     * 
     * @param n The length of the permutation.
     * 
     * @param perm A permutation of the elements [0, 1, ..., n-1]. 
     * That is, those elements 0,1,..., n-1 in some order.
     * 
     * @return The number of count of perm.
     */
    public static int countInversions(int n, int[] perm) {
        assert perm.length == n;
        if (n < 2) {
            return 0;
        }
        int[] copy = new int[n];
        for (int i = 0; i < n; i++) {
            copy[i] = perm[i];
        }
        int[] temp = new int[n];
        return reverse(copy, 0, n - 1, temp);
    }

    public static int reverse(int[] copy, int left, int right, int[] temp) {
        if (left == right)
            return 0;
        int mid = left + (right - left) / 2;
        int leftPart = reverse(copy, left, mid, temp);
        int rightPart = reverse(copy, mid + 1, right, temp);
        if (copy[mid] <= copy[mid + 1]) {
            return leftPart + rightPart;
        }
        int cross = merge(copy, left, mid, right, temp);
        return leftPart + rightPart + cross;
    }

    public static int merge(int[] copy, int left, int mid, int right, int[] temp) {
        for (int i = left; i <= right; i++)
            temp[i] = copy[i];
        int newLeft = left;
        int newMid = mid + 1;
        int count = 0;
        for (int k = left; k <= right; k++) {
            if (newLeft == mid + 1) {
                copy[k] = temp[newMid];
                newMid++;
            } else if (newMid == right + 1) {
                copy[k] = temp[newLeft];
                newLeft++;
            } else if (temp[newLeft] <= temp[newMid]) {
                copy[k] = temp[newLeft];
                newLeft++;
            } else {
                copy[k] = temp[newMid];
                newMid++;
                count += (mid-newLeft+1);
            }
        }
        return count;
    }

    

/*
     * If you want to write your own tests, put them here.
 */
public static void main(String[] args) {
        int[] test = {17,5,1,32,8,10,9,50};
        int result = countInversions(8,test);
        System.out.println(result);
    }
}

