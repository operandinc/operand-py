#!/bin/bash

# This script is used to regenerate the auto-generated bits of this client library.

rm -rf operand/
buf generate buf.build/operand/operand --path operand
requires=("index_pb2.py" "object_pb2.py")
for f in operand/v1/*; do
    if [[ ! " ${requires[@]} " =~ " $(basename $f) " ]]; then
        rm $f
    fi
done