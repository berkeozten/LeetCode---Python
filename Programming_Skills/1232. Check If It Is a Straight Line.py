class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if coordinates[1][0] - coordinates[0][0] != 0:
            m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for ix in range(1,len(coordinates) - 1):
                if coordinates[ix + 1][0] - coordinates[ix][0] != 0:
                    if (coordinates[ix + 1][1] - coordinates[ix][1]) / (coordinates[ix + 1][0] - coordinates[ix][0]) != m:
                        return False
                else:
                    return False
        else:
            for ix in range(1,len(coordinates) - 1):
                if coordinates[ix + 1][0] - coordinates[ix][0] != 0:
                    return False

        return True
