reset

set termina gif animate delay 0.15
set output "life.gif"

life_data = "life.dat"
lat_size_int = 100
time_int = 100

unset tics
unset key

set xrange[-1:lat_size_int]
set yrange[-1:lat_size_int]

set palette defined ( 0 "#FFFFFF", 1 "#000000")
set colorbox horizontal                         
set size 0.99,0.95; set origin 0.01,0.05
set colorbox user origin 0.05,0.05 size 0.90,0.02

do for [i=0:time_int]{

  plot life_data matrix index i with image notitle

}

reset 