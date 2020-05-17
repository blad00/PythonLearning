import os
import glob

with open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\Plaza4BrassicaComparison3Exp.tsv", "w") as outfile:

	path = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\\"

	annotsCounts = {}
	countFiles = 0

	fileCounter = len(glob.glob1(path, "*.txt"))
	#print(fileCounter)

	with os.scandir(path) as it:
		for entry in it:
			if entry.name.endswith(".txt") and entry.is_file():
				print(entry.name, entry.path)
				fileCu = open(entry.path)
				for line in fileCu:
					if line.startswith("("):
						continue
					fields = line.split(" ")
					gene = fields[0]
					#annot = fields[2]
					if gene in annotsCounts:
						annotsCounts[gene][countFiles] += 1
					else:
						annotsCounts[gene] = [0]*fileCounter
						annotsCounts[gene][countFiles] = 1
				countFiles+=1
				fileCu.close()



	genes = list(annotsCounts.keys())
	genes.sort()

	for gene in genes:
		outfile.write(gene)
		for cont in annotsCounts[gene]:
			outfile.write("\t"+str(cont))
		outfile.write("\n")



# numbers = [1, 2, 3, 4, 5]
# for index in range(len(numbers)):
# 	numbers[index] = numbers[index] ** 2
# print(numbers)