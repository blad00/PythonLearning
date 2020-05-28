
import sys
sys.path.append('D:\Desarrollo\gitDev\gitPy\PythonLearning')

from VIB.bra_otholog.Annotation import GeneAnnot
#from Annotation import GeneAnnot


def overlap(min1, max1, min2, max2):
    return min(max1, max2) - max(min1, min2)

def getBestHit(rapa4name, rapaHit3List):

    rapa4Annot = plaza4Map.get(rapa4name)
    rapa3Annots = []

    for rapa3hit in rapaHit3List:
        annoTMP = plaza3Map.get(rapa3hit[0])
        if annoTMP is not None:
            rapa3Annots.append(annoTMP)

    if len(rapa3Annots) == 0:
        return None

    #if only one hit we return
    if len(rapa3Annots) == 1:
        return rapa3Annots.pop().branuName

    #check how many rapa3 are in the same chromo as rapa4
    chromorapa4 = rapa4Annot.chromo
    countSameChromo = 0
    for rapa3rec in rapa3Annots:
        if rapa3rec.chromo == chromorapa4:
            countSameChromo += 1

    # if none was found in the same chromo we get the best evalue
    if countSameChromo == 0:
        minEvalue = 8
        minName = ""
        for rapa3name, eval in rapaHit3List:
            if eval < minEvalue:
                minEvalue = eval
                minName = rapa3name
        return minName

    #if only one was found in the same chromo that's the one
    if countSameChromo == 1:
        for rapa3rec in rapa3Annots:
            if rapa3rec.chromo == chromorapa4:
                return rapa3rec.branuName

    #if more than one were found in the query chromo we check the closest by overlap
    countOverlap = 0
    bestOverlapGene = ""
    highestOverlap = -float('inf')
    if countSameChromo > 1:
        # check if there are any with overlaping if not will return
        for rapa3rec in rapa3Annots:
            if rapa3rec.chromo == chromorapa4:
                print(rapa4Annot.branuName + "\t" + rapa4Annot.chromo + "\t" + rapa3rec.branuName + "\t" + rapa3rec.chromo)
                overlapping = overlap(rapa3rec.posIni, rapa3rec.posFin, rapa4Annot.posIni, rapa4Annot.posFin)
                if overlapping >= 0:
                    countOverlap += 1
                if overlapping > highestOverlap:
                    highestOverlap = overlapping
                    bestOverlapGene = rapa3rec.branuName


        if countOverlap >= 1:
            print("gene with multiple overlap\t"+rapa4Annot.branuName+"\t"+bestOverlapGene+"\t"+str(countOverlap))
        elif countOverlap == 0:
            print("gene with non overlap with many hits in the same chromo, closest\t"+rapa4Annot.branuName+"\t"+bestOverlapGene+"\t"+str(countOverlap))

        return bestOverlapGene

with open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\BlastRAPA\\blastoutput.txt", "r") as blastFile,\
        open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\RapaWork\\annotation.all_transcripts.exon_features.braPLAZA3.gff3", "r") as plaza3,\
            open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\RapaWork\\annotation.all_transcripts.exon_features.braPLAZA4.gff3", "r") as plaza4,\
                open("D:\DanielVIB\Brassica\Annotation2020TRAPID\Results\OrgDown\RapaWork\corrRapaTable.tsv", "w") as outfile:

    #load annotations

    plaza3Map = {}
    plaza4Map = {}

    for line in plaza3:
        if line.startswith("#"):
            continue
        fields = line.split("\t")
        if fields[2] == "gene":
            #extracting gene name
            geneName = fields[8].split(";")[0].split("=")[1]
            geneTmp = GeneAnnot(geneName)
            geneTmp.set_chromo(fields[0])
            geneTmp.set_posIni(int(fields[3]))
            geneTmp.set_posFin(int(fields[4]))
            geneTmp.set_strand(fields[6])
            #load map
            plaza3Map[geneName] = geneTmp

    for line in plaza4:
        if line.startswith("#"):
            continue
        fields = line.split("\t")
        if fields[2] == "gene":
            # extracting gene name
            geneName = fields[8].split(";")[0].split("=")[1]
            geneTmp = GeneAnnot(geneName)
            geneTmp.set_chromo(fields[0])
            geneTmp.set_posIni(int(fields[3]))
            geneTmp.set_posFin(int(fields[4]))
            geneTmp.set_strand(fields[6])
            # load map
            plaza4Map[geneName] = geneTmp

    geneNameFP4 = ""
    rapaChifu3Matches = []

    for line in blastFile:
        fields = line.split("\t")
        blastRapaGene = fields[0][:-2]
        #filling the list of a new rapa4 gene
        if geneNameFP4 == blastRapaGene:
            #add rapa3 hit and its evalue
            rapaChifu3Matches.append((fields[1], float(fields[10])))
        else:
            if geneNameFP4 != "":
                # method for dealing with the list and obtain the best hit
                bestHitName = getBestHit(geneNameFP4,rapaChifu3Matches)
                if bestHitName is not None:
                    outfile.write(geneNameFP4+"\t"+bestHitName+"\n")
#                    print(blastRapaGene+"\t"+bestHitName)

            #reset data structctures

            geneNameFP4 = blastRapaGene
            rapaChifu3Matches.clear()
            rapaChifu3Matches.append((fields[1], float(fields[10])))


        # gene = fields[0]
        # # annot = fields[2]
        # if gene in annotsCounts:
        #     annotsCounts[gene] += 1
        # else:
        #     annotsCounts[gene] = 1