#testaa onko validi ethereum osoite
import webbrowser



print("Test for valid Ethereum address")
charset = "1234567890abcdefx"

def test_address(address):
    if address[0:2].lower() == "0x" and len(address) == 42 and all(c in charset for c in address.lower()):
        print("Valid Ethereum address: " + address + " Opening etherscan")
        return True
    else:
        print("Invalid address: " + address + " Try again")
        return False

while True:
    address = input("Input Ethereum address: ")
    if test_address(address):
        webbrowser.open('https://etherscan.io/address/' + address)
        break

