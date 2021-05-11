import os
#Search the ranking of a list of genes, on all the files in a target folder


# read first gene
#print("Imput file with ranking")
#org = input()
org = "D:\DanielVIB\Brassica\ML_Ewout\\resultsRegulators\\rf\\shootsTotalBranchCount.tsv"
#print("Imput folder to be searched")
#path = input()
path = "D:\DanielVIB\Brassica\PilotData\TF_links_sam"

# declare output file
name, ext = os.path.splitext(org)
output = "{name}_{uid}{ext}".format(name=name, uid="Out", ext=ext)
outputFile = open(output, 'w')

#iterate interesting genes
orgFile = open(org, "r")
#skip title
next(orgFile)

lineNumOrg = 0
outputFile.write("geneTrial3"+"\t"+"posTrial3"+"\t"+"fileTrial1"+"\t"+"posTrial1"+"\n")

for line in orgFile:

    fields = line.split("\t")
    geneName = fields[0]
    lineNumOrg += 1
    outputFile.write(geneName+"\t"+str(lineNumOrg))
    # iterate over target folder
    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(".tsv") and entry.is_file():
                # print(entry.name, entry.path)
                lineNumTarget = 0
                targetFile = open(entry.path, "r")
                # skip title
                next(targetFile)

                found = False

                for lineTarget in targetFile:
                    lineNumTarget += 1
                    fields = lineTarget.split("\t")
                    geneTarget = fields[0]
                    geneLink = fields[1]
                    if geneName == geneTarget or geneName == geneLink:
                        outputFile.write("\t"+entry.name+"\t"+str(lineNumTarget))
                        found = True
                        break

                if found is False:
                    outputFile.write("\t"+entry.name+"\t"+str(0))

                targetFile.close()

        outputFile.write("\n")


outputFile.close()
orgFile.close()