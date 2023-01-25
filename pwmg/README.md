- pip listになければ自動インストールしてくれる機能
- windows立ち上げで自動でバックグラウンド起動（スタートアップ登録＋バックグラウンド処理）
- パスワードはテキストエディタで編集できる形式でリスト化
- パスワードの利用回数を記録
    e.g.) 
    pass1 : 100
    pass2 : 34
    pass3 : 1
- 利用回数が多いものほど上にくるようにソート
- リストにない場合は、記録されていないポップアップ表示
　「パスワードが記録されていません。新たに記録しますか？」Y/N
- Yの場合、入力画面を表示し、そのパスワードでファイルが開けたら記録
- Nの場合、Yでのファイルが開けなかったら記録しない


# PWMG : Pass Word ManaGement tool


[Python の win32gui を使ってアクティブウインドウの記録を取るスクリプトを作ってみた - Qiita](https://qiita.com/aikige/items/d7bdf26e2cb376268ed0)

[Pythonでウインドウハンドルを取得する方法 | サラリーマンがハッカーを真剣に目指す](http://bttb.s1.valueserver.jp/wordpress/blog/2017/09/28/python%e3%81%a7%e3%82%a6%e3%82%a4%e3%83%b3%e3%83%89%e3%82%a6%e3%83%8f%e3%83%b3%e3%83%89%e3%83%ab%e3%82%92%e5%8f%96%e5%be%97%e3%81%99%e3%82%8b%e6%96%b9%e6%b3%95/)



[はじめての Python-パスワード管理スクリプトをつくってあそぼう- – nujawak.online](https://nujawak.online/blog/39/)


[Windows でショートカットキーからバッチファイルを起動する設定方法 : ごった煮ブログ](http://blog.livedoor.jp/takyuchan/archives/51445538.html)



## tKinter

- [【Python】メッセージボックスを表示する(tkinter.messagebox) | 鎖プログラム](https://pg-chain.com/python-messagebox)

- [tkinterを使用してPythonで「はい / いいえ（Yes / No)」メッセージボックスを作成する | Men of Letters（メン・オブ・レターズ） – 論理的思考/業務改善/プログラミング](https://laboratory.kazuuu.net/create-yes-no-messagebox-in-python-using-tkinter/)

- [Tkinterメッセージボックス利用時の空ウィンドウ削除方法 - Qiita](https://qiita.com/sunadandy/items/c298d192cd423190ccda)

- [ボタンを使って Tkinter ウィンドウを閉じる | Delft スタック](https://www.delftstack.com/ja/howto/python-tkinter/how-to-close-a-tkinter-window-with-a-button/)

[【Python】tkinter pack オブジェクトを配置する | 鎖プログラム](https://pg-chain.com/python-pack-grid-place)

[PythonのtkinterでGUIを作ってみる_その２ - Qiita](https://qiita.com/daisuke8000/items/70792eda27d3443cc63e)





[pythonで業務効率化／RPA自作 – 検討 その４ PyWin32 を試す。（１） | beginners Hub](https://se.yuttar-ixm.com/pywin32-test-1/)

Tool:

[PythonでWindowsアプリを操作する（２）／画面パーツ取得・値セット・メニュー選択 - "BOKU"のITな日常](https://arakan-pgm-ai.hatenablog.com/entry/2019/08/28/000000)

“C:\Program Files (x86)\Windows Kits\10\bin\10.0.18362.0\x86\inspect.exe”


## pywinauto
[pywinautoの使い方をはじめから - いろいろ足りない](https://harist.hatenablog.jp/entry/2020/03/22/154620)

### ウィンドウハンドルからファイルパスを取得
[生産がす: アクティブなウィンドウのハンドルからファイルパス取得](http://sumishiro.blogspot.com/2009/09/blog-post_30.html)


ウィンドウの閉じ方

[「取得したハンドルでウィンドウを閉じたいのですが。。」（1） Insider.NET － ＠IT](https://atmarkit.itmedia.co.jp/bbs/phpBB/viewtopic.php?topic=12906&forum=7)

実行ファイルのパスを取得

[python - PythonでプロセスIDから実行ファイルのパスを取得したい - スタック・オーバーフロー](https://ja.stackoverflow.com/questions/62265/python%E3%81%A7%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9id%E3%81%8B%E3%82%89%E5%AE%9F%E8%A1%8C%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E3%83%91%E3%82%B9%E3%82%92%E5%8F%96%E5%BE%97%E3%81%97%E3%81%9F%E3%81%84)

## inspect

> C:\Program Files (x86)\Windows Kits\10\bin\10.0.20348.0\x64
inspect.exe

## ウィンドウ位置の取得

[Pythonでウィンドウのタイトルから爆速で位置を取得【Windows】 - Qiita](https://qiita.com/ShortArrow/items/409f9695c458433d0744)
[【tkinter】 画面サイズ・位置の設定方法 - 基礎 【Python】 - 田舎社会人のいろいろ学習記](https://www.python-beginners.com/entry/20210515/1621007804)













