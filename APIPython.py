from flask import Flask, jsonify
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = Flask(__name__)

KEY_VAULT_NAME = "VaultForLab010203"
KVUri = f"https://{KEY_VAULT_NAME}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

@app.route("/get-secret/miSecreto", methods=["GET"])
def get_secret():
    try:
        secret = client.get_secret("miSecreto")
        return jsonify({
            "secret_name": secret.name,
            "secret_value": secret.value
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "Hola"

if __name__ == "__main__":
    app.run(debug=True)
