# read first gene
print("Imput gene to check")
gene = input()

while gene != 'x':

    #declare output file
    output = "D:\DanielVIB\Brassica\ModelsValitationTrial1\\"+gene+".tsv"
    outputFile = open(output, 'w')

    print("get annotations")
    #get annotations
    annots = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\\transcripts_go_exp1285ExomePlaza4.5.txt"
    annotsFile = open(annots, "r")
    outputFile.write("Annotations"+"\n")

    for line in annotsFile:
        fields = line.split("\t")
        if fields[1] == gene:
            outputFile.write(fields[1]+'\t'+fields[2]+"\t"+fields[5])

    outputFile.write("\n")
    annotsFile.close()

    print("get syntenic orthologs")
    #get syntenic orthologs
    orthoSun = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\Syntenic\AthOrthoFromSynteniListSun.tsv"
    orthoSunFile = open(orthoSun, "r")
    outputFile.write("Syntenic Ortho Sun"+"\n")

    for line in orthoSunFile:
        fields = line.split("\t")
        if fields[0] == gene:
            outputFile.write(line+"\n")

    outputFile.write("\n")
    orthoSunFile.close()


    orthoChal = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\Syntenic\AthOrthoFromSynteniListChalhoub.tsv"
    orthoChalFile = open(orthoChal, "r")
    outputFile.write("Syntenic Ortho Chal"+"\n")

    for line in orthoChalFile:
        fields = line.split("\t")
        if fields[0] == gene:
            outputFile.write(line+"\n")

    outputFile.write("\n")
    orthoChalFile.close()

    print("get Diamond orthologs")
    #get Diamond orthologs
    orthoDia = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\BraNapus_ArabiOrthologFull.tsv"
    orthoDiaFile = open(orthoDia, "r")
    outputFile.write("Syntenic Ortho Diamond"+"\n")

    for line in orthoDiaFile:
        fields = line.split("\t")
        if fields[0] == gene:
            outputFile.write(line+"\n")

    orthoDiaFile.close()

    #close gene file
    outputFile.close()

    print("Imput gene to check")
    gene = input()