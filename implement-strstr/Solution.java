import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.text.*;
import java.util.stream.*;

public class Solution {
    static boolean isDebug = false;

    static int solve(String A, String B) {
        if (A.length() == 0 || B.length() == 0) {
            return -1;
        }
        char[] a = A.toCharArray();
        char[] b = B.toCharArray();
        int l = 0, r = 0;

        while(l + r < a.length) {
            if (a[l + r] == b[r]) {
                if (r + 1 < b.length) {
                    r++;
                } else {
                    return l;
                }
            } else {
                l++;
                r = 0;
            }
        }

        return -1;
    }

    static void solution() {

        try {
            BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
            String A = input.readLine();
            String B = input.readLine();
            System.out.println(solve(A, B));
            input.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    static void test(String caseName, String ans, String input) {
        InputStream stdin = System.in;
        System.setIn(new ByteArrayInputStream(input.getBytes()));

        PrintStream stdout = System.out;
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        if (!isDebug) {
            System.setOut(new PrintStream(out));
        }

        solution();

        System.setIn(stdin);
        System.setOut(stdout);
        String result = out.toString().trim();
        boolean testPassed = ans.trim().equals(result);
        System.out.printf("%s -> %s\n", caseName, testPassed ? "pass" : "fail");
        if (!testPassed) {
            System.out.println(result);
        }

    }


    static void case6() {
        StringBuilder input = new StringBuilder();
        input.append("aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb\n");
        input.append("bba\n");

        StringBuilder ans = new StringBuilder();
        ans.append("13\n");
        test("case6", ans.toString(), input.toString());
    }
    static void case5() {
        StringBuilder input = new StringBuilder();
        input.append("bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba\n");
        input.append("babaaa\n");

        StringBuilder ans = new StringBuilder();
        ans.append("48\n");
        test("case5", ans.toString(), input.toString());
    }
    static void case4() {
        StringBuilder input = new StringBuilder();
        input.append("ABCD\n");
        input.append("\n");

        StringBuilder ans = new StringBuilder();
        ans.append("-1\n");
        test("case4", ans.toString(), input.toString());
    }
    static void case3() {
        StringBuilder input = new StringBuilder();
        input.append("\n");
        input.append("ABCD\n");

        StringBuilder ans = new StringBuilder();
        ans.append("-1\n");
        test("case3", ans.toString(), input.toString());
    }
    static void case2() {
        StringBuilder input = new StringBuilder();
        input.append("THISTISSUEBOXHASTWOISSUES\n");
        input.append("ABCD\n");

        StringBuilder ans = new StringBuilder();
        ans.append("-1\n");
        test("case2", ans.toString(), input.toString());
    }
    static void case1() {
        StringBuilder input = new StringBuilder();
        input.append("THISTISSUEBOXHASTWOISSUES\n");
        input.append("ISSUES\n");

        StringBuilder ans = new StringBuilder();
        ans.append("19\n");
        test("case1", ans.toString(), input.toString());
    }
    public static void main(String[] args) {
        case1();
        case2();
        case3();
        case4();
        case5();
        case6();
    }
}
