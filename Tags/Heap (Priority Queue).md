

## Algorithm 

- AVL Tree 
- Add new item 
	- Add item at the end 
	- While the added item is less than the parent, swap item and parent 
		- Bubble up / heapify up 
- Remove item 
	- Return the item at index 0 
	- Replace index 1 with the last index
	- While the item is greater than its children, swap the item with its smallest child 
		-  heapify down
## Code 

```java 
  
import java.util.Arrays;  
  
public class MinHeap<E extends Comparable<E>> {  
    private int size;  
  
    private E[] items;  
  
  
    public MinHeap() {  
        this(10);  
    }  
  
    public MinHeap(int capacity) {  
        this.size = 0;  
        @SuppressWarnings("unchecked")  
        var array = (E[]) new Comparable[capacity];  
        this.items = array;  
    }  
  
    private static int getLeftChildIndex(int parentIndex) {  
        return 2 * parentIndex + 1;  
    }  
  
    private static int getRightChildIndex(int parentIndex) {  
        return 2 * parentIndex + 2;  
    }  
  
    private static int getParentIndex(int childIndex) {  
        return (childIndex - 1) / 2;  
    }  
  
    private boolean hasLeftChild(int index) {  
        return getLeftChildIndex(index) < size;  
    }  
  
    private boolean hasRightChild(int index) {  
        return getRightChildIndex(index) < size;  
    }  
  
    private boolean hasParent(int index) {  
        return getParentIndex(index) >= 0;  
    }  
  
    private E leftChild(int index) {  
        return this.items[getLeftChildIndex(index)];  
    }  
  
    private E rightChild(int index) {  
        return this.items[getRightChildIndex(index)];  
    }  
  
    private E parent(int index) {  
        return this.items[getParentIndex(index)];  
    }  
  
    private void swap(int first, int second) {  
        E temp = this.items[first];  
        this.items[first] = this.items[second];  
        this.items[second] = temp;  
    }  
  
    private void ensureExtraCapacity() {  
        if (size == items.length) {  
            items = Arrays.copyOf(items, items.length * 2);  
        }  
    }  
  
    private E peek() {  
        if (size == 0) throw new IllegalStateException();  
        return items[0];  
    }  
  
    public E poll() {  
        if (size == 0) throw new IllegalStateException();  
        E item = items[0];  
        items[0] = items[size - 1];  
        size--;  
        heapifyDown();  
        return item;  
    }  
  
  
    public void add(E item) {  
        ensureExtraCapacity();  
        items[size] = item;  
        size++;  
        heapifyUp();  
    }  
  
    private void heapifyUp() {  
        int index = size - 1;  
        while (hasParent(index) && parent(index).compareTo(items[index]) > 0) {  
            swap(getParentIndex(index), index);  
            index = getParentIndex(index);  
        }  
    }  
  
    private void heapifyDown() {  
        int index = 0;  
        while (hasLeftChild(index)) {  
            int smallerChildIndex = getLeftChildIndex(index);  
            if (hasRightChild(index) && rightChild(index).compareTo(leftChild(index)) < 0) {  
                smallerChildIndex = getRightChildIndex(index);  
            }  
  
            if (items[index].compareTo(items[smallerChildIndex]) < 0) {  
                break;  
            } else {  
                swap(index, smallerChildIndex);  
            }  
            index = smallerChildIndex;  
  
        }  
    }  
}


```