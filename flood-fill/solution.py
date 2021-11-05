class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        orgColor = image[sr][sc]
        if (orgColor == newColor):
            return image

        M, N = len(image), len(image[0])
        queue = [(sr, sc)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while(queue):
            y,x = queue.pop(0)
            image[y][x] = newColor
            for delta in directions:
                dy = y + delta[0]
                dx = x + delta[1]
                if ((0 <= dy < M) and
                    (0 <= dx < N) and
                    (image[dy][dx] == orgColor)):
                    queue.append((dy, dx))
        return image
