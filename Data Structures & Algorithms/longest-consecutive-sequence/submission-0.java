class Solution {
    public int longestConsecutive(int[] nums) {

        if (nums.length == 0) return 0;
        HashSet<Integer> hs = new HashSet<>();
        int longest =0;
        for(int num:nums){
            hs.add(num);
        }
        for(int num : nums){
            if(!hs.contains(num-1)){
                int count =1;
                while(hs.contains(num+1)){
                    count++;
                    num++;


                }
                longest = Math.max(longest, count);    

            }
            if(longest > nums.length/2) break;
        }
        return longest;
        
       
    }
}
