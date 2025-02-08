###########
###PART1###
###########
def total_distance(seq1, seq2):
    return sum(abs(a-b)for a,b in zip(sorted(seq1), sorted(seq2)))

def read_sequences(file_path: str):
    with open(file_path,"r") as f:
        for line in f:
            if line.strip():
                tab = line.split()
                yield int(tab[0]), int(tab[1]) 
                
# if __name__ == "__main__":
#     file_path = "Day1_input.txt"
#     data = read_sequences(file_path)
#     seq1, seq2 = zip(*data)
#     print(f"Total Distance bewteen two lists : {total_distance(seq1, seq2)}")

###########
###PART2###
###########

def total_similarity(seq1, seq2):
    return sum(i * seq2.count(i) for i in seq1)

if __name__ == "__main__":
    file_path = "Day1_input.txt"
    data = read_sequences(file_path)
    seq1, seq2 = zip(*data)
    # seq1 = [3,4,2,1,3,3]
    # seq2 = [4,3,5,3,9,3]
    print(f"Total Similarity bewteen two lists : {total_similarity(seq1, seq2)}")