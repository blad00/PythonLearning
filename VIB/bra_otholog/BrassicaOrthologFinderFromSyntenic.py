#class to store data for each BraNu gene

class BraEspc:

    def __init__(self, name):
        self.branuName = name    # instance variable unique to each instance
        self.listRapa = []
        self.listOle = []
        self.listAthOtho = []

    def add_rapa(self, rapaGene):
        self.listRapa.append(rapaGene)

    def add_ole(self, oleGene):
        self.listOle.append(oleGene)

    def add_ortho(self, orthoGene):
        self.listAthOtho.append(orthoGene)

#program it self

#Test
# simil = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\similarities_1285.dump_head.tsv"
# output = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\BraNapus_ArabiOrtholog.tsv"

simil = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\Syntenic\SynteniListChalhoub.tsv"
output = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\Syntenic\AthOrthoFromSynteniListChalhoub.tsv"

similFile = open(simil, "r")
# skip header
next(similFile)

outputFile = open(output, 'w')
#whole list of branu genes
listBranus = []

#main loop over the simil file
for line in similFile:

    fields = line.split("\t")
    geneNameBranu = fields[0]
    #create branu object
    branu = BraEspc(geneNameBranu)

    matches = fields[1].split(";")
    #second loop over the matches details
    for matchInfo in matches:
        matchDetails = matchInfo.split(",")
        matchGene = matchDetails[0]
        if matchGene.startswith("Brara") and matchGene not in branu.listRapa:
            branu.add_rapa(matchGene)
        elif matchGene.startswith("Bo") and matchGene not in branu.listOle:
            branu.add_ole(matchGene)
    #add the branu gene to the list
    listBranus.append(branu)

# for curBranu in listBranus:
#     print(curBranu.branuName)
#     print(curBranu.listOle)
#     print(curBranu.listRapa)

similFile.close()

#now load othofiles

anchor = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\integrative_orthology.anchor_point_brassicasVSarabidopsisTha.tsv"
bhif = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\integrative_orthology.BHIF_brassicasVSarabidopsisTha.tsv"
ortho = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\integrative_orthology.ORTHO_brassicasVSarabidopsisTha.tsv"
trog = "D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\integrative_orthology_files\integrative_orthology.TROG_brassicasVSarabidopsisTha.tsv"

#read ortho files and skip heads
anchorFile = open(anchor, "r")
next(anchorFile)
bhifFile = open(bhif, "r")
next(bhifFile)
orthoFile = open(ortho, "r")
next(orthoFile)
trogFile = open(trog, "r")
next(trogFile)

anchorMap = {}
bhifMap = {}
orthoMap = {}
trogMap = {}

## 1 anchor
for line in anchorFile:
    fields = line.split("\t")
    #get the brassica gene and the arabidopsis gene
    if fields[1] == "ath":
        braGene = fields[2]
        athGene = fields[0]
    else:
        braGene = fields[0]
        athGene = fields[2]

        if braGene in anchorMap:
            if athGene not in anchorMap[braGene]:
                anchorMap[braGene].append(athGene)
        else:
            anchorMap[braGene] = [athGene]

anchorFile.close()

## 2 NHIF
for line in bhifFile:
    fields = line.split("\t")
    #get the brassica gene and the arabidopsis gene
    if fields[1] == "ath":
        braGene = fields[2]
        athGene = fields[0]
    else:
        braGene = fields[0]
        athGene = fields[2]

        if braGene in bhifMap:
            if athGene not in bhifMap[braGene]:
                bhifMap[braGene].append(athGene)
        else:
            bhifMap[braGene] = [athGene]

bhifFile.close()

## 3 ORTHO
for line in orthoFile:
    fields = line.split("\t")
    #get the brassica gene and the arabidopsis gene
    if fields[1] == "ath":
        braGene = fields[2]
        athGene = fields[0]
    else:
        braGene = fields[0]
        athGene = fields[2]

        if braGene in orthoMap:
            if athGene not in orthoMap[braGene]:
                orthoMap[braGene].append(athGene)
        else:
            orthoMap[braGene] = [athGene]

orthoFile.close()

## 4 NHIF
for line in trogFile:
    fields = line.split("\t")
    #get the brassica gene and the arabidopsis gene
    if fields[1] == "ath":
        braGene = fields[2]
        athGene = fields[0]
    else:
        braGene = fields[0]
        athGene = fields[2]

        if braGene in trogMap:
            if athGene not in trogMap[braGene]:
                trogMap[braGene].append(athGene)
        else:
            trogMap[braGene] = [athGene]

trogFile.close()

# Searching ortho in at leat 2 integrative orthofile

#current Brassica napus gene
for curBranu in listBranus:
    outputFile.write(curBranu.branuName)

    #iterate over list of Rapa similarities
    for rapMatch in curBranu.listRapa:
        matchArabiCounts = {}
        # 1 check in anchor list of orthologs
        if rapMatch in anchorMap:
            for arabiortho in anchorMap.get(rapMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1
        # 2 check in bhif list of orthologs
        if rapMatch in bhifMap:
            for arabiortho in bhifMap.get(rapMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        # 3 check in ortho list of orthologs
        if rapMatch in orthoMap:
            for arabiortho in orthoMap.get(rapMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        # 4 check in ortho list of orthologs
        if rapMatch in trogMap:
            for arabiortho in trogMap.get(rapMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        arabiOrthoKeys = list(matchArabiCounts.keys())
        arabiOrthoKeys.sort()

        #Check the sum of the arabidpsis matches across the 4 files
        for arabiKey in arabiOrthoKeys:
            cont = matchArabiCounts[arabiKey]
#            if cont >= 2:
            outputFile.write("\t"+rapMatch+","+arabiKey+","+str(cont))

    #iterate over list of Oleracea similarities
    for oleMatch in curBranu.listOle:
        matchArabiCounts = {}
        # 1 check in anchor list of orthologs
        if oleMatch in anchorMap:
            for arabiortho in anchorMap.get(oleMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1
        # 2 check in bhif list of orthologs
        if oleMatch in bhifMap:
            for arabiortho in bhifMap.get(oleMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        # 3 check in ortho list of orthologs
        if oleMatch in orthoMap:
            for arabiortho in orthoMap.get(oleMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        # 4 check in ortho list of orthologs
        if oleMatch in trogMap:
            for arabiortho in trogMap.get(oleMatch):
                if arabiortho in matchArabiCounts:
                    matchArabiCounts[arabiortho] += 1
                else:
                    matchArabiCounts[arabiortho] = 1

        arabiOrthoKeys = list(matchArabiCounts.keys())
        arabiOrthoKeys.sort()

        #Check the sum of the arabidpsis matches across the 4 files
        for arabiKey in arabiOrthoKeys:
            cont = matchArabiCounts[arabiKey]
#            if cont >= 2:
            outputFile.write("\t"+oleMatch+","+arabiKey+","+str(cont))



    outputFile.write("\n")




#printing
# for gene in genes:
#     outputFile.write(gene)
#     for cont in trogMap[gene]:
#         outputFile.write("\t"+cont)
#     outputFile.write("\n")

outputFile.close()

#cleaning objects
# import sys
# sys.modules[__name__].__dict__.clear()