#!/bin/sh
cat data/doi_list.txt | python test_phylografter_doi.py
cat data/bad/doi_list.txt | python test_phylografter_doi.py 0