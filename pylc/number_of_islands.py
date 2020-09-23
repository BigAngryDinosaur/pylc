# @lc app=leetcode id=200 lang=python3

from typing import List, Tuple, Generator, TypeVar
from enum import Enum


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        if len(grid) == 0 or len(grid[0]) == 0: return 0

        return self.union_find(grid)

    def dfs_sol(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        num_islands = 0
        visited = [[False] * n for _ in range(m)]

        for i, row in enumerate(grid):
            for j, col in enumerate(row):

                if Terrain(col) is Terrain.LAND and not visited[i][j]:
                    num_islands += 1
                    stack = [(i, j)]

                    while stack:
                        r, c = stack.pop()
                        visited[r][c] = True

                        for nr, nc in neighbours(r, c, grid):
                            if not visited[nr][nc] and Terrain(grid[nr][nc]) is Terrain.LAND:
                                stack.append((nr, nc))


        return num_islands

    def union_find(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        dsu = DSU(grid)

        for i, row in enumerate(grid):
            for j, col in enumerate(row):

                if Terrain(col) is Terrain.LAND:
                    for r, c in neighbours(i, j, grid):
                        if Terrain(grid[r][c]) is Terrain.LAND:
                            a, b = i * n + j,  r * n + c
                            dsu.union(a, b)

        return dsu.num_components


class Terrain(Enum):
    WATER = "0"
    LAND  = "1"

T = TypeVar('T')

def neighbours(r: int, c: int, grid: List[List[T]]) -> Generator[Tuple[int, int], None, None]:
    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
            yield (nr, nc)

class DSU:

    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        node_count = m * n
        self.p = [-1] * node_count
        self.r = [0] * node_count
        self.num_components = 0

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    idx = i * n + j
                    self.p[idx] = idx
                    self.num_components += 1

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False

        if self.r[px] < self.r[py]:
            px, py = py, px

        self.p[py] = px

        if self.r[px] == self.r[py]:
            self.r[px] += 1

        self.num_components -= 1

        return True
