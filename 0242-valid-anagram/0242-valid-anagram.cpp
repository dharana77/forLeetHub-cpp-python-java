#include<map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> sm;
        map<char, int> tm;
        
        for(int i=0; i< s.size(); i++){
            sm[s[i]] += 1;
        }
        for(int i=0; i<t.size(); i++){
            tm[t[i]] += 1;
        }
        
        for(auto i=sm.begin(); i!=sm.end(); i++){
            char key = i->first;
            int value = i->second;
            if(tm[key] != value || tm[key] == 0){
                return false;
            }
        }
        for(auto i=tm.begin(); i!=tm.end(); i++){
            char key = i->first;
            int value = i->second;
            if(value != sm[key] || sm[key] == 0){
                return false;
            }
        }
        return true;
    }
};