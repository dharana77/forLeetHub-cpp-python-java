import java.util.*;
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> s = new HashSet<>();
        // System.out.println(rooms.size());
        boolean [] visited = new boolean [rooms.size() + 1];
        visited[0] = true;
        for(int key: rooms.get(0)){
            s.add(key);
        }
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(0);
        while(!q.isEmpty()){
            int cur = q.poll();
            List<Integer> tars = rooms.get(cur);
            for(int i=0; i<tars.size(); i++){
                if(!visited[tars.get(i)]){
                    visited[tars.get(i)] = true;
                    q.add(tars.get(i));
                }
            }
        }
        for(int i=0; i<rooms.size(); i++){
            if(!visited[i]) return false;
        }
        return true;
    }
}