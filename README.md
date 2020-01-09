# NLP

文章やテキストの分類を行うプログラムです。ソースコードは以下のサイトを参考にさせていただきました。

ディープラーニングで文章・テキスト分類を自動化する方法　URL:https://spjai.com/category-classification/

使用した言語はPython3.xです。

普通に実行すると結果が一瞬表示されてすぐ消えてしまうので、pythonコマンドやIDE等から実行した方が分かりやすいと思います。

コード中で形態素解析を行うため、ライブラリとしてMeCabを使用しています。

本プログラムを実行する際、MeCabを導入されていない方は以下のサイトから導入して下さい。

https://taku910.github.io/mecab/#download

また、「main.py」と「nlp_tasks.py」の実行にはMeCabに加えて「numpy」、「scikit-learn」、「pandas」ライブラリが必要です。
導入されていない方は別途導入してください。

## ＜内容＞

- MeCabSample1.py：MeCabを利用してtextの文字列内にweather_set内の単語と一致する単語が存在した場合、その単語を出力するサンプルです。

- TextClassify_Simple.py：textのカテゴリが「天気」と「ナビゲーション」のどちらに属するかを判定するサンプルです。

- main.py、nlp_tasks.py：「livedoorニュースコーパス」を利用してニュース記事のカテゴリ分類を行うサンプルです。プログラムをGitHubに上げる前にデータセット内に含まれていたニュース記事で検証し、正しく分類できることを確認しました。実行の時はclassifier = MyMLPClassifier()とclassifier.cross_validation('corpus.csv')をコメントアウトし、#predict()のコメントを外してください。

「livedoorニュースコーパス」のURL：http://www.rondhuit.com/download.html#ldcc

- modelsフォルダ：学習の結果生成された予測モデルが入っているフォルダです。

## ＜「livedoorニュースコーパス」について＞

「livedoorニュースコーパス」の各記事ファイルにはクリエイティブ・コモンズライセンス「表示 – 改変禁止」が適応されています。

クリエイティブ・コモンズライセンス「表示 – 改変禁止」の詳細につきましては以下のサイトをご覧ください。

URL：https://creativecommons.org/licenses/by-nd/2.1/jp/

各記事内容の提供元は以下の通りです。

- 独女通信 URL：http://news.livedoor.com/category/vender/90/

- ITライフハック URL：http://news.livedoor.com/category/vender/223/

- 家電チャンネル URL：http://news.livedoor.com/category/vender/kadench/

- livedoor HOMME URL：http://news.livedoor.com/category/vender/homme/

- MOVIE ENTER URL：http://news.livedoor.com/category/vender/movie_enter/

- Peachy URL：http://news.livedoor.com/category/vender/ldgirls/

- エスマックス URL：http://news.livedoor.com/category/vender/smax/

- Sports Watch URL：http://news.livedoor.com/category/vender/208/

- トピックニュース URL：http://news.livedoor.com/category/vender/news/
