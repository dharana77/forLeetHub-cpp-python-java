class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        
        for(int i=0; i<arr.length; i++){
            if(m.containsKey(arr[i])){
                m.put(arr[i], m.get(arr[i]) + 1);
            }else{
                m.put(arr[i], 0);
            }
        }
        
        Set<Integer> s = new HashSet<Integer>();
        for(Integer key: m.keySet()){
            if(s.contains(m.get(key))){
                return false;
            }else{
                s.add(m.get(key));
            }
        }
        return true;
    }
}