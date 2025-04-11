from Bio import SeqIO

def load_fasta(file_path):
    """
    Loads protein sequences from a FASTA file.
    Returns a list of tuples: (id, sequence)
    """
    return [(record.id, str(record.seq)) for record in SeqIO.parse(file_path, "fasta")]
