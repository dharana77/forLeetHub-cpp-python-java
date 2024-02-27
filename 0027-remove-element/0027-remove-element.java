import java.util.*;


class Solution {
    public int removeElement(int[] nums, int val) {
        int ret = 0;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        for(int i=0; i<nums.length; i++){
            if (nums[i] != val){
                ret += 1;
                arr.add(nums[i]);
            }
        }
        
        // nums = new int[ret];
        Integer[] test = arr.toArray(new Integer[ret]);
        // nums = Arrays.stream(test).mapToInt(Integer::intValue).toArray(); 
        for(int i=0; i<ret; i++){
            nums[i] = test[i];
        }
        return ret;
    }
}