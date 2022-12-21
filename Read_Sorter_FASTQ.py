class Read:
    def __init__(self, read_id,
                 read_sequence,
                 comment, quality):

        self.read_id = read_id
        self.read_sequence = read_sequence
        self.comment = comment
        self.quality = quality

    def __len__(self):
        return len(self.read_sequence)

    def gc(self):
        c = self.read_sequence.count('C')
        g = self.read_sequence.count('G')
        gc = c + g / len(self.read_sequence) * 100
        return gc


    def mean_quality(self):
        scores = []
        for char in self.quality:
            scores.append(ord(char) - 33)
        mean = sum(scores) / len(scores)
        return mean

class FASTQFile:
    def __init__(self, file = 'A:/Thaliana.fastq',
                 fastq_records = None):
        self.file = file
        self.fastq_records = fastq_records

    def sort_reads(self):
        read_stats = []
        for num in range(len(self.fastq_records)):
            read_stats.append((self.fastq_records[num].mean_quality()*(-1),
                               len(self.fastq_records[num])*(-1),
                               self.fastq_records[num].gc(),
                               self.fastq_records[num].read_id,
                               num))
        read_stats.sort()
        sorted_reads = []
        for stats in read_stats:
            sorted_reads.append(self.fastq_records[stats[4]])
        self.fastq_records = sorted_reads.copy()
        sorted_reads = []
        for i in self.fastq_records:
            print(i.mean_quality())

    def write_to_file(self, fastq_file_name):
        with open(fastq_file_name, "w") as file:
            for read in self.fastq_records:
                file.write(f'@{read.read_id}\n')
                file.write(f'{read.read_sequence}\n')
                file.write(f'{read.comment}\n')
                file.write(f'{read.quality}\n')
            

def read_fastq(fastq_file_name):
    fastqreads = FASTQFile(fastq_file_name)

    with open(fastq_file_name) as file:
        p = 0
        while True:
            obj = list(file.readline())
            if obj == []:
                break
            FASTQreads.fastq_records.append(Read())
            FASTQreads.fastq_records[-1].read_id = ''.join(obj[1:-1])
            obj = list(file.readline())
            FASTQreads.fastq_records[-1].read_sequence = ''.join(obj[0:-1])
            obj = list(file.readline())
            FASTQreads.fastq_records[-1].comment = ''.join(obj[0:-1])
            obj = list(file.readline())
            FASTQreads.fastq_records[-1].quality = ''.join(obj[0:-1])
            p += 1
    return FASTQreads
            
            
