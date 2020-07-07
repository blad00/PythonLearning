import vcf
#print(VCFdata)

NotColumn = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

Genotype = VCFdata[['#CHROM', 'POS', 'REF', 'ALT']].copy()

#print(Genotype)

samplelist = list(VCFdata.columns[9:])
#print(samplelist)

counter = 0

for col in VCFdata:
    sample = []
    samplename = samplelist[counter]
    if col not in NotColumn:
        for i, row_value in VCFdata[col].iteritems():
            #Change between / and | depending on the VCF format...
            if '0|0' in VCFdata[col][i]:
                sample.append(0)
            elif '0|1' in VCFdata[col][i] or '1|0' in VCFdata[col][i]:
                sample.append(1)
            elif '1|1' in VCFdata[col][i]:
                sample.append(2) #Twice the alternative allele, for quantification in linear models
        counter += 1
        Genotype[str(samplename)] = sample
        print(Genotype.shape,'\n\n', samplename, '\n\n')

Genotype.to_csv(r'D:/UGentBioinformatics/Thesis 2019-2020/MachineLearning/NAPUStrial3population_Q40_OnlySNP_minI154_Imputed_MAF_poly_012.txt',sep=' ', index=False, header=True)
