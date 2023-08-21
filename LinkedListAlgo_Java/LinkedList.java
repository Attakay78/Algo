public class LinkedList{
  private class Node{
    private int value;
    private Node next;

    private Node(int value){
      this.value = value;
    }
  }

  private Node first;
  private Node last;

  private boolean isEmpty(){
    return first == null;
  }

  public void addLast(int item){  
    var node = new Node(item);
    if(isEmpty()){
      first = last = node;
    }else{
      last.next = node;
      last = node;
    }
  }

  public void addFirst(int item){
    var node = new Node(item);
    if(isEmpty()){
      first = last = node;
    }else{
      node.next = first;
      first = node;
    }    
  }

  public void deleteFirst(){
    if(isEmpty()){
      System.out.println("LinkedList is empty");
    }else if(first == last){
      first = last = null;
      return;
    }
    else{
      var second = first.next;
      first.next = null;
      first = second;
    }
  }

  public int indexOf(int item){
    int count = 0;
    Node current = first;
    while(current != null){
      if (current.value == item) return count;
      current = current.next;
      count += 1;
    }
    return -1;
  }

  // Implement the more efficient way, current implementation is o(n)
  // Find a way to make it o(1) by storing count of items whenever
  // items are added and removed from the list.
  public int len(){
    int count = 0;
    Node current = first;
    while(current != null){
      current = current.next;
      count += 1;
    }
    return count;
  }

  public boolean contains(int item){
    Node current = first;
    while(current != null){
      if (current.value == item) return true;
      current = current.next;
    }
    return false;
  }

  public void deleteLast(){
    if(isEmpty()){
      System.out.println("LinkedList is empty");
    }else if(first == last){
      first = last = null;
    }
    else{
      Node current = first.next;
      Node previous = first;
      while(current != null){
        if(current.next == null){
          last = previous;
          last.next = null;
          return;
        }
        previous = current;
        current = current.next;
      }
    }
  }

  public void reverse(){
    // Store first current value as first
    Node current = first;
    Node previous_node = null;
    while(current != null){
      Node next_node = current.next;

      // if linkedList has only one node
      // do nothing
      if(current == last){
        return;
      }
      // check if next node is null (if last node is found)
      // set that node as first and it's next node as prev node
      else if(next_node == null){
        current.next = previous_node;
        first = current;
      }
        // if first node is found
        // set that node as last node and 
        // set it's next node as null
      else if(current == first){
        current.next = null;
        last = current;
      }
        // if node is in the middle
        // set it's next node to the prev node
      else{
        current.next = previous_node;
      }
      previous_node = current;
      current = next_node;     
    }
  }

  public void printMiddle(){
    // check if it's empty
    if(isEmpty()){
      System.out.println("List is empty");
      return;
    }

    // set both slow and fast pointer to first node
    Node slow_ptr = first;
    Node fast_ptr = first;

    // Check if both fast_ptr and it's next are not equal to last
    // when fast_ptr == last, linkedList is odd
    // when fast_ptr.next == last, linkedList is even
    // Note: this also checks if the list has 1 or 2 nodes only
    while( (fast_ptr != last) && (fast_ptr.next != last) ){
      slow_ptr = slow_ptr.next;
      fast_ptr = fast_ptr.next.next;
    }
    if(fast_ptr == last){
      System.out.println("Middle node: "+ slow_ptr.value);
    }else{
      System.out.println("Middle nodes: "+ slow_ptr.value + " and " + slow_ptr.next.value);
    }
    
  }

  public boolean hasLoop(){
    // Using Floyd's Cycle-Finding Algorithm

    Node slow_ptr = first;
    Node fast_ptr = first;

    while( (fast_ptr.next != null) && (fast_ptr.next.next !=null) ){
      slow_ptr = slow_ptr.next;
      fast_ptr = fast_ptr.next.next;

      if(slow_ptr == fast_ptr){
        return true;
      }
    }
    return false;
  }

  // creating a loop to test hasLoop() method
  public void createLoop(){
    Node new_node = new Node(-7);
    last.next = new_node;
    new_node.next = first;
  }
  
  // Find the kth node from the end of a linkedList in one pass
  // Strategy:
  // Use two pointers where the last pointer is 
  // k-1 from the first pointer
  // Move till you get to the end of the list and the node the
  // first pointer points to is the kth node
}
