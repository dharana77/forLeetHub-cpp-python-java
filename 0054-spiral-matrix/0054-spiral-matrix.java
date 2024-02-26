import java.util.*;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        
        Integer [] ans = new Integer[row*col];
        
        
        int current = 0;
        int count = 0;
        while(count * 2 <= row){
            for(int i=0+count; i<col-count; i++){
                if (current >= row * col) break;
                ans[current] = matrix[count][i];
                current += 1;
            }

            for(int i=1+count; i<row-count; i++){
                if (current >= row * col) break;
                ans[current] = matrix[i][col-1-count];
                current += 1;
            }

            for(int i=col-2-count; i>0+count; i--){
                if (current >= row * col) break;
                ans[current] = matrix[row-1-count][i];
                current += 1;
            }

            for(int i=row-1-count; i>0+count; i--){
                if (current >= row * col) break;
                ans[current] = matrix[i][0+count];
                current += 1;
            }
            count += 1;
        }
        
        List<Integer> result =  Arrays.asList(ans);
        
        return result;
    }
}