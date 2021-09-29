def DNA_strand(dna):
    strands = {'A': 'T',
               'T': 'A',              
               'C': 'G',
               'G': 'C' }  
              
    # code here
    for letter in dna:
        dna = dna.replace(letter, strands.get(letter))
    return dna