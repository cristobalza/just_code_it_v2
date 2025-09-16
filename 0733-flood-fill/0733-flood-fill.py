class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        """
        Given a image List[List[int]] - each image[i][j] is pixel color
                sr: int, 
                sc: int, 
                color: int
 
        Flood fill :=  change the color to 'color' on image[sr][sc] and adjacent

        Rules:
        - Begin w starting pixel and change its color to `color`
        - Perform same operation for each ppizel that is directly adjacent (share same side horizontally or vertically_) AND shares the same color as starting pixel
        - Keep repeating process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel 
        - Process stops when there are no more adjacent pixels
            

        dfs(r, c, original_pixel)

            check if r and c are in bound and if the (r,c) has not been visited before and if the image[r][c]== 0

                keep exploring 
        """

        def dfs(r, c, original_pixel):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and image[r][c] == original_pixel:

                visited.add((r, c))

                image[r][c] = color


                for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    dfs(_r, _c, original_pixel)

            return

        visited = set()
        ROWS, COLS = len(image), len(image[0])

        dfs(sr, sc, image[sr][sc])

        return image





        