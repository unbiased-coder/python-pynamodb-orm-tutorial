from model import UnbiasedCoderTable

def print_pynamodb_items(items):
    """
    Prints all PynamoDB Items

    Args:
        items (_type_): List of items
    """
    while True:
        try:
            next_item = items.next()
            print ('Item: ', next_item.serialize())
        except StopIteration:
            break

print ('Getting All Item from DynamoDB Using Scan')

unbiased_coder_items = UnbiasedCoderTable.scan()

print ('Retrieved Item Count Using Scan: ')
print_pynamodb_items(unbiased_coder_items)


unbiased_coder_items = UnbiasedCoderTable.query(hash_key='Unbiased', range_key_condition=UnbiasedCoderTable.surname.startswith('Coder'))

print ('Retrieved Item Count Using Query (name=Unbiased, surname=Coder): ')
print_pynamodb_items(unbiased_coder_items)
