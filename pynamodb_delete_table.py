from model import UnbiasedCoderTable

if not UnbiasedCoderTable.exists():
    print ('Unbiased Coder Table does not exist theres nothing to delete')
else:
    print ('Found Unbiased Coder Table, proceeding with delete')
    UnbiasedCoderTable.delete_table()


