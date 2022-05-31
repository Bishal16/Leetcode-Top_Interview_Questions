public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        
        var dict = new Dictionary<int, int>();
       
        foreach(int j in nums){
            if (dict.ContainsKey(j))
                dict[j] ++;
            else
                dict[j] = 1;            
        }
        
        //sort desc dictionary by value
        dict = dict.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
        int count =0;
        int[] num = new int[k];
        foreach(int v in dict.Keys){
            if (count<k){
                num[count] = v;
                count++;
            } 
        }
        return num;
    }
}