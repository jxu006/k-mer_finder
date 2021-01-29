#!/usr/bin/env python 

import sys
from operator import itemgetter
import argparse


def kmer_finder(fastq_file, k):
    """kmer-finder is used for generating a sorted k-mer sequences list from a raw FASTQ file."""
    #Open the raw FASTQ file to read
    f = open(fastq_file)
    kmer_dict = {}
    i = 0
    for row in f:
	i += 1
	if i % 4 == 2:
	    sequence = row.rstrip()
            #Count the k-mer sequences and add to the dictionary kmer_dict 
	    for j in range(len(sequence)-k+1):
	        kmer_sequence = sequence[j:(j+k)]
                if kmer_sequence not in kmer_dict:
                    kmer_dict[kmer_sequence] = 1
                else:
                    kmer_dict[kmer_sequence] += 1
    #Sort the k-mer sequences dictionary according to their frequency
    sorted_kmer_sequence = sorted(kmer_dict.items(), key=itemgetter(1), reverse=True)
    return sorted_kmer_sequence


def main():
    sorted_kmer_sequence = kmer_finder(args.fastq, args.kmer)
    o = open(args.outfile, "w")
    o.write("k-mer"+"\t"+"Number"+"\n")
    for seq in sorted_kmer_sequence:
        o.write(seq[0]+"\t"+str(seq[1])+"\n")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate a sorted k-mer sequences according to their frequency in the FASTQ data.")
    parser.add_argument('-f', dest='fastq', required=True, type=str, help='The raw fastq file')
    parser.add_argument('-k', dest='kmer', required=True, type=int, help='The length of k-mer')
    parser.add_argument('-o', dest='outfile', required=True, type=str, help='Output file')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    main()
