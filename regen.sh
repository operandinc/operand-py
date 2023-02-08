#!/bin/bash

# This script is used to regenerate the auto-generated bits of this client library.

rm -rf mcp/
buf generate buf.build/operand/mcp
# Make sure to ad ... before the imports in file and operand generated files.