package com.example;

import java.util.Arrays;

public class main {
    public static void main(String[] args) {
        System.out.println(stringCompression("aabcccccaaa"));
    }

    public static String stringCompression(String s) {
        char[] result = new char[s.length()];
        int pos = 0;
        int i = 0;
        while (i < s.length()) {
            char a = s.charAt(i);
            int count = 0;
            while (a == s.charAt(i) && i < s.length() - 1) {
                i++;
                System.out.println(i);
                count++;
            }
            result[pos++] = a;
            result[pos++] = (char) count;
        }
        return Arrays.toString(result);

    }

}
