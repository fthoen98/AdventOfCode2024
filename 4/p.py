import re


def readData(data) -> list[str]:
    """
    Description:
        This function reads input data contained inside a txt file
        and returns a matrix.

    Args:
        data(file path: str): Contains the file patht to input data

    Returns:
        matrix(lis[str]): Array containing string. This represents the matrix in
        which we need to find XMAS or SAMX occurences in all direcions.
    """
    with open(data, "r") as f:
        matrix = []
        for line in f:
            matrix.append("".join(line.strip()))
        return matrix


def count_(row: str) -> int:
    """
    Description:
        This function counts the XMAS and SAMX occurrences inside a string.

    Args:
        row (str):

    Returns:
        count(int): Count of occurrences.
    """
    count = 0
    pattern = r"(?=(XMAS|SAMX))"
    count += len(re.findall(pattern, row))
    return count


def count_strList(tab: list[str]) -> int:
    """
    Description:
        This function counts the occurrences of XMAS and SAMX in a list of strings.

    Args:
        tab (list[str]): List of strings to be analyzed.

    Returns:
        cnt(int): Total count of occurrences.
    """
    cnt = 0
    for str in tab:
        cnt += count_(str)
    return cnt


def wordsBuilding(matrix: list[str]):
    """
    Description:
        This function processes a matrix to count occurrences of XMAS and SAMX in
        horizontal, vertical, and diagonal directions.

    Args:
        matrix (list[str]): The matrix containing characters.

    Returns:
        int: Total count of occurrences in all directions.
    """
    hCnt = 0
    n = len(matrix)
    m = len(matrix[0])
    nDiags = (1 + (n - 1) * 2) - 2  # Number of diagonal lines

    # Initialize lists to store vertical and diagonal words
    vertWords = [""] * m
    diagLeftRightWords = [""] * nDiags
    diagRightLeftWords = [""] * nDiags

    # Iterate through the matrix to extract words in all directions
    for i, string in enumerate(matrix):
        hCnt += count_(string)  # Count horizontal occurrences
        reverseMatrix = "".join(
            list(reversed(string))
        )  # Reverse string for diagonal calculations
        for j in range(m):
            vertWords[j] += matrix[i][j]  # Build vertical words

            # Avoid out-of-bounds diagonal processing for corner cases
            if (i == n - 1 and j == 0) or (i == 0 and j == m - 1):
                pass
            else:

                diagLeftRightWords[i - j] += matrix[i][j]  
                # Build diagonal words from left to right
                diagRightLeftWords[i - j] += reverseMatrix[j] 
                # Build diagonal words from right to left

    # Sum occurrences in all directions
    return (
        hCnt
        + count_strList(vertWords)
        + count_strList(diagLeftRightWords)
        + count_strList(diagRightLeftWords)
    )


if __name__ == "__main__":
    filePath = "data.txt"
    data = readData(filePath)
    print(wordsBuilding(data))
    # print(f"The result is {res}.")
