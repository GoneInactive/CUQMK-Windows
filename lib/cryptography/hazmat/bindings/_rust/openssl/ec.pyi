# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

import typing

from cryptography.hazmat.primitives.asymmetric import ec

class ECPrivateKey: ...
class ECPublicKey: ...

class EllipticCurvePrivateNumbers:
    def __init__(
        self, private_value: int, public_numbers: EllipticCurvePublicNumbers
    ) -> None: ...
    def private_key(
        self, backend: typing.Any = None
    ) -> ec.EllipticCurvePrivateKey: ...
    @property
    def private_value(self) -> int: ...
    @property
    def public_numbers(self) -> EllipticCurvePublicNumbers: ...

class EllipticCurvePublicNumbers:
    def __init__(self, x: int, y: int, curve: ec.EllipticCurve) -> None: ...
    def public_key(
        self, backend: typing.Any = None
    ) -> ec.EllipticCurvePublicKey: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    @property
    def curve(self) -> ec.EllipticCurve: ...
    def __eq__(self, other: object) -> bool: ...

def curve_supported(curve: ec.EllipticCurve) -> bool: ...
def generate_private_key(
    curve: ec.EllipticCurve, backend: typing.Any = None
) -> ec.EllipticCurvePrivateKey: ...
def from_private_numbers(
    numbers: ec.EllipticCurvePrivateNumbers,
) -> ec.EllipticCurvePrivateKey: ...
def from_public_numbers(
    numbers: ec.EllipticCurvePublicNumbers,
) -> ec.EllipticCurvePublicKey: ...
def from_public_bytes(
    curve: ec.EllipticCurve, data: bytes
) -> ec.EllipticCurvePublicKey: ...
def derive_private_key(
    private_value: int, curve: ec.EllipticCurve
) -> ec.EllipticCurvePrivateKey: ...
