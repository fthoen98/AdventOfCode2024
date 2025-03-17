def read_input(file_path: str):
    with open(file_path, "r") as f:
        data = []
        for line in f:
            if line.strip():
                report = line.split()
                data.append(list(map(int, report)))
                print(data)
        return data


def count_safe_reports(data):
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


if __name__ == "__main__":
    file_path = "data.txt"
    data = read_input(file_path)
    nb_safe_reports = count_safe_reports(data)
    # print(f"The number of safe report is {nb_safe_reports}\n")
