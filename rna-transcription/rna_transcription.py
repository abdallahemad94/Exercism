def to_rna(dna_strand):
    DtoR = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in dna_strand.upper():
        if i not in DtoR:
            raise ValueError('Invalid DNA Strand')
    return ''.join([DtoR[i] for i in dna_strand.upper()])
