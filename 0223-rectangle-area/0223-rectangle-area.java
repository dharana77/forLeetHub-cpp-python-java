class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int biggerLeftX = Math.max(ax1, bx1);
        int biggerLeftY = Math.max(ay1, by1);
        int smallerRightX = Math.min(ax2, bx2);
        int smallerRightY = Math.min(ay2, by2);
        
        int same = (smallerRightX - biggerLeftX) * (smallerRightY - biggerLeftY);
        
        int sq1 = (ax2-ax1) * (ay2-ay1);
        int sq2 = (bx2-bx1) * (by2-by1);
        
        int answer = 0;
        boolean case5 = bx1 <= ax2 && bx2 >= ax1 && by1 <= ay2 && by2 >= ay1;
        
        if (case5){
            answer = sq1 + sq2 - same;
        }else{
            answer = sq1 + sq2;
        }
        return answer;
    }
}