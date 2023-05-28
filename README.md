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


# 環境についてメモ
## インストールする必要のあるパッケージとそのバージョン
・python 3.11.3
・//LabelImg 1.8.6

・pyyaml 5.1 「py -3.11 -m pyyaml==5.1」==の左右に空白入れない

・Detectron2 0.6
・Pillow>=7.1
・matplotlib
・pycocotools>=2.0.2
・termcolor>=1.1
・yacs>=0.1.8
・tabulate
・cloudpickle
・tqdm>4.29.0
・tensorboard
・fvcore<0.1.6,>=0.1.5
・iopath<0.1.10,>=0.1.7
・omegaconf>=2.1
・hydra-core>=1.1
・black
・packaging

・torch==1.10.0+cu113 https://pytorch.org/get-started/previous-versions/　ここ参照してバージョンが合ってるか確認。正直もうちょっと最新のやつ使いたい
・torchvision==0.11.1+cu113
・torchaudio===0.10.0+cu113

## install時のメモ
pythonはぐぐって公式からインストーラーをダウンロードし、インストールすればいい。
このときpyrcc5が同時にインストールされたりされなかったりするのはよくわからない。

//labelImgのinstallはWindowsPowerShellで「py -3.11 -m pip install labelImg」をたたけばok。-3.11の部分は自分のバージョンに合わせて変えてください

pyyaml、pytorchもpipでインストールする「py -3.11 -m install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html」

# 以下メモ

pip install -e '.[dev]'　で少し止まるかもしれないが待てばいける。

そしてGPUがある環境じゃないのでノートパソコンでやるのは無理なことがわかった。

まぁサーバーにあげたときcloneして、諸々インストールすれば即使えるみたいな環境が作れたのでヨシ☞

detectron2で大腿骨、膝などのセグメンテーションが可能かを調べる。またセグメンテーションの細かさを指定する変数を見つける。

https://kitigai.hatenablog.com/entry/2019/08/06/003834
デフォルトだとdetectron2がfacebookのgithubにpushし始めるので上のように、「cd ./detectron2」、「git remote set-url origin https://github.com/oswystk15662/Roentgen_Detectron2」「cd ..」をしてからadd、commit、pushをしてください。