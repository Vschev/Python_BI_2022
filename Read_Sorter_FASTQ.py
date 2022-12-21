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
        self.fastq_records = sorted(self.fastq_records, key = lambda x:
                                    (x.mean_quality()*(-1), len(x)*(-1),
                                     x.gc(), x.read_id))

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
        fastqreads.fastq_records = []
        while True:
            obj = file.read(1)
            if obj != "@":
                break
            r = Read(file.readline().strip(),
                     file.readline().strip(),
                     file.readline().strip(),
                     file.readline().strip())
            fastqreads.fastq_records.append(r)
    return fastqreads
            
            
