public class Solution {
    public int Reverse(int x) {
        int max = (int)Math.Pow(2, 31)-1;        
        int tmp, rem, ans = 0;
        while(x != 0){
            rem = x % 10;            
            x = x / 10;
            if (ans > max/10 || ans == max/10 && rem > 7)
                return 0;
            if(ans < -1*(max+1)/10 || (ans == -1*(max+1)/10 && rem < -8))
                return 0;
            ans = ans * 10 + rem;     
        }
        return ans;
    }
}

