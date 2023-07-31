/**
 * 141. Linked List Cycle
 * Source: https://leetcode.com/problems/linked-list-cycle/
 */

var hasCycle = (head) => {
    let pointer1 = head;
    let pointer2 = head;
    while(pointer2 && pointer2.next && pointer2.next.next) {
        pointer1 = pointer1.next;
        pointer2 = pointer2.next.next;
        if(pointer1 === pointer2) {
            return true;
        } 
    }
    return false;
}