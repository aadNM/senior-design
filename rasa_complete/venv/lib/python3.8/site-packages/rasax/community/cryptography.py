from typing import Tuple
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat


def generate_rsa_key_pair(
    bits: int = 2048,
    public_key_encoding: Encoding = Encoding.PEM,
    public_key_format: PublicFormat = PublicFormat.SubjectPublicKeyInfo,
) -> Tuple[bytes, bytes]:
    """Generate an RSA key pair of size `bits`.

     Args:
        bits: Size of the RSA key.
        public_key_encoding: The encoding which the public key should use.
        public_key_format: The format the public key should have.

    Returns:
        Tuple of (private key, public key).
    """

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization

    private_key = rsa.generate_private_key(
        public_exponent=65537,  # recommended public exponent: https://bit.ly/31TSXgD
        key_size=bits,
        backend=default_backend(),
    )
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=public_key_encoding, format=public_key_format
    )

    return private_key_pem, public_key_pem


def generate_rsa_key_pair_in_open_ssh_format(bits: int = 2048) -> Tuple[bytes, bytes]:
    """Generate a RKS key with the public key in OpenSSH format.

    Args:
        bits: Size of the RSA key.

    Returns:
        Tuple of (private key, public key) where the private key is in PKCS8 format and
        the public key is in OpenSSH format.
    """
    return generate_rsa_key_pair(
        bits,
        public_key_encoding=Encoding.OpenSSH,
        public_key_format=PublicFormat.OpenSSH,
    )
