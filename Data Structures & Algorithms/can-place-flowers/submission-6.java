class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int numFlowers = 0;
        int[] flowers = new int[flowerbed.length + 2];

        for (int i = 1; i <= flowerbed.length; i++) {
            flowers[i] = flowerbed[i-1];
        }


        for (int i = 1; i <= flowerbed.length; i++) {
            if (flowers[i] == 0 && flowers[i-1] == 0 && flowers[i+1] == 0){
                flowers[i] = 1;
                numFlowers += 1;
            }
        }
        if (numFlowers >= n){
            return true;
        }
        else{
            return false;
        }
    }
}