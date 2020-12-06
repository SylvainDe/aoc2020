set -x

day=$(date "+%-d")
year=$(date "+%Y")
puzzle_url="https://adventofcode.com/${year}/day/${day}"
input_url="https://adventofcode.com/${year}/day/${day}/input"
input_file="day${day}_input.txt"
script_file="day${day}.py"

firefox "${puzzle_url}"
firefox "${input_url}"
touch "${input_file}"
cp ./day_template.py "${script_file}"
echo -e "\n${puzzle_url} : 0/2" >> README.md

git add "${input_file}" "${script_file}" README.md
git commit -m "Day ${day} - part 1"

vim "${script_file}" "${input_file}"
