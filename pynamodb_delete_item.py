from model import UnbiasedCoderTable

print ('Deleting Item name: John Williams from DynamoDB')

unbiased_coder_item = UnbiasedCoderTable.get('John', 'Williams')

unbiased_coder_item.delete()

