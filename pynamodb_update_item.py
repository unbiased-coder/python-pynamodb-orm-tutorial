from model import UnbiasedCoderTable

print ('Updating Item name: Unbiased Coder to: Unbiased c0der')

unbiased_coder_item = UnbiasedCoderTable.get('Unbiased', 'Coder')

unbiased_coder_item.update(
    actions=[
        UnbiasedCoderTable.twittername.set('@unbiasedcoder')
    ]
)