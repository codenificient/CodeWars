function DNAStrand(dna){
  let newStr = ''
  let strand = new Map()
  strand.set("C", "G")
  strand.set("G", "C")
  strand.set("A", "T")
  strand.set("T", "A")
  
  //your code here
  let letters = dna.split('')
  for (let letter of letters) {
    while (dna.includes(letter)) {
           newStr = dna.replace(letter, strand.get(letter))
           })
  }
  return newStr
}