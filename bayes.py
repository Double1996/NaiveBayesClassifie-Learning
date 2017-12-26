import csv
import random
import math


def load_csv_file(filename):
    with open(filename) as f:
        lines = csv.reader(f)
        data_set = list(lines)
    for i in range(len(data_set)):
        data_set = [float(x) for x in data_set[i]]
    return data_set


def split_data_set(data_set, split_ratio):
    train_size = int(len(data_set) * split_ratio)
    train_set = []
    data_set_copy = list(data_set)
    while len(train_set) < train_size:
        index = random.randrange(len(data_set_copy))
        train_set.append(data_set_copy.pop(index))
    return [train_set, data_set_copy]


def separte_by_class(data_set, class_index):
    result = {}
    for i in range(len(data_set)):
        vertor = data_set[i]
        class_val = vertor[class_index]
        if (class_val not in result):
            result[class_val] = []
        result[class_val].append(vertor)
    return result


def mean(numbers):
    return sum(numbers) / float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers))
    return math.sqrt(variance)


def summarize(data_set):
    summaries = [(mean())]


if __name__ == '__main__':
    load_csv_file('pima-indians-diabetes')
