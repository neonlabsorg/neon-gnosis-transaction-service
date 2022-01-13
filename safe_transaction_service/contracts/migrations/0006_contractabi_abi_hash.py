# Generated by Django 3.2.5 on 2021-07-15 12:39
import json

from django.db import IntegrityError, migrations, transaction

from web3 import Web3

import gnosis.eth.django.models


def add_hash_for_contract_abis(apps, schema_editor):
    ContractAbi = apps.get_model("contracts", "ContractAbi")
    for contract_abi in ContractAbi.objects.iterator():
        try:
            with transaction.atomic():
                contract_abi.abi_hash = Web3.keccak(
                    text=json.dumps(contract_abi.abi, separators=(",", ":"))
                )
                contract_abi.save(update_fields=["abi_hash"])
        except IntegrityError:
            contract_abi.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0005_alter_contractabi_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="contractabi",
            name="abi_hash",
            field=gnosis.eth.django.models.Sha3HashField(
                blank=True, default=None, null=True, unique=True
            ),
        ),
        migrations.RunPython(
            add_hash_for_contract_abis, reverse_code=migrations.RunPython.noop
        ),
    ]
