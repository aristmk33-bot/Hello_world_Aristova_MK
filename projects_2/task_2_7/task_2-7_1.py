files = ["seq1", "seq2", "seq3", "seq4"]
sampling_date = "2026-02-18"

for name in files:
    new_name = name + ".fasta" + "_" + sampling_date
    print(new_name)