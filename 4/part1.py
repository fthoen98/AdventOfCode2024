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
        return ["".join(line.strip()) for line in f]


def count_occurences(matrix: list[str]) -> int:
    """
    Description:
        Thus function return the number of XMAS or SAMX occurences
        inside a list of string

    Args:
        matrix (list[str]): list of strings(matrix) in which we look
        for XMAS|SAMX occurences

    Returns:
        int: Number of XMAS|SAMX occurences
    """
    pattern = r"(?=(XMAS|SAMX))"
    return sum(len(re.findall(pattern, string)) for string in matrix)


def count_matrix_words(matrix: list[str]):
    """
    Description:
        This function processes a matrix to count occurrences of XMAS and SAMX in
        horizontal, vertical, and diagonal directions.

    Args:
        matrix (list[str]): The matrix containing characters.

    Returns:
        int: Total count of occurrences in all directions.
    """
    n = len(matrix)
    m = len(matrix[0])
    nDiags = n + m - 1  # Number of diagonal lines

    # Initialize lists to store vertical and diagonal words
    vertWords = [""] * m
    diagLeftRightWords = [""] * nDiags
    diagRightLeftWords = [""] * nDiags

    # Iterate through the matrix to extract words in all directions
    for i, string in enumerate(matrix):
        reverseMatrix = string[
            ::-1
        ]  # Reverse string for diagonal calculations
        for j, char in enumerate(string):
            vertWords[j] += char  # Build vertical words
            diag_idx = i - j + n - 1  # compute normlized diag offsets
            diagLeftRightWords[
                diag_idx
            ] += char  # Build diagonal words from left to right
            diagRightLeftWords[diag_idx] += reverseMatrix[
                j
            ]  # Build diagonal words from right to left

    # Sum occurrences in all directions
    return count_occurences(
        matrix + vertWords + diagLeftRightWords + diagRightLeftWords
    )


if __name__ == "__main__":
    filePath = "data.txt"
    data = readData(filePath)
    print(count_matrix_words(data))
    # print(f"The result is {res}.")
