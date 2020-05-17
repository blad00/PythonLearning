

#file = open("/home/dacru/Midas/research/deepseq/ngsproject_brassica/Annotation2020TRAPID/Results/transcripts_go_exp1086.txt", "r")
#with open("/home/dacru/Midas/research/deepseq/ngsproject_brassica/Annotation2020TRAPID/Results/transcripts_go_exp1105Exome.txt", "r") as file,\
#		open("/home/dacru/Midas/research/deepseq/ngsproject_brassica/Annotation2020TRAPID/Results/BrassicaNapusAnnotExome.txt", "w") as outfile:
with open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\\transcripts_go_exp1285ExomePlaza4.5.txt", "r") as file,\
		open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\BrassicaNapusAnnotExomePlaza4.5.txt", "w") as outfile:
	next(file)
	outfile.write("(species=Brassica)(type=Biological Process)(curator=GO)"+"\n")

	for line in file:
		fields = line.split("\t")
		gene = fields[1]
		annot = fields[2].split(":")[1]
		outfile.write(gene + " = " + annot+"\n")
