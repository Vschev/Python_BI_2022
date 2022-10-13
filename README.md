# Python_BI_2022
Bioinf assignments

fastq_filtrator.py

DESCRIPTION
This is a utility that takes NGS reads from the input fastq file, filters them based on several parametres, and saves those that pass all checks in an output file. 
Optionally, the reads that don't meet the criteria are written into an additional file.
You can set the desired length, GC-content and the minimal mean Q-score (Phred) of the reads you wants to save.

USING THE UTILITY
Simply call the function main with the proper arguments, and it will do its work. You can specify the following arguments:

NECESSARY ARGUMENTS
input_fastq - this is the path to an input fastq. file. 
It supports both the absolute and relative paths including just the name of the file if it is in the working directory.

OPTIONAL ARGUMENTS
output_file_prefix - the output file's name prefix. Reads that pass the filtering are saved in the "{output_file_prefix}_passed.fastq"
If you are also saving the failed reads (see save_filtered) those go into the "{output_file_prefix}_failed.fastq"

gc_bounds=(0, 100) - this tuple of two elements indicates the lower and upper bounds for the accessible GC-content % in your reads.
Alternatively, you can assign a single integer or a doublegc_bounds=(0, 100), length_bounds=(0, 2 ** 32),
         quality_threshold=0, save_filtered=False
in
