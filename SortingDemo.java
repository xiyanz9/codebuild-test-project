public class SortingDemo {
    public static void main(String[] args) {
        // Test array
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("Original Array:");
        printArray(arr);
        
        // Create a copy for bubble sort
        int[] bubbleArr = arr.clone();
        bubbleSort(bubbleArr);
        System.out.println("\nAfter Bubble Sort:");
        printArray(bubbleArr);
        
        // Create a copy for selection sort
        int[] selectionArr = arr.clone();
        selectionSort(selectionArr);
        System.out.println("\nAfter Selection Sort:");
        printArray(selectionArr);
    }
    
    // Bubble Sort Implementation
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    // swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    
    // Selection Sort Implementation
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            int minIdx = i;
            for (int j = i+1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap found minimum element with first element
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }
    
    // Utility method to print array
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
