i=1

while [ $i -gt 0 ]
do
  sleep 30
  echo Hours left: $i
  ((i--))
done

python3 test.py