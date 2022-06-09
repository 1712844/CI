package com.example;

import java.util.Arrays;

public class main {
    public static void main(String[] args) {
        System.out.println(stringCompression("aabcccccaaa"));
    }

    public static String stringCompression(String s) {
        StringBuilder compressed = new StringBuilder();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count++;
            if (i + 1 >= s.length() || s.charAt(i) != s.charAt(i+1)) {
                compressed.append(s.charAt(i));
                compressed.append(count);
                count = 0;
            }
        }
        return compressed.length() < s.length() ? compressed.toString() : s;
    }

}
