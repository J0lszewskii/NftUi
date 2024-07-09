from pinata import Pinata

def upload_to_ipfs(filename, api_key_file):
    with open(api_key_file, "r") as file:
        lines = file.readlines()
        ap_key = lines[0].split(": ")[1].strip()
        secret_key = lines[1].split(": ")[1].strip()
        access_token = lines[2].split(": ")[1].strip()
    pinata = Pinata(ap_key, secret_key, access_token)

    response = pinata.pin_file(filename)
    return response['data']['IpfsHash']

if __name__ == "__main__":
    print(upload_to_ipfs("ipfs.py", "api_key.txt"))

