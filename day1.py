from utils.read import read_file

def part_one(_input):
    left = []
    right = []
    for line in _input:
        split_line = line.split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    left.sort()
    right.sort()
    distance = []
    for i in range(len(left)):
        distance.append(abs(left[i] - right[i]))

    print(f"The total distance between the 2 lists is: {sum(distance)}")


def part_two(_input):
    left = []
    right = []
    for line in _input:
        split_line = line.split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    left.sort()
    similarity = []
    for i in range(len(left)):
        occurance = right.count(left[i])
        similarity.append(left[i] * occurance)


    print(f"The similarity score is: {sum(similarity)}")


if __name__ == "__main__":
    stringInput = read_file(1, "string", False)
    part_one(stringInput)
    part_two(stringInput)
