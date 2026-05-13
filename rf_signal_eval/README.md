# RF signal evaluation

減衰するRF信号をreference信号でミキシングし、I/Qベースバンドから位相差を推定する簡易サンプルです。

## Files

- `signal_eval.py`: 信号生成、ダウンコンバート、位相推定ロジック
- `rf_downconversion_demo.ipynb`: 実験しながら確認するNotebook

## Quick start

```bash
python rf_signal_eval/signal_eval.py
```

Notebookを使う場合は以下を実行してから開いてください。

```bash
pip install numpy matplotlib jupyter
jupyter notebook rf_signal_eval/rf_downconversion_demo.ipynb
```
