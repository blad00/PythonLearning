
with open("D:\DanielVIB\Maize\MoreDataSets\PearsonNetworks\ConsolidateCut\ProcessesRecallNoBP.txt", "r") as fileSAC,\
        open("D:\DanielVIB\Maize\MoreDataSets\PearsonNetworks\ConsolidateCut\ProcessesRecallKrem.txt", "r") as fileKrem,\
		    open("D:\DanielVIB\Maize\MoreDataSets\PearsonNetworks\ConsolidateCut\ProcessesRecallKremNoBP.txt", "w") as outfile:

    #Load krem file into a dic
    # skip head
    next(fileKrem)
    kremRecords = {}

    for line in fileKrem:
        fields = line.split("\t")
        proc = fields[0]
        kremRecords[proc] = line

#iterateSAC to print Krem in the same format

    # print head
    outfile.write(next(fileSAC))
    for line in fileSAC:
        fields = line.split("\t")
        proc = fields[0]
        lineKrem = kremRecords.get(proc)
        outfile.write(lineKrem)


