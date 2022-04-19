Crontab -e 
0 * * * * /inital_user_rollcall.sh | md5sum > /users/log/current_users
0 * * * * /user_rollcall.sh | md5sum > /users/log/current_users

If [[/users/log/current_user -s && cmp et 1