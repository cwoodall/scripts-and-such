#!/usr/bin/python
##
# Name: Chord Generators (chord_generators.py)
# Purpose: 
# Date: January 5, 2011
#
# Use: python vote_counter.py [options]
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: Apache License 2.0
##

note_relation = { 
	'A': 1, 'A#': 2, 'Bb': 2, 'B': 3, 'Cb': 3, 'B#': 4, 'C': 4 , 'C#': 5, 
	'Db': 5, 'D': 6, 'D#': 7, 'Eb': 7, 'E': 8, 'Fb': 8, 'F': 9, 'F#': 10,
	'Gb': 10, 'G': 11, 'G#': 12, 'Ab': 12 
	}	
	
def generateChord(base_note, mode='major', notes=3):
	base = note_relation[base_note]
	chord = [base]
	if mode == 'major':
		i = 0
		for num in range(1, notes):
			next_note = base + 4*num - i
			if next_note > 12:
				next_note -= 12
			chord.append(next_note)
			i += 1
			
	for note in chord:
		for k, v in note_relation.iteritems():
			if base_note[1]:
				if v == note and k[1] == '#':
					print k 
				if v == note and k[1] == 'b':
					print k
			else:
				if v == note:
					print k
		
def main():
	chord_name = raw_input("Chord name: ")
	chord = generateChord(chord_name)
	print chord
	
if __name__ == '__main__':
	main()