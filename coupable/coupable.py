def coupable(DNA):
    if ("CATA" in DNA
            and "ATGC" in DNA
            and abs(DNA.find("CATA") - DNA.find("ATGC")) > 4):
        return True
    else:
        return False


if coupable("CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN"):
    print("Colonel Moutarde est coupable.")
if coupable("CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"):
    print("Mlle Rose est coupable.")
if coupable("AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN"):
    print("Mme Pervenche est coupable.")
if coupable("CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"):
    print("Mr Leblanc est coupable.")