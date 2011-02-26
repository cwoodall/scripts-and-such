# Scripts and Such

A collection of scripts which don't necessitate individual repositories. Basically
just stuff I want to save online and allow people to look at.

## Vote Counter (vote_counter.py)

**Language:** Python  
**Folder:** python-dump  
**Purpose:** To calculate a sorted list of album rankings for 130BPM's year-end
rankings (and any other ranking).  
**Status:** Done    
**Version:** 1.0  

### Use of vote_counter.py

	Usage: vote_counter.py [options]  
  
	Options:  
 		-h, --help            show this help message and exit  
		-f FILE, --file=FILE  The location of the csv file  
  		-o OUTPUT, --output=OUTPUT  
                        	  The location of the output file  
  		-q, --quiet           Dont't print the results to stdout  

## MATLAB Dictionary (dictionary.m)

**Language:** MATLAB  
**Folder:** matlab-dump  
**Purpose:** A basic hash-table/dictionary system for MATLAB which leverages 
MATLAB's Cell Array's defining a dictionary as a subset of a Cell Array.  
**TODO:** Test code for speed and ability to handle various loads. Also, define a 
class for it and port the code to MATLAB C++ to make it faster (if necissary).  
**Status:** Proof of Concept  
**Version:** Proof of Concept  

### Usage

For usage look at the dictionary_example.m file

## Chord Generator

**Language:** Python  
**Folder:** python-dump   
**Purpose:** To generate chords based on chord notation...  
**Status:** Currently handles major chords OK, but not well. Needs alot of work.  
**Version:** -  

### Usage

None as of now.

## Ones In A Bit (ones-in-a-byte/byte_count.py)

**Language:** Python  
**Folder:** python-dump   
**Purpose:** To count the number of 1s in a byte.  
**Status:** Done and works, need to insert an if __name__ == '__main__' statement  
**Version:** 1  


