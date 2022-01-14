# br1be 
## 概要

macOS ゲートキーパー回避スクリプト
署名がないアプリや壊れているアプリ、信頼されていないアプリを管理者、SIP有効環境で実行できるようにします

## Shell版

### 前提

- なし

### 実行

`YourApp` というアプリに対して実行したい場合

```bash
./br1be.sh YourApp
```


## Python版

### 前提

- Python 3

### 実行

プロジェクトルートにて

```bash
python main.py YourApp
```

のように実行。

例)
```bash
python main.py ~/Downloads/Chromium.app
```
正常に終了すると、`YourApp`で指定した実行ファイルやアプリは実行できるようになります。

## 原理

macOSのGatekeeperはファイルやフォルダの `com.apple.quarantine` 属性を見て署名が**無効でないか**をチェックしている。
なので、`xattr` コマンドを利用して対象の `com.apple.quarantine` 属性を削除することでこのチェックを回避できる。
個人的にはこれはもはやセキュリティ上の欠陥なのではと思っているが、Wineが公式でこの方法を解説してたので仕様なんだと思い込むようにしている。
