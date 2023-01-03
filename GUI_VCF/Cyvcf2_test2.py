from cyvcf2 import VCF

in_file = '/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Testing1sample/104197-124.hard-filtered.gvcf.gz'

vcf = VCF(in_file)

samples = vcf.samples

print(samples)

counter = 0

limit = 10

for record in vcf:
    counter += 1
    # print(record)
    # print(record.CHROM + "\t" + str(record.start) + "\t" + str(record.ID) + "\t" + record.REF + "\t" + str(record.ALT))
    print(record.CHROM, record.start, record.ID, record.REF, record.ALT)

    if counter == limit:
        break

