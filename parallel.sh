mkdir -p logs
rm -rf logs
mkdir logs

python3 wordle.py > logs/res_0.log -e 0 1000 &
python3 wordle.py > logs/res_1.log -e 1000 2000 &
python3 wordle.py > logs/res_2.log -e 2000 3000 &
python3 wordle.py > logs/res_3.log -e 3000 4000 &
python3 wordle.py > logs/res_4.log -e 4000 5000 &
python3 wordle.py > logs/res_5.log -e 5000 6000 &
python3 wordle.py > logs/res_6.log -e 6000 7000 &
python3 wordle.py > logs/res_7.log -e 7000 8000 &
python3 wordle.py > logs/res_8.log -e 8000 9000 &
python3 wordle.py > logs/res_9.log -e 9000 10000 &
python3 wordle.py > logs/res_10.log -e 10000 11000 &
python3 wordle.py > logs/res_11.log -e 11000 12000 &
python3 wordle.py > logs/res_12.log -e 12000 13000 &
python3 wordle.py > logs/res_13.log -e 13000 14000 &
python3 wordle.py > logs/res_14.log -e 14000 15000 &

wait
results=$(
  cat logs/* | grep -iv 'progress' | grep -iv 'solved' | grep -iv 'failed'
)
echo "15\n$results" | python3 merge.py > logs/res.log

