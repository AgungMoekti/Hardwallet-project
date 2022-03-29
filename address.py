import blocksmith

def address(key):
    if(key[0:2] == '0x'):
        key = key[2:len(key)]

    # address = blocksmith.EthereumWallet.generate_address(key)
    # print(address)

    checksum_address = blocksmith.EthereumWallet.checksum_address(address)
    # print(checksum_address)
    return checksum_address
