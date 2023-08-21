public class DynamicArray{
  private int arr_size;
  private int[] arr;
  private int[] dynamic_arr;
  private int count = 0;
  
  public DynamicArray(int arr_size){
    this.arr_size = arr_size;
    this.arr = new int[this.arr_size];
  }

  public void insert(int item){
    if (this.count < this.arr_size){
      this.arr[this.count] = item;
      this.count += 1;
    }else{
      this.dynamic_arr = new int[this.arr_size];
      this.dynamic_arr = this.arr;
      this.arr_size *= 2;
      this.arr = new int[this.arr_size];
      for(int num =0; num < this.count; num++){
        this.arr[num] = this.dynamic_arr[num];
      }
      this.arr[this.count] = item;
      this.count +=1;
    }   
  }

  public void print(){
    for(int i=0; i<count; i++){
      System.out.println(this.arr[i]);
    }
  }

  public int len(){
    return this.arr.length;
  }

  public void remove(){
    if (count == 0){
      System.out.println("No item in array");
    }else{
      this.count -= 1;
    }
  }

  public void removeAt(int index){
    if (index < 0 || index >= this.count){
      System.out.println("Index out of range");
    }else{
      for(int i=index; i < this.count; i++){
        this.arr[i] = this.arr[i+1];
      }

      this.count -= 1;
    }
  }
}
