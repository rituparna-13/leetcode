// Given the head of a linked list, remove the nth node from the end of the list and return its head. 
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // Input: head of the ListNode and the node n to remove.
    // Output: return the head of the ListNode after removing node n.
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;

        // Using ListNode fast as a reference to reach till Node n
        for (int i = 0; i < n; i++) fast = fast.next;

        // Remove the node n by changing the pointer or moving fast to fast.next
        while (fast != null) {
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }

        // case: delete first node
        if (slow == head) return head.next; 
        // case: delete last node
        if (slow.next == null) prev.next = null; 
		
        prev.next = slow.next;
        return head;
    }
}
