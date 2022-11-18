class Solution {
    public boolean isUgly(int n) {
        boolean con = true;
        
        if (n==1) return true;
        
        while(n!=1){
            System.out.println(n);
            if(n==2 || n==3 || n== 5) break;
            int temp = isPrime(n);
            if (temp != 2 && temp != 3 && temp !=5){
                return false;
            }
            n /=temp;
            
        }
        
        if (n==2 || n==3 || n==5) return true;
        return false;
    }
    
    public int isPrime(int n){
        for(int i=2; i<= Math.sqrt(n); i++){
            if(n%i == 0){
                return i;
            }
        }
        return n;
    }
}