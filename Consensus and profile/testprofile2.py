import argparse
from numpy import *
 
def main(args):
    '''Returns a consensus sequence and profile matrix for a collection of sequences'''
    
    profile = zeros( (4,1000), dtype=int16 )
    base_to_index_dict = { 'A':0, 'C':1, 'G':2, 'T':3 }
    index_to_base_dict = { 0:'A', 1:'C', 2:'G', 3:'T' }
    
    input = args.input_file.read()
    for seq_record in input.split(">"):
        if seq_record == '':
            continue
        else:
            record = seq_record.split("\n")
            #print( record )
            record_id = record[0]
            dna_string = ''.join(record[1:])
            #print( record_id, dna_string, gc_count(dna_string), sep='\n' )
            add_to_profile_matrix( dna_string, profile, base_to_index_dict )
            if( args.debug == 1 ):
                print( profile )
    
    consensus = []
    for i in range(0,1000):
        counts = profile[:,i]
        if sum( counts) == 0:
            break
        max_count = 0
        j = 0
        for count in counts:
            if count > max_count:
                max_count = count
                max_base = index_to_base_dict[ j ]
            j = j + 1
        consensus.append( max_base )
        i = i + 1
    
    print( ''.join( consensus ) )
    print( 'A:', str( profile[0,:i] ) )
    print( 'C:', str( profile[1,:i] ) )
    print( 'G:', str( profile[2,:i] ) )
    print( 'T:', str( profile[3,:i] ) )
    
def add_to_profile_matrix( dna, profile, base_to_index_dict ):
    i = 0
    for base in dna:
        profile[ base_to_index_dict[base], i ] = profile[ base_to_index_dict[base], i ] + 1
        i = i + 1
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_file', metavar='FILE', type=argparse.FileType('r'),
        help='10 sequences in fasta format')
    parser.add_argument('--debug', action='count', default=0,
        help='Prints debugging information')
    args = parser.parse_args()
    main(args)
 