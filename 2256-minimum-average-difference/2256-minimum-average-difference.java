class Solution {
    public int minimumAverageDifference(int[] nums) {
        //0-indexed arr, len n
        //rounded down to the nearest integer
        int n = nums.length;
        long total[] = new long[n];
        long s = 0;
        for(int i=0; i<n; i++){
            s+= nums[i];
            total[i] = s;
        }
        long ans = Integer.MAX_VALUE;
        int mnIdx = -1;
        
        for(int i=0; i<n-1; i++){
            long left = i+1;
            long right = n-(left);
            long leftAvg = total[i]/left;
            long rightAvg = (total[n-1] - total[i])/right;
            long res = Math.abs(leftAvg - rightAvg);
            if(res < ans){
                ans = res;
                mnIdx = i;
                // System.out.println(ans);
            }
        }
        
        for(int i=0; i<n-1; i++){
            int left = i+1;
            int right = n-(left);
            long leftAvg = total[i]/left;
            long rightAvg = (total[n-1] - total[i])/right;
            long res = Math.abs(leftAvg - rightAvg);
            if(res == ans){
                mnIdx = i;
                break;
            }
        }
        long res = Math.abs(total[n-1]/n);
        
        
        if (res < ans){
            // System.out.println(res);
            mnIdx = n-1;
        }
        return mnIdx;
        
    }
}