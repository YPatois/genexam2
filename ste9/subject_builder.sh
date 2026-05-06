#!/bin/bash
POOL="pool"
physproblems=("physique/energie/luge_ete.pdf" "physique/mouvement/drone.pdf")
chemproblems=("chimie/acide/acide_amine.pdf" "chimie/cinetique/methylpropane.pdf")

# Counter for subject numbering
subject_num=1

nbpage=( 1 6 3 4)

# Loop through each physics problem
for phys in "${physproblems[@]}"; do
    # Loop through each chemistry problem
    for chem in "${chemproblems[@]}"; do
        # Extract filenames without paths
        phys_filename="pool/$phys"
        chem_filename="pool/$chem"

        # Define output filen${POOL}/ame
        output_file="sujet_${subject_num}.pdf"

        # Merge the PDFs and number pages using pdftk
        # Note: pdftk must be installed (e.g., `sudo apt install pdftk-java` on Ubuntu)
        pdftk A="$phys_filename" B="$chem_filename" cat A B output "$output_file"

        # Add page numbers using ghostscript
        # FIXME

        # Increment subject number
        ((subject_num++))
    done
done

echo "Generated $((subject_num - 1)) subjects in the '$POOL' directory."



