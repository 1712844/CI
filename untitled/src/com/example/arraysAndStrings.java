package com.example;

public interface arraysAndStrings {
    public static boolean isUniqueChars(String str) {
        if (str.length() > 128) {
            return false;
        }

        boolean[] char_set = new boolean[128];

        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i);
            if (char_set[val]) {
                return false;
            }
            char_set[val] = true;
        }
        return true;
    }

    public static boolean checkPermutation(String s1, String s2) {
        if ((s1.length() != s2.length()) || (s1.length() > 128) ) {
            return false;
        }

        int[] letterCount = new int[128];
        char[] s1_array = s1.toCharArray();
        char[] s2_array = s2.toCharArray();
        for (char c : s1_array) {
            letterCount[c]++;
        }

        for (char c: s2_array) {
            letterCount[c]--;
            if (letterCount[c] < 0) {
                return false;
            }
        }
        return true;
    }
}
