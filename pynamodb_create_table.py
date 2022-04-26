from model import UnbiasedCoderTable

if not UnbiasedCoderTable.exists():
    print ('Unbiased Coder Table does not exist proceed into creating it')
    UnbiasedCoderTable.create_table(read_capacity_units=10, write_capacity_units=10, wait=True)
else:
    print ('Unbiased Coder Table already exists not creating it')
