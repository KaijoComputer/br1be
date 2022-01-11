# br1be 
## 概要

macOS ゲートキーパー回避スクリプト
署名がないアプリや壊れているアプリ、信頼されていないアプリを管理者、SIP有効環境で実行できるようにします

## 前提

- Python 3

## 実行

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
