from blockchain.blockchain import Blockchain
from ai.credential_verification import verify_credentials
import json

def main():
    blockchain = Blockchain()

    with open('data/sample_credentials.json', 'r') as file:
        sample_credentials = json.load(file)

    # Simulate adding a new credential
    blockchain.new_transaction("Hospital", "Credentialing Authority", sample_credentials)
    blockchain.new_block(proof=12345)

    # Verify the credential
    status = verify_credentials(sample_credentials)
    print("Credential Verification Status:", status)

    # Save blockchain
    with open('blockchain/credentials_chain.json', 'w') as file:
        json.dump(blockchain.chain, file)

if __name__ == "__main__":
    main()
