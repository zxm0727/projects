
import org.jgrapht.*;
import org.jgrapht.alg.flow.PushRelabelMFImpl;
import org.jgrapht.graph.*;
import org.jgrapht.alg.*;

import java.util.*;
/**
 *
 * @author xinmingzhang
 */
public class SauerSignage {

    public static boolean isSignagePossible(String[][] displays, String[] phrase){
        Graph<String, DefaultWeightedEdge> graph = new SimpleDirectedWeightedGraph<>(DefaultWeightedEdge.class);

        graph.addVertex("source");
        int len = displays.length;
        for(int i = 0; i<len; i++) {
            String currentD = "display" + i;
            graph.addVertex(currentD);
            //connect S with displays
            graph.addEdge("source", currentD);
            graph.setEdgeWeight("source", currentD, 1.0);
        }
        ArrayList<String> third = new ArrayList<>();
        for(int i = 0; i<len; i++) {
            for(int j = 0; j<displays[i].length; j++){
                if(!third.contains(displays[i][j]))
                    third.add(displays[i][j]);
            }
        }

        ArrayList<String> letter = new ArrayList<>();
        ArrayList<Integer> count = new ArrayList<>();
        for(int i = 0;i<26; i++){
            count.add(0);
        }
        int len2 = phrase.length;
        for(int i = 0; i < len2; i++) {
            if(!letter.contains(phrase[i]))
                letter.add(phrase[i]);
            int curr= letter.indexOf(phrase[i]);
            //count++;
            count.set(curr, count.get(curr)+1);
        }
        graph.addVertex("phrase");
        for (int i = 0;i < third.size(); i++) {
            String current = third.get(i);
            int currIndex = letter.indexOf(current);
            graph.addVertex(current);
            if(letter.contains(current)){
                graph.addEdge(current, "phrase");
                graph.setEdgeWeight(current, "phrase", count.get(currIndex));
            }
        }

        for (int i = 0; i < len; i++) {
            for (String vertex : displays[i]) {
                graph.addEdge("display"+i, vertex);
                graph.setEdgeWeight("display"+i, vertex, 1.0);
            }
        }

        //The graph network flow algorithm you're suggested to use.
        PushRelabelMFImpl<String,DefaultWeightedEdge> maxFlow = new PushRelabelMFImpl<>(graph);
        double flowAmt = maxFlow.calculateMaximumFlow("source", "phrase");

        //System.out.println(maxFlow.getFlowMap());

        if(flowAmt == phrase.length)
            return true;

        return false;
    }

    public static void main(String[] args){
        String[][] displays = {{"W","C", "X"}, {"T", "Q", "X", "E"}, {"J", "V", "E", "Z"}, {"X", "H", "Q", "O"}, {"G", "J", "R", "U"}, {"I", "M", "N", "W", "E"}};
        String[] phrase = {"I", "I", "X", "R", "Z", "W"};

        System.out.println(isSignagePossible(displays, phrase));
    }

}
