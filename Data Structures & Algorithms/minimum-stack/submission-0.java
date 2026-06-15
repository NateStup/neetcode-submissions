class MinStack {
    private java.util.ArrayList<int[]> stack;

    public MinStack() {
        this.stack = new java.util.ArrayList<>();
    }
    
    public void push(int val) {
        if (this.stack.isEmpty()) {
            this.stack.add(new int[]{val, val});
        }
        else {
            int currentMin = this.stack.get(this.stack.size() - 1)[1];
            int newMin = Math.min(currentMin, val);
            this.stack.add(new int[]{val, newMin});
        }
    }
    
    public void pop() {
        if (!this.stack.isEmpty()) {
            this.stack.remove(this.stack.size() - 1);
        }
    }
    
    public int top() {
        return this.stack.get(this.stack.size() - 1)[0];
    }
    
    public int getMin() {
        return this.stack.get(this.stack.size() - 1)[1];    }
}
