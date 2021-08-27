#Program to find the best ATH ortholog and relevant info from a list of Bnapus Genes

with open("D:\DanielVIB\Brassica\Annotation2020TRAPID\AnnotStevenFolder\SupplMaterial_Brassica_Arabidopsis_orthologs.tsv", "r") as orthoTable,\
        open("D:\DanielVIB\Brassica\\4Steven\inputGeneList.tsv", "r") as inputFile,\
            open("D:\DanielVIB\Brassica\\4Steven\outputOrthoGeneList.tsv", "w") as outfile:


	#load all ortho in a dict
	# skip header
	next(orthoTable)

	map_ortho = {}
	bra_gene = ""

	for line in orthoTable:
		fields = line.split("\t")
		if bra_gene != fields[0]:
			bra_gene = fields[0]
			map_ortho[bra_gene] = fields[3]+"\t"+fields[6]+"\t"+fields[7]

	#iterate over the input list to get the translation
	# skip header
	next(inputFile)
	for line in inputFile:
		fields = line.split("\t")
		text = map_ortho.get(fields[0].rstrip())
		if text is not None:
			outfile.write(fields[0].rstrip()+"\t"+text)
		else:
			outfile.write(fields[0].rstrip()+"\n")

