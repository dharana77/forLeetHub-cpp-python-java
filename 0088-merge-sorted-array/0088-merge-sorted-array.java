class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] merged = new int[n+m];
        for(int i=0; i<m; i++){
            merged[i] = nums1[i];
        }
        for(int j=0; j<n; j++){
            nums1[m+j] = nums2[j];
            merged[m+j] = nums2[j];
        }

        for(int i=0; i<n+m; i++){
            nums1[i] = merged[i];
        }
        Arrays.sort(nums1);
    }
}