with open("D:\DanielVIB\Maize\\00LastIteration\\v2\corrected_counts.tsv", "r") as fileAllGenes,\
        open("D:\DanielVIB\maizeEnrich\superAnnotV3\zea_mays.b73.version3.all_transcripts.all_features.gff3", "r") as fileAnnot,\
            open("D:\DanielVIB\Maize\SNPwork\Tree\SinglePlantGeneLengths.tsv", "w") as outfile:

    # skip head
    next(fileAllGenes)

    allGenes = []

    #print header
    outfile.write("GeneName" + "\t" + "GeneLength"+"\n")

    #load all genes names
    for line in fileAllGenes:
        fields = line.split("\t")
        gene = fields[0]
        allGenes.append(gene)

    #iterate the annotation to get the genes I need and calculate their length
    for line in fileAnnot:
        fields = line.split("\t")
        if fields[2] == "gene":
            geneName = fields[8].split(";")[1].split("=")[1]
            if geneName in allGenes:
                posFin = int(fields[4])
                posIni = int(fields[3])
                geneLength = posFin-posIni
                outfile.write(geneName+"\t"+str(geneLength)+"\n")




