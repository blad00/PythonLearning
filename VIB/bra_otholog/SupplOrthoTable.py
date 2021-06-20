class BestOrtholog:

	def __init__(self, **kwargs):
		self._BnapusName = kwargs["name"]    # instance variable unique to each instance
		self._listTargets_CST = []
		self._listTargets_CS = []
		self._listTargets_C_S = []
		self._listTargets_CT_ST = []
		self._listTargets_T = []

	def name(self):
		return self._BnapusName

	def CST(self, o = None):
		if o: self._listTargets_CST.append(o)
		try: return self._listTargets_CST
		except AttributeError: return None

	def CS(self, o = None):
		if o: self._listTargets_CS.append(o)
		try: return self._listTargets_CS
		except AttributeError: return None

	def C_S(self, o = None):
		if o: self._listTargets_C_S.append(o)
		try: return self._listTargets_C_S
		except AttributeError: return None

	def CT_ST(self, o = None):
		if o: self._listTargets_CT_ST.append(o)
		try: return self._listTargets_CT_ST
		except AttributeError: return None

	def T(self, o = None):
		if o: self._listTargets_T.append(o)
		try: return self._listTargets_T
		except AttributeError: return None



class AthOrtholog:

	def __init__(self, **kwargs):
		self._athName = kwargs["name"]    # instance variable unique to each instance
		self._list_1_int = []
		self._list_2_int = []
		self._list_3_int = []
		self._list_4_int = []

	def name(self):
		return self._athName

	def list_1_int(self, o = None):
		if o: self._list_1_int.append(o)
		try: return self._list_1_int
		except AttributeError: return None

	def list_2_int(self, o = None):
		if o: self._list_2_int.append(o)
		try: return self._list_2_int
		except AttributeError: return None

	def list_3_int(self, o = None):
		if o: self._list_3_int.append(o)
		try: return self._list_3_int
		except AttributeError: return None

	def list_4_int(self, o = None):
		if o: self._list_4_int.append(o)
		try: return self._list_4_int
		except AttributeError: return None


#load main file

napus_ortho_file = "D:\DanielVIB\Brassica\Annotation2020TRAPID\AnnotStevenFolder\synteny\\bna.tsv"

napus_ortho = open(napus_ortho_file, "r")

# skip header
next(napus_ortho)

cu_bnapus_gene = ""
branu = None

map_bnapus = {}

for line in napus_ortho:
	fields = line.rstrip().split("\t")
	#first case
	if cu_bnapus_gene == "":
		branu = BestOrtholog(name = fields[0])
		cu_bnapus_gene = fields[0]

	#if it is a new Bnapus Gene create
	if cu_bnapus_gene != fields[0]:
		map_bnapus[branu.name()] = branu
		branu = BestOrtholog(name = fields[0])
		cu_bnapus_gene = fields[0]

	#add new rapa or ole gene to its specific set
	if fields[2] == "CST":
		branu.CST(fields[1])
	elif fields[2] == "CS":
		branu.CS(fields[1])
	elif fields[2] == "C" or fields[2] == "S":
		branu.C_S(fields[1])
	elif fields[2] == "CT" or fields[2] == "ST":
		branu.CT_ST(fields[1])
	elif fields[2] == "T":
		branu.T(fields[1])

#last item to add
map_bnapus[branu.name()] = branu
napus_ortho.close()


# load arabidopsis orthologs
ath_ortho_file = "D:\DanielVIB\Brassica\Annotation2020TRAPID\AnnotStevenFolder\synteny\\ath.tsv"

ath_ortho = open(ath_ortho_file, "r")

cu_ortho_gene = ""
ortho_tmp = None

map_b_ath = {}

# skip header
next(ath_ortho)

