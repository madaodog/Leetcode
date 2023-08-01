/**
 * 2. Add Two Numbers
 * Source: https://leetcode.com/problems/add-two-numbers/
 */


var addTwoNumbers = function(l1, l2) {
    let newList = new ListNode(null, null);
    let current = newList;
    let carry = 0;
    while(l1 || l2 || carry) {
        let sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;

        carry = (sum >=10 ? 1 : 0);

        let newNode = new ListNode((sum >= 10 ? sum-10 : sum), null);
        current.next = newNode;
        current = newNode;

        if(l1) {
            l1 = l1.next;
        }
        if(l2) {
            l2 = l2.next;
        }
    }
    return newList.next;

}