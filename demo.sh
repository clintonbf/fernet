#!/bin/bash

MESSAGE="Hello HoboCat"
E_MESSAGE="e_message.txt"

echo "This demo uses the file 'keyfile' as the encryption key source"

python3.8 dc_encrypt $MESSAGE > $E_MESSAGE

python3.8 dc_decrypt $E_MESSAGE