class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l =0;
        int r = numbers.length -1;
        int num_a ;
        int num_b ;
        while(l<r){
            num_a = numbers[l];
            num_b = numbers[r];
            int sum = num_a + num_b;
            if(sum == target){
                break;
            }
            if(sum < target){
                l++;
                continue;
            }
            r--;
            
        

        }

        return  new int[] {l+1,r+1};
    }
}
