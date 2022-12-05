# Advent of Code day one 
# https://adventofcode.com/2022/day/1


with open('vztup.txt') as f:  #komentarrr
	lines = f.read()

elfs_raw = lines.split("\n\n")   #split podle radku

elfs = list()

for elf in elfs_raw:
	elfs.append(elf.split("\n"))

elfs_sums = list()

for elf in elfs:
	sum = 0
	for entry in elf:
		sum += int(entry)
	elfs_sums.append(sum)

print(max(elfs_sums))
		