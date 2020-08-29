# Author: Guilherme Contesini
# e-mail: gcontesini@gmail.c
# date: 05/05/2012
# course: Computational Physics I

# Problem 1 - Conway game of life

# 

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import numpy as np

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def main():

  lattice_size_int = 100
  total_time_int = 100
  density_float = 0.3

  grid_ary = create_grid( lattice_size_int, density_float )
  # grid_ary = np.random.randint(0,2,[lattice_size_int,lattice_size_int])

  file_obj = open("life.dat","w")

  for t_int in np.arange(total_time_int):

    for i_int in np.arange( lattice_size_int ):

      for j_int in np.arange( lattice_size_int ):

        file_obj.write( str( grid_ary[i_int][j_int] ) + "  " )

        if( j_int == lattice_size_int-1 ):
          
          file_obj.write("\n")

    file_obj.write("\n")

    grid_ary = celular( grid_ary, lattice_size_int )

  file_obj.close()
  print("EOS")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def create_grid( lattice_size_int_, density_float_ ):

  aux_grid_ary = np.zeros([lattice_size_int_, lattice_size_int_],dtype=int)

  for i_int in np.arange( lattice_size_int_ ):

    for j_int in np.arange( lattice_size_int_ ):

      if( np.random.random() < density_float_ ):

        aux_grid_ary[i_int][j_int] = 1

  return  aux_grid_ary

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def celular( grid_ary_, lattice_size_int_ ):

  aux_grid_ary = np.zeros( [lattice_size_int_,lattice_size_int_], dtype=int )

  for x_int in np.arange( lattice_size_int_ ):

    for y_int in np.arange( lattice_size_int_ ):

      index_tpl_ = ( x_int, y_int )

      number_neighbor_int = count_neighbors( grid_ary_, lattice_size_int_, index_tpl_)
      
      # print(number_neighbor_int)

      if( grid_ary_[x_int][y_int] == 1 ):

        # Underpopulation
        if( number_neighbor_int < 2 ):

          aux_grid_ary[x_int][y_int] = 0

        # Aging
        if( number_neighbor_int == 2 or number_neighbor_int == 3 ): 
        # if( number_neighbor_int == 3 ): 

          aux_grid_ary[x_int][y_int] = 1

        # Overpopulation
        if(  number_neighbor_int > 3):

          aux_grid_ary[x_int][y_int] = 0

      else:

        # Reproduction
        if( number_neighbor_int == 3 ): 

          aux_grid_ary[x_int][y_int] = 1

    comparison = aux_grid_ary == grid_ary_      

    if( comparison.all() ):

      exit(0)

  return aux_grid_ary

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def count_neighbors( grid_ary_, lattice_size_int_, site_index_tpl_ ):

  sum_int = 0

  # 1-d Neumann_neighbor for Ising
  #   line = (L+i-+1)%L + (i/L)*L         left/right
  #   column = ((L+i-+i)%L)*L + (i%L)     down/up

  # Funny that if you use only von Neumann neighbor in a high density 
  #   lattice (>0.5) the system behaves like the evolution of a river.

  # left_index_int  = ((lattice_size_int_+site_index_int_-1)%lattice_size_int_) + ((site_index_int_//lattice_size_int_)*lattice_size_int_)
  # right_index_int = ((lattice_size_int_+site_index_int_+1)%lattice_size_int_) + ((site_index_int_//lattice_size_int_)*lattice_size_int_)
  # down_index_int = ((lattice_size_int_+site_index_int_-1)%lattice_size_int_)*lattice_size_int_ + (site_index_int_%lattice_size_int_)
  # up_index_int = ((lattice_size_int_+site_index_int_+1)%lattice_size_int_)*lattice_size_int_ + (site_index_int_%lattice_size_int_)

  # sum_int += grid_ary_[left_index_int] + grid_ary_[right_index_int] + grid_ary_[down_index_int] + grid_ary_[up_index_int]

  x_int = site_index_tpl_[0]
  y_int = site_index_tpl_[1]

  # 2-d Moore neighbor for Ising
  # line (x_int+-1)%lattice_size_int_  , y_int
  # colunm (x_int) , (y_int+-)%lattice_size_int_

  # straight down
  if( grid_ary_[x_int][(y_int-1)%lattice_size_int_] == 1 ):

    sum_int += 1

  # straight up
  if( grid_ary_[x_int][(y_int+1)%lattice_size_int_] == 1 ):

    sum_int += 1

  # straight left
  if( grid_ary_[(x_int-1)%lattice_size_int_][y_int] == 1 ):

    sum_int += 1

  # straight right
  if( grid_ary_[(x_int+1)%lattice_size_int_][y_int] == 1 ):  

    sum_int += 1

  # left up
  if( grid_ary_[(x_int-1)%lattice_size_int_][(y_int-1)%lattice_size_int_] == 1 ):

    sum_int += 1

  # left down
  if( grid_ary_[(x_int-1)%lattice_size_int_][(y_int+1)%lattice_size_int_] == 1 ):

    sum_int += 1

  # right up
  if( grid_ary_[(x_int+1)%lattice_size_int_][(y_int-1)%lattice_size_int_] == 1 ):

    sum_int += 1

  # straight down
  if( grid_ary_[(x_int+1)%lattice_size_int_][(y_int+1)%lattice_size_int_] == 1 ):  

    sum_int += 1

  return sum_int

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

if __name__ == '__main__':
  main()