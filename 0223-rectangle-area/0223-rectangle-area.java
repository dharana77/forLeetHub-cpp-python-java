class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        int biggerLeftX = Math.max(ax1, bx1);
        int biggerLeftY = Math.max(ay1, by1);
        int smallerRightX = Math.min(ax2, bx2);
        int smallerRightY = Math.min(ay2, by2);
        
        // System.out.printf("%d%d%d%d", biggerLeftX, biggerLeftY, smallerRightX, smallerRightY);
        int same = (smallerRightX - biggerLeftX) * (smallerRightY - biggerLeftY);
        
        int sq1 = (ax2-ax1) * (ay2-ay1);
        int sq2 = (bx2-bx1) * (by2-by1);
        
        System.out.println(sq1);
        System.out.println(sq2);
        System.out.println(same);
        
        int answer = 0;
        boolean case1 = ax1 >=bx1 && ay1 >= by1 && ax1 <= bx2 && ay1 <= by2;
        boolean case2 = ax2 >=bx1 && ay1 >= by1 && ax2 <= bx2 && ay2 <= by2;
        boolean case3 = bx1 >= ax1 && by1 >= ay1 && bx1 <= ax2 && by1 <= ay2;
        boolean case4 = bx2 >= ax1 && by2 >= ay1 && bx2 <= ax2 && by2 <= ay2;
        boolean case5 = bx1 <= ax2 && bx2 >= ax1 && by1 <= ay2 && by2 >= ay1;
        
        if ( case1 || case2 || case3 || case4 || case5){
            answer = sq1 + sq2 - same;
        }else{
            answer = sq1 + sq2;
        }
        return answer;
    }
}