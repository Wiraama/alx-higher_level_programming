--script that creates the database hbtn_0c_0 in your MySQL server.--
--If the database hbtn_0c_0 already exists, your script should not fail--
MYSQL_USER="your_mysql_user"

echo "Enter MySQL password for user $MYSQL_USER:"
read -s MYSQL_PASSWORD

mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "CREATE DATABASE IF NOT EXISTS hbtn_0c_0;"
