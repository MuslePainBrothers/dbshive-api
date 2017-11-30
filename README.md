# dbshive-api
web -> [dbshive-web](https://github.com/MuslePainBrothers/dbshive-web)

## 環境
- python v3.6.3

## セットアップ
```
$ pip install requirements.txt
$ ./setup.sh
```

## 起動
```
python run.py
```

## スクリプト
`script/`にあるコマンドの説明
* databasedump.sh
  
  - データベースのバックアップ
* tabledump.sh
  
  - テーブルのバックアップ
* backup.sh
  
  - 全てのバックアップ
* update_db.sh
  
  - バックアップされたデータの更新(用途はあまりない気がする)
