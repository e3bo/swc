
for chili in *.txt
do 
  cut -d , -f 2 $chili |sort | uniq -c
  echo " "
done
