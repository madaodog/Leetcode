const topKFrequent = (nums, k) => {
    countHashMap = {};
    indexList = [];
    res = [];

    for(let j = 0; j <= nums.length; j++) {
        indexList.push([]);
    }

    for(let i = 0; i < nums.length; i++) {
        if(countHashMap.hasOwnProperty(nums[i])) {
            countHashMap[nums[i]] += 1;
        } else {
            countHashMap[nums[i]] = 1;
        }
    }

    for(let h = 0; h < nums.length; h++) {
        if(!indexList[countHashMap[nums[h]]].includes(nums[h])) {
            indexList[countHashMap[nums[h]]].push(nums[h]);
        }
    }

    for(let i = indexList.length - 1; i >= 0; i--) {
        if(indexList[i].length > 0) {
            res.push(...indexList[i])
        }
        if(res.length == k) {
            return res;
        }
    }

}

console.log(topKFrequent([-1,-1], 1));

