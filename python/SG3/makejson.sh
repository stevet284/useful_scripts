
echo "{"
cat codes.raw | while read line
do
code=$(echo $line |awk ' {print $1} ')
text=$(echo $line |cut -c 6-500)
echo \"$code\": \"$text\",
done
echo "}"
