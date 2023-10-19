import re


def is_valid_bitcoin_address(address):
    try:
        legacy_pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        bech32_pattern = r"^(bc1)[0-9A-Za-z]{25,84}$"
        if re.match(legacy_pattern, address) or re.match(bech32_pattern, address):
            return True
        else:
            return False
    except Exception as e:
        return False


bitcoin_address = input("Enter a Bitcoin address: ")

if is_valid_bitcoin_address(bitcoin_address):
    print("Valid Bitcoin Address")
else:
    print("Invalid Bitcoin Address")
