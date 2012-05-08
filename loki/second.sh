
for chili in *.txt
do 
  tail -2 $chili | head -1
done
