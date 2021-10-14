import vcf

def trim_VCF(vcf_in, vcf_out, num_lines):
	vcf_reader = vcf.Reader(open(vcf_in, 'r'))
	vcf_writer = vcf.Writer(open(vcf_out, 'w'), vcf_reader)

	counter = 0

	for record in vcf_reader: # Each record

		counter += 1
		if counter < num_lines:
			vcf_writer.write_record(record) # Keep that locus
		else:
			break

def random_sample_selection(vcf_in, tab_out, num_SNPs):
	vcf_reader = vcf.Reader(open(vcf_in, 'r'))
	with open(tab_out, "w") as out_file:

		#print header
		out_file.write(f"Reference\tPosition\tID\tReference allele\t"
			 f"Alternate allele(s)")

		for sample in vcf_reader.samples:
			out_file.write(f"\t{sample}")

		out_file.write("\n")

		counter_limit = 1
		i = 0
		for record in vcf_reader:
			i += 1
			if i <= counter_limit:
				out_file.write(f"{record.CHROM}\t{record.POS}\t{record.ID}\t{record.REF}\t{record.ALT}")
				for sample in vcf_reader.samples:
					#out_file.write(f"\t{sample['GT']}")
					call = record.genotype(sample)
					out_file.write(f"\t{call.gt_bases}")
				out_file.write("\n")
				counter_limit += 10





in_file = 'D:\\DanielRijk\QC\\bean_pv_faiza_10K.vcf'
#out_file = 'D:\DanielRijk\QC\\bean_pv_faiza_100_out.vcf'
out_file = "D:\DanielRijk\QC\\bean_pv_faiza_100_out.tsv"

#trim_VCF(in_file,out_file,100)
random_sample_selection(in_file,out_file,1000)
