# Leetcode 1976: Number of Ways to Arrive at Destination
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
import collections
import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        pq = [(0, 0, 0)]
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        while pq:
            d, u, w = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    ways[v] = ways[u]
                    heapq.heappush(pq, (d + w, v, w))
                elif d + w == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % (10 ** 9 + 7)
        return ways[-1] % (10 ** 9 + 7)