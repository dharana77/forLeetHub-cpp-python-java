/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newList = new ListNode();
        ListNode* pt = newList;
        
        while(list1 != NULL && list2 != NULL){
            if(list1->val <= list2->val){
                pt -> next = list1;
                list1 = list1 ->next;   
            }else{
                pt->next = list2;
                list2 = list2->next;
            }
            pt = pt->next;
        }
        if(list1 != NULL){
            pt->next = list1;
        }else if(list2 != NULL){
            pt->next = list2;
        }
        return newList->next;
    }
};