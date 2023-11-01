#Run through 70,000 files, I had 17 files missing, so it goes through all of them in order and prints out the names of the missing one

cd Results

for i in {0..70000}; do
	file_name="Run${i}.txt"
        [ ! -f $file_name ] && echo "$file_name"
done