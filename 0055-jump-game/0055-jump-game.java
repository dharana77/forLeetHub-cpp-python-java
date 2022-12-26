import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public boolean canJump(int[] nums) {
        //bfs
        int n = nums.length;
        if(n==1) return true;
        int [] dp = new int[n+1];
        int mx = 0;
        for(int i=0; i<=mx; i++){
            if(mx >= n-1) return true;
            if(mx < i + nums[i]){
                mx = i + nums[i];
            }
        }
        return false;
    }
}