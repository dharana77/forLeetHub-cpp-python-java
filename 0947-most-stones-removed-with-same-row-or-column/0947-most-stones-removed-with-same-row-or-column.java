class Solution {
    public int removeStones(int[][] stones) {
        int n = stones.length;
        int parent[] = new int[n];
        
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
        
        int answer = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(stones[i][0] == stones[j][0] || stones[j][1] == stones[i][1]){
                    int pi = find(parent, i);
                    int pj = find(parent, j);
                    parent[pj] = pi;
                    if(pi != pj){
                        answer+=1;
                    }
                }
            }
        }
        return answer;
    }
    
    private int find(int[] parent, int i){
        if(i == parent[i]) return i;
        return find(parent, parent[i]);
    }
}