package com.example;

public class main {
    public static void main(String[] args) {
        System.out.println(urlFy("Mr John Smith    ".toCharArray(), 13));
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
}
