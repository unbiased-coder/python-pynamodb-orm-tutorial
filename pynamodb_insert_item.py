from model import UnbiasedCoderTable

print ('Adding 3 items in DynamoDB')

unbiased_coder_item1 = UnbiasedCoderTable(
    name = 'Unbiased',
    surname = 'Coder'
).save()

unbiased_coder_item2 = UnbiasedCoderTable(
    name = 'Alex',
    surname = 'Smith'
).save()

unbiased_coder_item3 = UnbiasedCoderTable(
    name = 'John',
    surname = 'Williams'
).save()

print ('Completed saving 3 items in DB')
