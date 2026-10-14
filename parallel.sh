mkdir -p logs
rm -rf logs
mkdir logs

idx=0
num=0
step=500
limit=15000

if [ $# -gt 0 ]; then
  limit=$1
fi

if [ $# -gt 1 ]; then
  step=$2
fi

if [ $# -gt 2 ]; then
  num=$3
fi

while [ $num -lt $limit ]; do
  python3 wordle.py > logs/res_$idx.log -e $num $((num + step)) &
  num=$((num + step))
  idx=$((idx + 1))
done

wait

results=$(cat logs/*)
results=$(echo "$results" | grep -iv 'progress')
results=$(echo "$results" | grep -iv 'solved')
results=$(echo "$results" | grep -iv 'failed')

echo "$idx\n$results" | python3 merge.py > logs/res.log
cat logs/res.log

