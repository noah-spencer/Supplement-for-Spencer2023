#! /bin/bash

mapfile -t contigs < <(cut -d ',' -f 1 MAGSEP.pro | uniq)

for c in "${contigs[@]}"; do
  grep -F "${c}" MAGSEP.pro > ${c}.pro
done
