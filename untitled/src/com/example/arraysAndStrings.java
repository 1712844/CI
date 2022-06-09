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

    public static char[] urlFy(char[] input, int len) {
        if (input.length == 0 || input.length < len) {
            return input;
        }
        int inputLen = input.length - 1;
        int pointer = len - 1;
        int runner = 0;
        while (pointer > -1) {
            if (input[pointer] != ' ') {
                input[inputLen - runner] = input[pointer];
            } else {
                input[inputLen - runner] = '0';
                input[inputLen - runner - 1] = '2';
                input[inputLen - runner - 2] = '%';
                runner = runner + 2;
            }
            runner++;
            pointer--;
            System.out.println(input);
        }
        return input;
    }

    //1.4
    public static boolean palindromePermutation(String str) {
        int countOdd = 0;
        int[] table = new int[Character.getNumericValue('z') -
                Character.getNumericValue('a') + 1];
        for (char c : str.toCharArray()) {
            int val = getCharNumber(c);
            if (val != -1) {
                table[val]++;
                if(table[val] % 2 == 1) {
                    countOdd++;
                } else {
                    countOdd--;
                }
            }
        }
        return countOdd <= 1;
    }

    public static int getCharNumber(int c) {
        int a = Character.getNumericValue('a');
        int z = Character.getNumericValue('z');
        int val = Character.getNumericValue(c);
        if (val <= z && val >= a) {
            return val - a;
        }
        return -1;
    }

    //1.5
    public static boolean oneAway(String str1, String str2) {
        if (Math.abs(str1.length() - str2.length()) >=2) {
            return false;
        }

        String s1 = str1.length() < str2.length() ? str1 : str2;
        String s2 = str1.length() < str2.length() ? str2 : str1;

        int idx1 = 0;
        int idx2 = 0;
        boolean dif = false;
        while (idx1 < s1.length() && idx2 < s2.length()) {
            if (s1.charAt(idx1) != s2.charAt(idx2)) {
                if (dif) {
                    return false;
                }
                dif = true;
                if (s1.length() == s2.length()) {
                    idx1++;
                }
            } else {
                idx1++;
            }
            idx2++;
        }
        return true;
    }

    //1.6
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

    //1.7
    public static boolean rotateMatrix(int[][] matrix) {
        if (matrix.length == 0 | matrix.length != matrix[0].length) {
            return false;
        }
        int n = matrix.length;
        for (int layer = 0; layer < n/2; layer++) {
            int first = layer;
            int last = n - 1 - layer;
            for (int i = first; i < last; i++) {
                int offset = i - first;
                int top = matrix[first][i];
                matrix[first][i] = matrix[last - offset][first];
                matrix[last-offset][first] = matrix[last][last-offset];
                matrix[last][last-offset] = top;
            }
        }
        return true;
    }
}
