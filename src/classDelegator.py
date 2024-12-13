import numpy as np
from custom_types import Gwei, Epoch

class Delegator:
    def __init__(self, delegator_id):
        self.delegator_id = delegator_id  # Unique identifier for each delegator

        # self.pubkey = BLSPubkey # for the purpose of this pyproject, we work with delegator_id instead of BLSPubkey, which will be used in the specs
        self.withdrawal_credentials: bytes = b'\x00' * 32  # Commitment to pubkey for withdrawals
        self.delegated_balance =  Gwei  # Balance at stake
         # Status epochs
        self.activation_epoch = Epoch
        self.exit_epoch = Epoch
