#full_table_patch = "D:\DanielVIB\maizeEnrich\V3vsV4\\2021\MaizeGDB_B73_pangene_2020_11.tsv"
#output_file_path = "D:\DanielVIB\maizeEnrich\V3vsV4\\2021\V3_V4_tr.tsv"

full_table_patch = "/home/dacru/Midas/biocomp/groups/group_esb/dacru/maizeEnrich/V3vsV4/2021/MaizeGDB_B73_pangene_2020_11.tsv"
output_file_path = "/home/dacru/Midas/biocomp/groups/group_esb/dacru/maizeEnrich/V3vsV4/2021/V3_V4_ck.tsv"

with open(full_table_patch, "r") as full_table,\
        open(output_file_path, "w") as out_file:

	#skip title
	next(full_table)

	list_V3 = []
	list_V4 = []

	out_file.write(f"V3\tV4\n")

	for line in full_table:
		fields = line.rstrip().split("\t")
		#loop over fields to find only V3 and V4
		for index in range(1,len(fields)):
			if fields[index].startswith("B73v3_"):
				geneV3_tmp = fields[index].split("_")
				if len(geneV3_tmp) == 2:
					list_V3.append(geneV3_tmp[1])
				else:
					separator = "_"
					list_V3.append(separator.join(geneV3_tmp[1:]))
			elif fields[index].startswith("Zm00001d"):
				list_V4.append(fields[index])

		if not list_V3 and not list_V4:
			continue
		#print in cells
		separator = " "
		str_V3 = separator.join(list_V3)
		str_V4 = separator.join(list_V4)

		out_file.write(f"{str_V3}\t{str_V4}\n")

		list_V3.clear()
		list_V4.clear()












