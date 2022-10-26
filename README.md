# Python_BI_2022
Bioinf assignments

## fastq_filtrator.py

### DESCRIPTION

This is a utility that takes NGS reads from the input fastq file, filters them by several parametres, and saves those that pass all checks in an output file. 
Optionally, the reads that don't meet the criteria are written into an additional file.
Input file is not changed.
You can set the desired length, GC-content and the minimal mean Q-score (Phred) of the reads you wants to save.

### USING THE UTILITY

Simply call the function main with the proper arguments, and it will do its work. You can specify the following arguments:

#### NECESSARY ARGUMENTS

input_fastq - this is the path to an input fastq.file. 
It might be the absolute path or one from the working directory.

#### OPTIONAL ARGUMENTS

output_file_prefix - the output file's name prefix. Reads that pass the filtering are saved in the "{output_file_prefix}_passed.fastq"
If you are also saving the failed reads (see save_filtered) those go into the "{output_file_prefix}\_failed.fastq"
**WARNING**: output files are opened in the "append" mode. 
Please use unique values of this argument for every run if you don't want reads from different inputs saved in a single file.

gc_bounds=(0, 100) - use this argument if you want to remove reads that do not have the desired GC percentage. 
This tuple of two elements indicates the lower and upper bounds for the accessible GC-content % in your reads.
Alternatively, you can assign a single integer or a double number here, it will be considered an upper bound.

length_bounds=(0, 2 ** 32) - this argument allows to select the reads whose length lies in the given interval.
You can also assign a number here instead of a tuple, in this case, only reads of lower length will remain. 

quality_threshold=0, - sets the threshold for the mean q-value of a read using the Phred33 scale. If the read doesn't surpass the threshold, it is removed.
See the documentation for the fastq quality scale here: https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm

save_filtered=False - reads that filtered out are not saved by default. If you want them to be saved, set the value True.
  
### FUNCTIONS INSIDE THE MODULE

main(input_fastq, output_file_prefix='', gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0, save_filtered=False) - the main function :)


The other functions are used inside the main and receive their arguments from it:


scan(data) - the function used for file loading reads from file into the memory.

base_length(read, sequence, upper_bound) - checks if the sequence in a read is shorter than the max allowed length.

full_length(read, sequence, lower_bound) - checks if the sequence in a read is also longer than the min allowed length, if needed.

base_gc(read, sequence, lower_bound) - counts the GC content (%) of a sequence in a read and checks if it is shorter than the max allowed number.

full_gc(read, sequence, lower_bound) - uses the base_GC calculations and additionally checks if the GC content higher than the min allowed number.

filter_quality(read, sequence, threshold) - calculates the mean q-score of a read and filters reads in which it is lower than a threshold.

output(path, read, good=1) - the function that fills in the output file(s) with reads.
