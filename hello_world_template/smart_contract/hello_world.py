from typing import Any

from boa3.builtin.compile_time import public, metadata, NeoMetadata


@metadata
def contract_manifest() -> NeoMetadata:
    """
    Defines this smart contract's metadata information.
    """
    meta = NeoMetadata()
    return meta


@public
def _deploy(data: Any, update: bool):
    """
    This method will automatically be called when the smart contract is deployed or updated.
    """
    pass
