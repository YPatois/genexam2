# Définir le terminal pour un fichier PNG
set terminal png size 1200,500
set output 'graphique_reaction.png'

# Définition des fonctions avec la variable x
C(x) = 0.30 * exp(-0.035 * x)
Cprime(x) = -0.0105 * exp(-0.035 * x) * 10
Cseconde(x) = 3.675e-4 * exp(-0.035 * x) * 100

# Configuration du graphique
set xrange [0:50]
set yrange [-0.15:0.35]
set xlabel "Temps (min)"
set ylabel "Valeur"
set grid
set key top left

# Tracé des fonctions
plot C(x) title "C(t)" with lines linewidth 2 linecolor rgb "blue", \
     Cprime(x) title "C'(t) x 10" with lines linewidth 2 linecolor rgb "red", \
     Cseconde(x) title "C''(t) x 100" with lines linewidth 2 linecolor rgb "green"

