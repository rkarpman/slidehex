## Discrete configurations spaces of sliding with hexagonal tiles

DEVELOPERS:

Ray Karpman (karpman1@otterbein.edu)  
Erika Roldan (erika.roldan@ma.tum.de)

DATE: January 3, 2022

LICENSE: GNU GENERAL PUBLIC LICENSE (see license.txt)

## Overview

## Acknowledgements

Erika Roldan rreceived funding from the European Union’s Horizon 2020 
research and innovation program under the Marie Skłodowska-Curie grant agreement No. 754462.

## Citations

You are welcome to use and adapt this code for your own projects. If you use this code, 
please cite the paper PARITY PROPERTY OF HEXAGONAL SLIDING PUZZLES. 

`@article{slidehex2022,
  title={Parity property of hexagonal sliding puzzles},
  author={Karpman, Ray and Roldan, Erika},
  journal={arXiv preprint},
  year={2022}
}`

## Dependencies

Python 3.8.

## Usage 

To use the program, download and run the script `slidehex_by_comp.py`. 

Tuples representing boards of various shapes explored in the paper
are saved as global variables in the script. You may also define your own boards.
A board is represented as a tuple of ordered pairs, 
which give the centers of hexagonal tiles on a board.

Configurations are represented as tuples of integers, where 0 represents a hole
and positive integers represent tile labels. The `ith` entry of a tuple representing
a configuration gives the contents of the tile in position `i` of the corresponding board,
which is assumed to have been provided as a tuple. 

A number of related functions are provided, which can be used to compute a list
off all configurations in a sample component of a puzzle graph, once a board and vertex are provided.
We have attempted to make their use relatively self-explanatory, with comments on the code.

In the paper, we primarily used the function 

`write_component_idx(holes, board, board_name, file_name)`.

Your board must be pre-defined, as explained above. The parameters `board_name` is
a string giving a verbal description of the board, to make the output file more 
self-contained. The parameter `file_name` is the name of the output file, which should include
the extension `.txt.`

This function uses a breadth-first search algorithm, and the final output file 
contains a list of all configurations in a sample csomponent of the puzzle graph
with the given number of holes, and given board. The function also computes a 
dictionary encoding the relations in the resulting search tree. Keys are positions in the 
list of all configurations, and values are lists of configurations neighboring the key. 
