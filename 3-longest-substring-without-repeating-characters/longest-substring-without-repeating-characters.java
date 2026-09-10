class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLength = 0;
        Set<Character> seen = new HashSet();

        for (int right = 0; right < s.length(); right ++) {
            char curr = s.charAt(right);

            while (seen.contains(curr)) {
                seen.remove(s.charAt(left));
                left ++;
            }

            seen.add(curr);
            maxLength = Math.max(maxLength, right - left + 1);

        }   
        return maxLength;
    }
}