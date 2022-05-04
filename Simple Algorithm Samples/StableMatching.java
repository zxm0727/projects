import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class StableMatching {
    /*
     * Generates a stable matching.
     * 
     * @param prefHorses Preferences of the horses. prefHorses[i] lists the indices
     * of the riders that the i-th horse prefers, in order of preference.
     * 
     * @param prefRiders Preferences of the riders. prefHorses[i] lists the
     * indices of the horses that the i-th rider prefers, in order of preference.
     * 
     * @param horseOptimal if true, the generated stable matching should be most
     * optimal for the horses. Otherwise, it should be most optimal for the riders.
     * 
     * @return Computed stable matching. It is a 1D array, where arr[i]=j means the
     * i-th horse is matched to the j-th rider.
     */
    public static int[] findStableMatching(int[][] prefHorses, int[][] prefRiders, boolean horseOptimal) {
        assert prefHorses.length == prefRiders.length;
        int len = prefHorses.length;
        int[] result = new int[len];
        if(horseOptimal){
            int[] temp = match(prefHorses, prefRiders, len);
            for(int i = 0; i < len; i++)
            	for(int j = 0; j < len; j++)
            		if(temp[j] == i)
            			result[i] = j;
        } else {
            result = match(prefRiders, prefHorses, len);
        }
        
        return result;
    }

    public static int[] match(int[][] pref1, int[][] pref2, int len){
        int[] result = new int[len];
        Arrays.fill(result, -1);
        Queue<Integer> free = new LinkedList<Integer>();
        for(int i = 0; i < len; i++)
            free.add(i);
        Map<Integer, Integer> next = new HashMap<Integer, Integer>();
        for(int i = 0; i<len; i++)
            next.put(i, pref1[i][0]);
        int[] count = new int[len];
        Arrays.fill(count, 0);
        while(free.size()!=0){
            int current1 = free.remove();
            int current2 = next.get(current1);
            if(result[current2] == -1){
                result[current2] = current1;
            } else {
                int prev = 0;
                int current = 0;
                for (int i = 0; i < len; i++) {
                    if (pref2[current2][i] == result[current2]) {
                        prev = i;
                    }
                    if (pref2[current2][i] == current1) {
                        current = i;
                    }
                }
                if (prev > current) {
                    free.add(result[current2]);
                    result[current2] = current1;
                } else {
                    free.add(current1);
                }
        }
            count[current1]++;
            if(count[current1]<len){
                next.put(current1, pref1[current1][count[current1]]);
            }
        }
        return result;
    }
        
    
    
    /*
     * A short sanity check is provided to help you see what the input and output
     * look like :)
     * 
     * You can also modify the provided main method for your own test cases. This
     * method will not be graded.
     */
    public static void main(String[] args) {
        int[][] prefHorses = { { 0, 1 }, // Preferences of h0
                { 1, 0 }, // Preferences of h1
        };
        int[][] prefRiders = { { 0, 1 }, // Preferences of r0
                { 1, 0 }, // Preferences of r1
        };

        System.out.printf("Horse-optimal: ");
        System.out.println(Arrays.toString(findStableMatching(prefHorses, prefRiders, true)));
        System.out.printf("Rider-optimal: ");
        System.out.println(Arrays.toString(findStableMatching(prefHorses, prefRiders, false)));
    }
}