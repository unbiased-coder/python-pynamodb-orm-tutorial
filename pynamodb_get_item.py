from model import UnbiasedCoderTable

print ('Getting Item from DynamoDB')

unbiased_coder_item = UnbiasedCoderTable.get('Unbiased', 'Coder')

print ('Retrieved Item: ', unbiased_coder_item.serialize())
