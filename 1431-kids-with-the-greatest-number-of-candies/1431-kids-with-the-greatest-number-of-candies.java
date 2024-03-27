class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int mx = Arrays.stream(candies).max().getAsInt();
        List<Boolean> answer = new ArrayList<>();
        for(int i=0; i<candies.length; i++){
            if(candies[i] + extraCandies >= mx){
                answer.add(true);
            }else{
                answer.add(false);
            }
        }
        return answer;
    }
}