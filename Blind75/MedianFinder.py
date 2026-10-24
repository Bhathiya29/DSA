import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (store negatives)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to the appropriate half
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Rebalance the heaps
        if len(self.small) > len(self.large) + 1:
            largest_small = -heapq.heappop(self.small)
            heapq.heappush(self.large, largest_small)

        elif len(self.large) > len(self.small):
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0
    