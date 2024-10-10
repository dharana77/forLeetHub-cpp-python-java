class Solution {
public:
    bool isPalindrome(string s) {
        
        string target = "";
        for(int i=0; i<s.size(); i++){
            if(isalpha(s[i]) || isdigit(s[i])){
                target += tolower(s[i]);
            }
        }
        // cout << target << endl;
        
        if(target.size() == 0){
            return true;
        }
        
        for(int i=0; i<target.size()/2 + 1; i++){
            if(target[i] != target[target.size() - 1 - i]){
                return false;
            }
        }
        return true;
    }
};