## Discrete configurations spaces of sliding with hexagonal tiles

DEVELOPERS:

Ray Karpman (karpman1@otterbein.edu)  
Erika Roldan (erika.roldan@ma.tum.de)

DATE: January 3, 2022

LICENSE: GNU GENERAL PUBLIC LICENSE (see license.txt)

## Overview

Sliding puzzles are sequential mechanical puzzles which are solved by sliding certain pieces on a fixed board from a starting configuration to a target final configuration. The most famous is the 15 Puzzle, which consists of 15 tiles (and one hole) on a 4-by-4 square board. The code in this repository can be used to investigate the behavior of sliding puzzles on a subset of the tesselation of the plane by hexagons. For a board with squares tiles, is always possible to slide a square tile into a hole that shares an edge with the tile. For a board with hexagonal tiles, a tile can only slide into a neighboring empty hexagonal hole if  there are two adjacent empty hexagons that are at the same time sharing an edge with the tile to move

The *puzzle graph* of a sliding puzzle is a graph whose vertices are configurations of the board. Two configurations are adjacent if one can be obtained from the other by sliding a tile into a hole. We are interested in characterizing the connected components of the puzzle graphs of puzzles with hexagonal tiles, which in turn allow us to determine whether a puzzle is solvable. We define functions which take a representation of a hexagonal board and a starting configuration as input, and produce an output file containing a list of all configurations in the same connected component of the puzzle graph as the starting configuration.

## Acknowledgements

Erika Roldan received funding from the European Union’s Horizon 2020 
research and innovation program under the Marie Skłodowska-Curie grant agreement No. 754462.

## Citations

You are welcome to use and adapt this code for your own projects. If you use this code, 
please cite the paper PARITY PROPERTY OF HEXAGONAL SLIDING PUZZLES. 

```
@article{slidehex2022,
title={Parity property of hexagonal sliding puzzles},
author={Karpman, Ray and Roldan, Erika},
journal={arXiv preprint},
year={2022}
}
```

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
of all configurations in a sample component of a puzzle graph, once a board and vertex are provided.
We have attempted to make their use relatively self-explanatory by commenting the code.

In the paper, we primarily computed connected components using the function.

`write_component_idx(holes, board, board_name, file_name)`.

The parameter board be defined, as explained above. The parameter `board_name` is
a string giving a verbal description of the board, to make the output file 
easier to understand. The parameter `file_name` is the name of the output file, which should include
the extension `.txt.`

This function uses a breadth-first search algorithm to find all configurations of the given board
in the connected component containing a sample configuration with the 
desired number of holes. The final output file lists the configurations, one per line. The function also computes a 
dictionary encoding the relations in the resulting search tree. Key-value pairs from this dictionary
are also recorded in the output file. Keys are positions in the 
list of all configurations, and values are lists of configurations neighboring the key. 
While this is not needed for our results in the paper, we feel it could yield useful insights
into the combinatorics of the puzzle graphs.
