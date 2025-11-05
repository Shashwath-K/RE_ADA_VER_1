package Basics.Arrays;
import java.lang.*;

public class Ex_1_arrays {
    public static void main (String args[]) {
        int arr[] = { 1, 2, 3, 4, 5 };
        char charr[] = { 'a', 'b', 'c', 'd', 'e' };
        float farr[] = { 1.4f, 2.0f, 24f, 5.0f, 0.0f };
        System.out.println("Integer Array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\nCharacter Array: ");
        for (int i = 0; i < charr.length; i++) {
            System.out.print(charr[i] + " ");
        }
        System.out.println("\nFloat Array: ");
        for (int i = 0; i < farr.length; i++) {
            System.out.print(farr[i] + " ");
        }
    }
}