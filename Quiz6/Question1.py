NUM_RECORDS = 3
SCORE_BEGIN_INDEX = 2
SCORE_END_INDEX = 6
NUM_SCORE = SCORE_END_INDEX - SCORE_BEGIN_INDEX
TOTAL_SCORE_INDEX = 6
def add_total_score(data):
    for r in data:
        total = 0
        for i in range(SCORE_BEGIN_INDEX, SCORE_END_INDEX):
            total = total + r[i]
        r.append(total)
def read_input(n):
    data = []
    for i in range(n):
        user_input = input("Student Record (ID, Name, Scores): ").split()
    for j in range(SCORE_BEGIN_INDEX,SCORE_END_INDEX):
            user_input[j] = int(user_input[j])

        data.append(user_input)

    return data
def print_all(data):
    for r in data:
        for i in range(0, SCORE_END_INDEX):
            print(r[i], end=' ')
        total = r[TOTAL_SCORE_INDEX]
        avg = total /NUM_SCORE
        print("Total: {0} Avg: {1}".format(total, avg))
def find_highest_score(data):
    max_score_idx = 0
    for idx, r in enumerate(data):
        if idx == 0:
            max_score = r[TOTAL_SCORE_INDEX]
        elif max_score < r[TOTAL_SCORE_INDEX]:
            max_score = r[TOTAL_SCORE_INDEX]
            max_score_idx = idx
        else:
            pass
  print(data[max_score_idx][0], data[max_score_idx][1])
def find_lowest_score(data, score_idx):
    in_score_idx = score_idx + SCORE_BEGIN_INDEX - 1
    min_score_idx = 0
    for idx, r in enumerate(data):
        if idx == 0:
            min_score = r[in_score_idx]
        elif min_score > r[in_score_idx]:
            min_score = r[in_score_idx]
            min_score_idx = idx
        else:
            pass
    print(data[min_score_idx][0], data[min_score_idx][1])
data = read_input(NUM_RECORDS)
add_total_score(data)
print_all(data)
find_highest_score(data)
find_lowest_score(data, 1)
find_lowest_score(data, 2)
find_lowest_score(data, 3)
find_lowest_score(data, 4)
