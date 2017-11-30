mysql -u root -h localhost -e "create database dbshive;"
mysql -u root -h localhost dbshive < sql/dbshive.sql
mysql -u root -h localhost dbshive < sql/dbshive_table.sql
