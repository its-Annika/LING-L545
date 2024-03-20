hfst-twolc grn.twol -o grn.twol.hfst

make
hfst-lexc grn.lexc -o grn.lexc.hfst

hfst-compose-intersect -1 grn.lexc.hfst -2 grn.twol.hfst -o grn.gen.hfst

hfst-fst2strings grn.gen.hfst
