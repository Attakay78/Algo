class Main {
  public static void main(String[] args) {
    // Dynamic Array Testing
    // DynamicArray arr = new DynamicArray(2);
    // arr.insert(3);
    // arr.insert(4);

    // arr.print();
    // System.out.println("length= " +arr.len());

    // arr.remove();
    // arr.removeAt(0);
    // arr.print();


    // LinkedList Testing
    var linkedList = new LinkedList();
    linkedList.addLast(20);
    linkedList.addLast(78);
    linkedList.addFirst(100);
    linkedList.addFirst(5);
    // linkedList.deleteFirst();

    // System.out.println(linkedList.indexOf(78));
    // linkedList.deleteLast();
    // System.out.println(linkedList.len());
    // System.out.println(linkedList.contains(78));

    // linkedList.reverse();
    // linkedList.printMiddle();
    linkedList.createLoop();
    System.out.println(linkedList.hasLoop());
  }
}
