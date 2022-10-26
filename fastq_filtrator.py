def main(input_fastq, output_file_prefix='',
         gc_bounds=(0, 100), length_bounds=(0, 2 ** 32),
         quality_threshold=0, save_filtered=False):
    file = open(input_fastq)
    while True:
        read = scan(file)

        # indicates the end of the file

        if read[0] == '':
            break

        if length_bounds != (0, 2 ** 32):
            if not isinstance(length_bounds, tuple):
                base_length(read, read[1], length_bounds)
            else:
                base_length(read, read[1], length_bounds[1])
                full_length(read, read[1], length_bounds[0])

        if len(read) != 4 and save_filtered:
            output(output_file_prefix, read[0:4], good=0)
            continue

        if gc_bounds != (0, 100):
            if not isinstance(gc_bounds, tuple):
                base_gc(read, read[1], gc_bounds)
            else:
                full_gc(read, read[1], gc_bounds[0], gc_bounds[1])

        if len(read) != 4 and save_filtered:
            output(output_file_prefix, read[0:4], good=0)
            continue

        if quality_threshold != 0:
            filter_quality(read, read[3], quality_threshold)

        if len(read) != 4 and save_filtered:
            output(output_file_prefix, read[0:4], good=0)
            continue

        output(output_file_prefix, read[0:4], good=1)
    file.close()


# generates reads from fastq file

def scan(data):
    current_read = []
    for string in range(4):
        current_read.append(data.readline())
    return current_read


# filters reads by their length

def base_length(read, sequence, upper_bound):
    if len(sequence) > upper_bound:
        read.append("X_X")


def full_length(read, sequence, lower_bound):
    if len(sequence) < lower_bound:
        read.append("X_X")


# filters reads by their GC% content

def base_gc(read, sequence, upper_bound):
    base_count = {"A": 0, "G": 0, "C": 0, "T": 0, "N": 0}
    for nucl in sequence:
        if nucl in base_count:
            base_count[nucl] += 1
        else:
            base_count[nucl] = 0
    total = (base_count["G"] + base_count["C"])
    gc = total / sum(base_count.values()) * 100
    if gc > upper_bound:
        read.append("X_X")
    return gc


def full_gc(read, sequence, lower_bound, upper_bound):
    gc = base_gc(read, sequence, upper_bound)
    if gc > upper_bound:
        read.append("X_X")
    if gc < lower_bound:
        read.append("X_X")


# filters reads by their quality

def filter_quality(read, sequence, threshold):
    scores = []
    for char in sequence:
        scores.append(ord(char) - 33)
    mean = sum(scores) / len(scores)
    if mean < threshold:
        read.append("X_X")


# opens output and adds a read to the end

def output(path, read, good=1):
    if good == 1:
        file1 = open(f"{path}_passed.fastq", "a")
    else:
        file1 = open(f"{path}_failed.fastq", "a")
    for line in read[0:4]:
        file1.write(line)
    file1.close()
