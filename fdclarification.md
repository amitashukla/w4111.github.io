---
layout: page
---

# Clarification about Functional Dependency Decomposition

This document clarifies decomposition for functional dependencies.  What I demonstrated in class was misleading.

## BCNF

In BCNF, you take the FDs as-is, and perform decomposition.  The order of functional dependencies that you use to perform decomposition will affect the tables that you end up with.

        for each fd of the form X->Y in FDs
          for each R in DecomposedRelations
            if fd is in R's projection
              if fd violates BCNF with respect to R
                decompose R using fd 
                updated DecomposedRelation by replacing R with its decomposition


The key is how `violates` is checked.  You start with the **fds in R's projection**, and then check

1. is fd trivial?  otherwise
2. does `X` determine R when using the fds in R's projection?


What this means is that your decomposition may have been lossy and thus lose potential keys!  Take the example from the lecture notes:

        R:   ABCDE
        FDS: A->BCDE, BC->A, D->B, C->D

        # suppose we first check D->B:

        D doesn't determine R, thus we decompose into: BD, ACDE

        Let's check BD:
        
          Only D->B is in its projection, thus its in BCNF.  
          
        Let's check ACDE:
        
          Only C->D is in its projection, so ACDE is redundant.
          Decompose into: CD, ACE

        ACDE has empty projection, thus it's in BCNF


## 3NF

In 3NF, you first compute the minimal cover of the FDs.  Note that the minimal cover may not always be unique.  Once you have the minimal cover, the procuder is similar to BCNF, with two key differences

1. checking violation of 3NF also allows Y to be part of a key (minimal key).
2. once you have performed BCNF decomposition, any lost dependencies are added as new relations.
