
cd Results

for i in {0..70000}; do
	file_name="Run${i}.txt"
        [ ! -f $file_name ] && echo "$file_name"
done