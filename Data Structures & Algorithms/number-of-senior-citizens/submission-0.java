class Solution {
    public int countSeniors(String[] details) {
        int count = 0;
        for(int i = 0; i < details.length; i++){
            String string = new String(details[i].substring(11,13));
            int age = Integer.parseInt(string);
            if (age > 60) {
                count += 1;
            }
        }
        return count;
    }
}