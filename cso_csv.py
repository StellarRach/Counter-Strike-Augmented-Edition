"""
TEA-like 64-bit block encrypt/decrypt (in-place).

- Operates on 8-byte chunks within a mutable bytearray.
- Key is a sequence of 4 integers (32-bit each).
"""
from typing import Sequence
import sys
import os

_DELTA = 0x9E3779B9
_MASK32 = 0xFFFFFFFF


def _u32(x: int) -> int:
    return x & _MASK32


def _get_u32_le(buf: bytearray, off: int) -> int:
    return int.from_bytes(buf[off:off + 4], 'little')


def _set_u32_le(buf: bytearray, off: int, val: int) -> None:
    buf[off:off + 4] = _u32(val).to_bytes(4, 'little')


def _norm_key(key: Sequence[int]) -> tuple[int, int, int, int]:
    if len(key) != 4:
        raise ValueError("key must contain exactly 4 integers")
    return tuple(_u32(k) for k in key)  # type: ignore[return-value]


def encrypt_chunk(buf: bytearray, key: Sequence[int], offset: int = 0) -> None:
    """Encrypt a single 8-byte chunk in-place starting at offset."""
    if offset < 0 or offset + 8 > len(buf):
        raise ValueError("buffer too small for 8-byte chunk at the given offset")

    k0, k1, k2, k3 = _norm_key(key)
    x = _get_u32_le(buf, offset)
    y = _get_u32_le(buf, offset + 4)

    for i in range(32):
        # Update x
        t1 = _u32((i + 1) * _DELTA + y)
        t2 = _u32(k0 + _u32(16 * y))
        t3 = _u32(k1 + (y >> 5))
        x = _u32(x + (t1 ^ t2 ^ t3))

        # Update y using new x
        t1 = _u32((i + 1) * _DELTA + x)
        t2 = _u32(k2 + _u32(16 * x))
        t3 = _u32(k3 + (x >> 5))
        y = _u32(y + (t1 ^ t2 ^ t3))

    _set_u32_le(buf, offset, x)
    _set_u32_le(buf, offset + 4, y)


def decrypt_chunk(buf: bytearray, key: Sequence[int], offset: int = 0) -> None:
    """Decrypt a single 8-byte chunk in-place starting at offset."""
    if offset < 0 or offset + 8 > len(buf):
        raise ValueError("buffer too small for 8-byte chunk at the given offset")

    k0, k1, k2, k3 = _norm_key(key)
    x = _get_u32_le(buf, offset)
    y = _get_u32_le(buf, offset + 4)

    for i in range(32):
        # y depends on current x
        t1 = _u32((32 - i) * _DELTA + x)
        t2 = _u32(k2 + _u32(16 * x))
        t3 = _u32(k3 + (x >> 5))
        y = _u32(y - (t1 ^ t2 ^ t3))

        # x depends on new y
        t1 = _u32((32 - i) * _DELTA + y)
        t2 = _u32(k0 + _u32(16 * y))
        t3 = _u32(k1 + (y >> 5))
        x = _u32(x - (t1 ^ t2 ^ t3))

    _set_u32_le(buf, offset, x)
    _set_u32_le(buf, offset + 4, y)

def decrypt_cso(data: bytes, key: Sequence[int] = [0xB38520FD, 0x5F30E75F, 0xE2EB67E0, 0xFC67A521]) -> bytes:
    ba = bytearray(data)
    for i in range(0, (len(data)-1)//8+1):
        decrypt_chunk(ba, key, i*8)
    return bytes(ba)

def encrypt_csv(data: bytes, key: Sequence[int] = [0xB38520FD, 0x5F30E75F, 0xE2EB67E0, 0xFC67A521]) -> bytes:
    ba = bytearray(data + b'\x00' * (8 - len(data) % 8))
    for i in range(0, (len(data)-1)//8+1):
        encrypt_chunk(ba, key, i*8)
    return bytes(ba)

if __name__ == "__main__":

    args = sys.argv[1:]
    if not args:
        prog = os.path.basename(sys.argv[0]) or "cso_csv.py"
        print(f"Usage: {prog} <file> [<file> ...]", file=sys.stderr)
        sys.exit(1)

    for path in args:
        if not os.path.isfile(path):
            print(f"Error: file not found: {path}", file=sys.stderr)
            continue
        split = os.path.splitext(path)
        base = split[0]
        ext = split[1].lower()
        if ext != '.csv' and ext != '.cso':
            print(f"Error: unsupported file extension (only .csv and .cso supported): {path}", file=sys.stderr)
            continue
        enc = (ext == '.csv')
        try:
            with open(path, "rb") as f:
                data = f.read()
            if enc:
                data = encrypt_csv(data)
            else:
                data = decrypt_cso(data)

            base += ('.cso' if enc else '.csv')
            with open(base, "wb") as f:
                f.write(data if enc else data.rstrip(b'\x00'))

            print(f"Processed {path} -> {base}")
        except Exception as e:
            print(f"Error processing {path}: {e}", file=sys.stderr)