for line in ath_ortho:
	fields = line.rstrip().split("\t")
	# first case
	if cu_ortho_gene == "":
		ortho_tmp = AthOrtholog(name=fields[0])
		cu_ortho_gene = fields[0]

	# if it is a new Bnapus Gene create
	if cu_ortho_gene != fields[0]:
		map_b_ath[ortho_tmp.name()] = ortho_tmp
		ortho_tmp = AthOrtholog(name=fields[0])
		cu_ortho_gene = fields[0]

	if len(fields[2]) == 1:
		ortho_tmp.list_1_int().append(fields[1])
	elif len(fields[2]) == 2:
		ortho_tmp.list_2_int().append(fields[1])
	elif len(fields[2]) == 3:
		ortho_tmp.list_3_int().append(fields[1])
	elif len(fields[2]) == 4:
		ortho_tmp.list_4_int().append(fields[1])

#last item to add
map_b_ath[ortho_tmp.name()] = ortho_tmp
ath_ortho.close()


#iterate over the map of bnapus genes for final report

outputFile = "D:\DanielVIB\Brassica\Annotation2020TRAPID\AnnotStevenFolder\\report.tsv"
output = open(outputFile, 'w')

output.write(f"B. napus gene\tB.rapa/oleracea candidate ortholog\tevidence\tA.th candidate ortholog\t#Integrative sources\t#supported Ath Ortholog\tA.th alternative name\tA.th gene description\n")

keys_bnapus = list(map_bnapus.keys())
keys_bnapus.sort()

str_evi_winner = ""

for key_bna in keys_bnapus:
	branu = map_bnapus.get(key_bna)

#Select the most relevant list best CST

	re_list = None

	if len(branu.CST()) > 0:
		re_list = branu.CST()
		str_evi_winner = "CST"
	elif len(branu.CS()) > 0:
		re_list = branu.CS()
		str_evi_winner = "CS"
	elif len(branu.C_S()) > 0:
		re_list = branu.C_S()
		str_evi_winner = "C/S"
	elif len(branu.CT_ST()) > 0:
		re_list = branu.CT_ST()
		str_evi_winner = "CT/ST"
	elif len(branu.T()) > 0:
		re_list = branu.T()
		str_evi_winner = "T"


#get the best ath ortholog

	list_ath_winner = []
	num_list_winner = 0
	ath_name_winner = ""

	list_ath = []
	num_list = 0
	ath_name = ""


	#print(key_bna)
	#select the winner

	for b_ortho in re_list:
		a_ortho = map_b_ath.get(b_ortho)
		if len(a_ortho.list_4_int()) > 0:
			num_list = 4
		elif len(a_ortho.list_3_int()) > 0:
			num_list = 3
		elif len(a_ortho.list_2_int()) > 0:
			num_list = 2
		elif len(a_ortho.list_1_int()) > 0:
			num_list = 1

		if num_list > num_list_winner:
			num_list_winner = num_list


	for b_ortho in re_list:
		a_ortho = map_b_ath.get(b_ortho)
		ath_name = a_ortho.name()
		if num_list_winner == 4 and len(a_ortho.list_4_int()) > 0:
			list_ath_winner = a_ortho.list_4_int()
			output.write(f"{key_bna}\t{a_ortho.name()}\t{str_evi_winner}\t{list_ath_winner[0]}\t"
						 f"{num_list_winner}\t{len(list_ath_winner)}\n")

		elif num_list_winner == 3 and len(a_ortho.list_3_int()) > 0:
			list_ath_winner = a_ortho.list_3_int()
			output.write(f"{key_bna}\t{a_ortho.name()}\t{str_evi_winner}\t{list_ath_winner[0]}\t"
						 f"{num_list_winner}\t{len(list_ath_winner)}\n")

		elif num_list_winner == 2 and len(a_ortho.list_2_int()) > 0:
			list_ath_winner = a_ortho.list_2_int()
			output.write(f"{key_bna}\t{a_ortho.name()}\t{str_evi_winner}\t{list_ath_winner[0]}\t"
						 f"{num_list_winner}\t{len(list_ath_winner)}\n")

		elif num_list_winner == 1 and len(a_ortho.list_1_int()) > 0:
			list_ath_winner = a_ortho.list_1_int()
			output.write(f"{key_bna}\t{a_ortho.name()}\t{str_evi_winner}\t{list_ath_winner[0]}\t"
						 f"{num_list_winner}\t{len(list_ath_winner)}\n")


output.close()