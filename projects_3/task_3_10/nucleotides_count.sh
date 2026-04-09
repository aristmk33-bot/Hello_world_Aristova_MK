#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    if [ ! -s "$file" ]; then
        continue
    fi
    
    A=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "A" | wc -l)
    T=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "T" | wc -l)
    G=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "G" | wc -l)
    C=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "C" | wc -l)
    
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A" "$T" "$G" "$C"
done
