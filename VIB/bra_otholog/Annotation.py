class GeneAnnot:

    def __init__(self, name):
        self.branuName = name    # instance variable unique to each instance
        self.posIni = 0
        self.posFin = 0
        self.chromo = ""
        self.strand = ""

    def set_posIni(self, posIni):
        self.posIni = posIni

    def set_posFin(self, posFin):
        self.posFin = posFin

    def set_chromo(self, chromo):
        self.chromo = chromo

    def set_strand(self, strand):
        self.strand = strand