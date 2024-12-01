class Solution {
    public boolean checkIfExist(int[] arr) {
        for(int i=0; i<arr.length; i++) {
            for(int j= i+1; j<arr.length; j++) {
                int v = arr[i];
                int s = arr[j] * 2;
                // System.out.println(v);
                // System.out.println(s);
                if (v == s || arr[i] * 2 == arr[j]) return true;
            }
        }
        return false;
    }
}