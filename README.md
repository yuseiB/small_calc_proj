# small_calc_proj

## RF signal evaluation sample

`rf_signal_eval` フォルダに、減衰するRF信号をreference信号でミキシングしてダウンコンバートし、I/Qから位相差を確認するサンプルを追加しています。

- Python script: `rf_signal_eval/signal_eval.py`
- Notebook: `rf_signal_eval/rf_downconversion_demo.ipynb`

実行例:

```bash
python rf_signal_eval/signal_eval.py
```

## WSL Ubuntu (shell: fish) での実行手順

```fish
# リポジトリルートへ移動
cd /path/to/small_calc_proj

# 既存仮想環境が壊れている/古い場合は削除して作り直す
rm -rf .venv
python3 -m venv .venv

# fish 用の activate スクリプトを使う
source .venv/bin/activate.fish

# pip が無い場合の復旧
python -m ensurepip --upgrade

# 依存パッケージをインストール
python -m pip install --upgrade pip
python -m pip install numpy

# 実行
python rf_signal_eval/signal_eval.py
```
