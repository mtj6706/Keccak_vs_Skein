"""
A practical implementation of the Skein Hashing algorithm as a simple hashing algorithm
"""


def toBytes(integer: int, byte_len: int = None) -> bytes:
    """
    Converts an integer to a string of bytes, Least Significant Byte first
    :return: The LSB representation of an integer in bytes
    """

    if byte_len is None:
        # If the Byte length is not specified, the bare minimum of bytes will be used instead
        # By taking the number of bits in the int, and adding 7 we get a number that when divided by 8 and floored (//)
        #   we will have the amount of bytes necessary to hold it without overflow
        byte_len = (integer.bit_length() + 7) // 8

    return integer.to_bytes(byte_len, 'little')


def toInt(byte: bytes) -> int:
    """
    Converts a string of bytes to an integer, Least Significant Byte first
    :return: The LSB representation of a string of bytes as an integer
    """

    return int.from_bytes(byte, 'little')
