import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class AlgorithmComparison {
    public static void main(String args[]) {

        int size = 10000;
        int arr[] = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = (int) (Math.random() * 1000);
        }

        System.out.println("Number of elements in the array: " + size);
        System.out.println("\nElements randomly distributed : ");
        System.out.println("\nSorting Algorithm\tTime Taken(ns)");
        compareSortingAlgorithms(arr);
        System.out.println();
//        System.out.println("\nElements already sorted : ");
//        System.out.println("\nSorting Algorithm\tTime Taken(ns)");
//        Arrays.sort(arr);
//        compareSortingAlgorithms(arr);

//        System.out.println("\nElements sorted in reverse order : ");
//        System.out.println("\nSorting Algorithm\tTime Taken(ns)");
//        for (int i = 0; i <= arr.length / 2; i++) {
//            int t = arr[i];
//            arr[i] = arr[size - i - 1];
//            arr[size - i - 1] = t;
//        }
//        compareSortingAlgorithms(arr);

        for (int n = 0; n <= 10000; n += 1000 ) {
            long time = System.nanoTime();
            //  HeapSort.heapSort(array);
            //  MergeSort.mergeSort(array, 0 , array.length-1);
            //  QuickSort.quickSort(arr, 0, arr.length - 1);

            PigeonholeSort.pigeonhole_sort(arr, arr.length);

            time = System.nanoTime() - time;

            System.out.printf("n = %d -> time = %d ns%n", n, time);
        }
    }

    private static void compareSortingAlgorithms(int arr[]) {
//        printSortingTime(SortType.ODDEVEN, arr);
        printSortingTime(SortType.HEAP, arr);
        printSortingTime(SortType.MERGE, arr);
        printSortingTime(SortType.QUICK, arr);
        printSortingTime(SortType.PIGEON, arr);

    }

    private static void printSortingTime(SortType sortType, int[] arr) {

        int arr2[] = new int[arr.length];
        System.arraycopy(arr, 0, arr2, 0, arr.length);

        long startTime = System.nanoTime();

        switch (sortType) {
            case HEAP:
                HeapSort.heapSort(arr2);
                break;
            case MERGE:
                MergeSort.mergeSort(arr2, 0, arr2.length - 1);
                break;
            case QUICK:
                QuickSort.quickSort(arr2, 0, arr2.length - 1);
                break;
            case PIGEON:
                PigeonholeSort.pigeonhole_sort(arr2, arr2.length);
                break;

        }

        long endTime = System.nanoTime();
        long duration = endTime - startTime;

        System.out.printf("%-17s %15d %n", sortType + "_Sort", duration);
    }
}
