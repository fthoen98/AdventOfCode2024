def read_input(file_path: str):
    """
    Reads a file and processes its contents into a list of lists of integers.

    Args:
        file_path (str): The path to the input file.

    Returns:
        list of list of int: A list where each element is a list of integers
        representing a line in the file.
    """
    with open(file_path, "r") as f:
        data = []
        for line in f:
            if line.strip():
                report = line.split()
                data.append(list(map(int, report)))
        return data


def count_safe_reports(data: list[list[int]]):
    """
    Counts the number of safe reports in a list of reports.

    Args:
        data (list of list of int): A list where each element is a list of integers
        representing a report.

    Returns:
        int: The number of safe reports.
    """
    firstSort = [
        report
        for report in data
        if sorted(report) == report or sorted(report, reverse=True) == report
    ]
    return sum(
        (
            1
            if all(1 <= abs(a - b) <= 3 for a, b in zip(report, report[1:]))
            else 0
        )
        for report in firstSort
    )
