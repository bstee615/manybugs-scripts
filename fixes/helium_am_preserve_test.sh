dir='/home/benjis/work/benchmarks/manybugs/inputs/gzip/gzip-bug-2009-10-09-1a085b1446-118a107f2d/gzip'

# arrange

cp -r . $dir/trailing-nul-before

# act

cp -r . $dir/trailing-nul-after

# assert
