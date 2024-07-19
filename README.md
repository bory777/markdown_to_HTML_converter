# Markdown to HTML Converter

Markdown to HTML Converterは、MarkdownファイルをHTMLファイルに変換するPythonスクリプトです。コマンドライン引数としてMarkdownファイルとHTMLファイルのパスを指定し、Markdownの内容をHTMLに変換して指定されたHTMLファイルに書き込みます。

## 必要条件

- Python 3.x
- `markdown`ライブラリ

## インストール

1. Python 3.xをインストールします。
2. 必要なライブラリをインストールします。

```bash
pip install markdown
```

## 使用方法

コマンドラインで以下のようにスクリプトを実行します。

```bash
python3 script.py markdown <inputfile> <outputfile>
```

- `<inputfile>`: 変換するMarkdownファイルのパス
- `<outputfile>`: 出力先のHTMLファイルのパス

例：

```bash
python3 script.py markdown example.md example.html
```

### 注意事項

- 入力ファイルはMarkdown形式のファイルである必要があります。
- 出力ファイルはHTML形式のファイルである必要があります。
- 指定されたHTMLファイルが既に存在する場合、その内容は上書きされます。

## スクリプトの説明

### `main`関数

コマンドライン引数を解析し、適切な処理を呼び出します。

- 引数の数を確認し、不正な場合はエラーメッセージを表示して終了します。
- コマンドが`markdown`であることを確認し、Markdownファイルの変換処理を呼び出します。

### `converter`関数

MarkdownファイルをHTMLに変換し、指定されたファイルに出力します。

- 入力ファイルを開いて内容を読み込みます。ファイルが存在しない場合や読み込み中にエラーが発生した場合、エラーメッセージを表示して終了します。
- Markdownの内容をHTMLに変換します。
- 変換したHTMLを出力ファイルに書き込みます。書き込み中にエラーが発生した場合、エラーメッセージを表示して終了します。

## 例外処理

スクリプトは、以下のエラーに対するハンドリングを行います：
- ファイルが存在しない場合（`FileNotFoundError`）
- ファイルの読み込み中に発生する一般的な入出力エラー（`IOError`）
- ファイルの書き込み中に発生する一般的な入出力エラー（`IOError`）
