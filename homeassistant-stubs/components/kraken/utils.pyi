from pykrakenapi.pykrakenapi import KrakenAPI as KrakenAPI

def get_tradable_asset_pairs(kraken_api: KrakenAPI) -> dict[str, str]: ...