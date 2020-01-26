#!/usr/bin/python3


import random
import sys

def usage():
        print(
           """\n This Python script will generate a random fasta file with genetic
                 sequence of type [rna/dna/aa] and of length [SEQUENCE_LENGTH]



                 USAGE:
                         seqGen [type = rna/dna/aa] [length = SEQUENCE_LENGTH] [name = SEQUENCE_NAME]


                 note to self: What to implement in the futur:
                                                        -Ability to change sequence name
                                                        -Ability to specify exon/intron CDS/(5/3)UTR
                                                        -other file formats (FASTQ)
                                                        -Generate sequence given shannon index
                                                        -Generate LCR of length n and position x
                                                                                        \n""")


#if (len(sys.argv) == 1) or (sys.argv[1] == "--help"):
#       usage()
#       sys.exit()

for arg in sys.argv:
        if ("help" in arg) or (len(sys.argv) == 1) :
                usage()
                sys.exit()


class randomGen():

        def __init__ (self): #, str_seqType, int_segLength):

                self.str_seqType = sys.argv[1]
                self.int_seqLength = int(sys.argv[2])
                self.str_rna = list("AUCG")
                self.str_dna = list("ATCG")
                self.str_protein = list("ACDEFGHIKLMNPQRSTVWY")

        def sequenceType(self):
                cmdArgs = self.str_seqType
                if cmdArgs == "rna":
                        return self.str_rna
                elif cmdArgs == "dna":
                        return self.str_dna
                elif cmdArgs == "aa":
                        return self.str_protein
                else:
                        usage()

        def sequenceLength(self):
                seqLength = self.int_seqLength
                if not(isinstance(seqLength, int)):
                        usage()
                return seqLength

        def makeSequence (self):
                list_gen = self.sequenceType()
                int_len = self.sequenceLength()
                list_seq = []

                while(int_len > 0):

                        int_len -= 1
                        random.shuffle(list_gen)
                        list_seq.append(list_gen[0])




                return list_seq

        def makeFasta (self, gen_list):
                myFileName = ("ENST" + str(random.randrange(200000000, 999999999)) + ".fasta")
                f = open("".join(myFileName), 'x')
                f.write('>' +'mySequence\n')

                for i in gen_list:
                        f.write(i)
                f.close()


sequence = randomGen()

results = sequence.makeSequence()

sequence.makeFasta(results)





