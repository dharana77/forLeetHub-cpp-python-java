import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        int [] visited = new int [n+1];
        visited[source] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(source);
        
        while(!q.isEmpty()){
            int cur = q.poll();
            if(cur == destination)return true;
            Set<Integer> nexts = findNeighbors(edges, n, cur);
            for(int next : nexts){
                if(visited[next]!=1){
                    visited[next] = 1;
                    q.add(next);
                }
            }
        }
        
        if(visited[destination]==1) return true;
        return false;
    }
    
    private static Set<Integer> findNeighbors(int edges[][], int n, int v){
        Set<Integer> s = new HashSet<Integer>() ;
        for(int i=0; i<edges.length; i++){
            int from = edges[i][0];
            int to = edges[i][1];
            if(from == v){
                s.add(to);
            }else if(to == v){
                s.add(from);
            }
        }
        return s;
    }
}