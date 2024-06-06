import sys
import markdown

def main():
    """
    メイン関数。コマンドライン引数を解析し、適切な処理を呼び出します。
    """

    # 引数の数の確認
    if len(sys.argv) != 4:
        print('書き方: python3 script.py markdown <inputfile> <outputfile>')
        sys.exit(1)

    # 引数を取得
    command = sys.argv[1]
    inputfile = sys.argv[2]   # マークダウン形式のファイル
    outputfile = sys.argv[3]   # HTMLに変換し出力するファイル

    # コマンド引数がmarkdownのときに変換処理する
    if command == 'markdown':
        converter(inputfile, outputfile)
    else:
         print("コマンドがmarkdownではありません。")
         sys.exit(1)

def converter (inputfile, outputfile):
        """
        markdownファイルをHTMLに変換し、指定されたファイルに出力します。
        """
        try:
            # ファイルを開く
            with open(inputfile, 'r', encoding = "utf-8") as f:
                contents = f.read()

            # マークダウンをhtmlに変換する
            html = markdown.markdown(contents)

            # 変換したファイルを書き込む
            with open(outputfile, 'w', encoding = "utf-8") as f:
                f.write(html)
            
            print(f'{inputfile}をHTMLに変換して{outputfile}に保存しました。')

        except FileNotFoundError:
            print(f'Error: {inputfile}がありません。')
            sys.exit(1)
            
        except IOError as e:
            print(f'Error: ファイルの読み書き中にエラーが発生しました。{e}')
            sys.exit(1)

if __name__ == "__main__":
    main()

