

with open("/home/dacru/Midas/research/deepseq/ngsproject_brassica/Annotation2020TRAPID/Results/BrassicaNapusAnnotExome.txt", "r") as file1,\
		open("/home/dacru/Midas/research/deepseq/ngsproject_brassica/Annotation2020TRAPID/Results/Plaza4BrassicaExome.tsv", "w") as outfile:
	next(file1)

	annotsCounts = {}

	for line in file1:
		fields = line.split(" ")
		gene = fields[0]
		#annot = fields[2]
		if gene in annotsCounts:
			annotsCounts[gene] += 1
		else:
			annotsCounts[gene] = 1

	genes = list(annotsCounts.keys())
	genes.sort()

	for gene in genes:
		#outfile.write(gene+"\t"+str(annotsCounts[gene])+"\n")
		outfile.write("{}\t{}\n".format(gene,annotsCounts[gene]))




