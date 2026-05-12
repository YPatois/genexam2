#!/bin/bash

POOL="pool"
physproblems=("physique/energie/luge_ete.pdf" "physique/mouvement/drone.pdf")
chemproblems=("chimie/acide/acide_amine.pdf" "chimie/cinetique/methylpropane.pdf")

# Counter for subject numbering
subject_num=1

# Number of pages for each subject (order: phys1+chem1, phys1+chem2, phys2+chem1, phys2+chem2)
nbpage=(6 7 4 5)

# Loop through each physics problem
for phys in "${physproblems[@]}"; do
    # Loop through each chemistry problem
    for chem in "${chemproblems[@]}"; do
        # Extract filenames without paths
        phys_filename="$POOL/$phys"
        chem_filename="$POOL/$chem"

        # Define output filename
        output_file="sujet_${subject_num}.pdf"

        # Merge the PDFs using pdftk
        pdftk A="$phys_filename" B="$chem_filename" cat A B output "$output_file"

        # Generate LaTeX file for the overlay
        overlay_tex="sujet_${subject_num}_overlay.tex"
        cat > "$overlay_tex" <<EOF
\documentclass[a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{lastpage}
\usepackage{fancyhdr}
\usepackage{geometry}
\usepackage{forloop}

% Set page margins to 0 to cover the entire page
\geometry{top=2cm, bottom=2cm}

% Custom header and footer
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Header: "Sujet numéro: <n>"
\fancyhead[C]{\fontsize{12}{14}\selectfont Sujet numéro: $subject_num}

% Footer: "Page <i>/<n>"
%\fancyfoot[C]{\fontsize{12}{14}\selectfont Page \thepage/\pageref{LastPage}}
\fancyfoot[C]{\fontsize{12}{14}\selectfont Page \thepage}

\begin{document}
% Create empty pages to match the total number of pages in the merged PDF
\newcounter{x}
\forloop{x}{1}{\value{x} < $((nbpage[$subject_num - 1]))}{
    \clearpage
    .
}
.
\clearpage
\end{document}
EOF

        # Compile the LaTeX file to generate the overlay PDF
        pdflatex "$overlay_tex"
        overlay_pdf="${overlay_tex%.tex}.pdf"
        #exit 0
        # Overlay the LaTeX-generated PDF onto the merged PDF using pdfjam
        pdftk "$overlay_pdf" multistamp "$output_file" output "${output_file%.pdf}_numbered.pdf"
        # Clean up temporary files
        #rm -f "$overlay_tex" "$overlay_pdf" "${overlay_pdf%.pdf}.aux" "${overlay_pdf%.pdf}.log"

        # Increment subject number
        ((subject_num++))
    done
done

echo "Generated $((subject_num - 1)) subjects in the '$POOL' directory."
