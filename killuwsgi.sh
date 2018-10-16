
#!/bin/sh
NAME="uwsgi"  
if [ ! -n "$NAME" ];then  
    echo "no arguments"  
    exit;  
fi  
  
echo $NAME  
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`  
echo $ID  
echo "################################################"  
for id in $ID  
do  
kill -9 $id  
echo "kill $id"  
done  
echo  "################################################"

uwsgi -x ~/tjbaoan/myproject.xml
echo "uwsgi has been restartd!"
NAME="nginx"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi

echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "################################################"
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "################################################"
nginx
