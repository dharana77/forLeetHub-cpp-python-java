import java.util.Queue;
import java.util.LinkedList;

class MyQueue {
    Queue<Integer> q;
    public MyQueue() {
        this.q = new LinkedList<Integer>();
    }
    
    public void push(int x) {
        this.q.add(x);
    }
    
    public int pop() {
        return this.q.poll();
    }
    
    public int peek() {
        return this.q.peek();
    }
    
    public boolean empty() {
        return this.q.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */