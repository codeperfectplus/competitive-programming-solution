function modifyArray(nums) {
    // iterate through the array
    for(let i=0;i<nums.length;i++) {
         // all even elements are doubled
         if(nums[i] % 2 == 0){
             nums[i]*=2;
         // all odd elements are tripled
          }else{
              nums[i]*=3;
          }
              
         }  
        // return array 
       return nums;
    }
