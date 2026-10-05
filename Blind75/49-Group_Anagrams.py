class Solution(object):
    def groupAnagrams(self, strs):

        hm =collections.defaultdict(list)

        for s in strs:
            hash = str(sorted(list(s)))
            hm[hash].append(s)

        return hm.values()    