Detectron2はBSDライセンス

https://qiita.com/risagon/items/0cd3592b08ee058ffb80

↓僕のnotionでレントゲンプロジェクトについてまとめたものです
https://cumbersome-pheasant-bf1.notion.site/f1d44e4ab2c544619e4827d8fb85211c

# git を使う時の注意点
0.以下のコマンドはVScodeのterminalに打ち込めば出来ます。また、先にカレントディレクトリを変更することをお勧めします
1.クローンはいつも通りしてください。
2.その後 git configを変える必要があれば変えてください。ここの話しは正直よくわかってないです。アカウントが１つの場合気にしなくて大丈夫です
3.コンフリクトを避けるためにブランチを変えてください。以下はブランチ系の使うであろうコマンド一覧です
・「git branch」でどんなブランチああるか確認できます
・「git branch sub2」でsub2というブランチが作れます
・「git checkout sub2」でsub2というブランチに移動できます

各ブランチで行った変更は別のブランチに共有されません。

4.ブランチを変えた後「git pull」で保存された変更を読み込んでください。mainブランチから読み込みたいときはsubのブランチにいることを確認してから「git merge main」でmainと同じ状況にすることが出来ます。subの方だけの物がある場合どうなるかわからないので、確認します。。

5.ファイルを変更し保存したら、git branch」で自分のいるブランチを確認した後大丈夫だった、ら「git add .」、「git commit -m "適当な変更ポイントを示すメッセージ"」、「git push」で自分のいるブランチに保存できます。

6.mainにマージさせたいときはバグがないかを確認し、管理してる人に一言伝えましょう（実際の現場がどんな感じかは不明）


# 大澤の環境についてメモ

python 3.11.3
pythonはぐぐって公式からインストーラーをダウンロードし、インストールすればいい。
このときpyrcc5が同時にインストールされたりされなかったりするのはよくわからない。

LabelImg 1.8.6
labelImgのinstallはWindowsPowerShellで僕の場合は「"Current Directry"> py -3.11 -m pip install labelImg」をたたけばok。-3.11の部分は自分のバージョンに合わせて変えてください

coco-annotatorは　https://qiita.com/PoodleMaster/items/39830656d69d34a39f34
の通りにやる
Ubuntu必須なので、とても容量持ってかれるので注意
はっきり言ってクソアプリなのでこの方法いがいでcocoファイルを生成したい

# 以下メモ

pip install -e '.[dev]'　で少し止まるかもしれないが待てばいける。

そしてGPUがある環境じゃないのでノートパソコンでやるのは無理なことがわかった。

まぁサーバーにあげたときcloneして、諸々インストールすれば即使えるみたいな環境が作れたのでヨシ☞

detectron2で大腿骨、膝などのセグメンテーションが可能かを調べる。またセグメンテーションの細かさを指定する変数を見つける。

# サーバーのディレクトリ構造
```c++
SIG_Roentgen
├諸々
├lib/
│├必要な諸々
│├学習済みデータ
├src/
│├web_controller.py//ここから↓を呼び出す形に
│├det_femur.py//大腿骨 det = detection
│├det_knee.py
│├det_spine.py 脊椎
│├index.html 
│├stylesheet.css
├Resources/
│├subjects/
││├raw/
││├processed/
│├web/
││├.icoなど

/*
フォルダ名は現場で使われそうなやつを知らないのでとりあえず、、
撮った写真に関して「 raw_" 日付時刻"」、「 done_"日付時刻"」などにするとpythonでチェックしやすい。
3つ用意したほうがいいと思った記憶があるがなぜかは忘れた
html単体で写真とる機能がある
webアプリは渡辺さんがやったことあるのでかなり頼れる
*/
```

カレントディレクトリは"SIG_roentgen"が都合がいいかも
