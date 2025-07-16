#!/bin/bash
mkdir -p images docs scripts
mv *.jpg *.png images 2>/dev/null
mv *.txt *.pdf docs 2>/dev/null
mv *.sh scripts 2>/dev/null
echo "Files sorted!"


