#!/bin/bash

if [ -z "$1" ]; then
    echo "[*] Usage: $0 <file>";
    exit 1;
fi

if [ ! -e "$1" ]; then
    echo "[*] File not found";
    exit 1;
fi

echo "[*] Now to bribe the gatekeeper..."

eval "xattr -d com.apple.quarantine $1";

# check if finished successfully
if [ $? -eq 0 ]; then
    echo "[*] Done! Now you are free to pass! :)";
else
    echo "[*] Already you are free to pass! :)";
fi