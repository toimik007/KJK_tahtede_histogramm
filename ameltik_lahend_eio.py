import sys

# seda arvu tegelikult ei kasuta
num_lines = int(sys.stdin.readline())

# loeme sisendi ridahaaval ja teeme jooksvalt statistika
hist = {}
for line in sys.stdin.readlines():
	for char in line:
		if char not in hist:
			hist[char] = 0
		hist[char] += 1

# väljastame statistika, jättes vahele tühikud ja reavahetused
for char in hist:
	if not char.isspace(): # filtreerime tühikud ja reavahetused välja
		sys.stdout.write('{} {}\n'.format(char, hist[char]))
