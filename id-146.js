/**
 * 146. LRU Cache
 * Source: https://leetcode.com/problems/lru-cache/
 */

class Node {
    constructor(key, value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}
/**
 * Have to use count otherwise you need Object.key(cache).length which is O(n) (>> O(1))
 */
class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = {};
        this.left = new Node(0,0);  
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left; 
        this.count = 0;
    }

    addNode(node) {
        let prev = this.right.prev;
        let next = this.right
        prev.next = node;
        this.right.prev = node;
        node.next = next;
        node.prev = prev;
        this.count++;
    }

    removeNode(node) {
        let prev = node.prev;
        let next = node.next;
        prev.next = next;
        next.prev = prev;
        this.count--;
    }

    get(key) {
        if(this.cache[key]) {
            this.removeNode(this.cache[key]);
            this.addNode(this.cache[key]);
            return this.cache[key].value;
        } else {
            return -1;
        }
    }

    put(key, value) {
        if(this.cache[key]) {
            this.removeNode(this.cache[key]); }
        this.cache[key] = new Node(key, value);
        this.addNode(this.cache[key]);

        if(this.count > this.capacity) {
            let deletedNode = this.left.next;
            this.removeNode(deletedNode);
            delete this.cache[deletedNode.key];
            }
    }
        


}
