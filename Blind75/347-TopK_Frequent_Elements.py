from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        cntToVals = collections.defaultdict(list)

        for val, cnt in counter.items():
            cntToVals[cnt].append(val)

        cnts =[-cnt for cnt in cntToVals.keys()]
        heapq.heapify(cnts)

        res = []
        for i in range(len(cnts)):
           next_cnt = - heapq.heapop(cnts) 
           for num in cntToVals[next_cnt]:
            if len(res) == k: return res
            res.append(num)
        return res
        