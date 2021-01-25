import os

def listup(path, depth=0):
    # ディレクトリの中に入っていることが分かるようにインデントする
    indent = ' ' * depth
    print(indent + 'Now in {}' .format(path))

    # ディレクトリ内のエントリ（ディレクトリ or ファイル）を処理
    for entry in os.listdir(path):
        # entryはベース名のみなのでjoinでパスにする
        fullpath = os.path.join(path, entry)

        if os.path.isdir(fullpath):
            # ディレクトリの場合、自分自身を呼び出す
            # 探索が深くなっていることが分かるようにdepthに 1を足す
            listup(fullpath, depth + 1)

        else:
            #ファイルの場合は表示のみ
            print(indent + 'Found {}'.format(fullpath))

    # ひとつのディレクトリの処理が終わったことがわかるように表示
    print(indent + 'Leave {}'.format(path))

listup('.')