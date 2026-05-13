# RF signal evaluation

減衰するRF信号をreference信号でミキシングし、I/Qベースバンドから位相差を推定する簡易サンプルです。

## Files

- `signal_eval.py`: 信号生成、ダウンコンバート、位相推定ロジック
- `rf_downconversion_demo.ipynb`: 基本的なダウンコンバートを確認するシンプルなNotebook
- `rf_bam_signal_chain.ipynb`: **包括的な学習Notebook** – BAM向け信号処理の全ブロックを解説

## `rf_bam_signal_chain.ipynb` の内容

加速器のビーム到達モニター (BAM) の信号処理チェーンを、以下のセクションに沿って数値計算で学べます。

| セクション | 内容 |
|-----------|------|
| 0 | インポート & グローバル設定 |
| 1 | ベースライン: 減衰RF信号とIQ位相推定 |
| 2 | バンドパスフィルタ (BW vs. リンギング) |
| 3 | RFミキサ (差周波数・和周波数) |
| 4 | IQデモジュレーション (全位相範囲でのスイープ) |
| 5 | 局部発振器 (LO) の効果 – 位相雑音・周波数オフセット |
| 6 | PLL 動作 – ロック収束・追従・残留位相誤差 |
| 7 | ADCサンプリング – エイリアシング・量子化雑音・ジッタ |
| 8 | デジタル位相検出 – アンラップ・窓平均・SNR改善 |
| 9 | タイミングスキャンによるキャリブレーション |
| 10 | エンドツーエンドBAM様チェーン |
| 11 | 最終バリデーション – タイミング分解能と動作レンジ |

## Quick start

```bash
pip install numpy scipy matplotlib jupyter
```

シンプルなスクリプト実行:

```bash
python rf_signal_eval/signal_eval.py
```

包括的な学習Notebookを開く:

```bash
jupyter notebook rf_signal_eval/rf_bam_signal_chain.ipynb
```

基本デモNotebook:

```bash
jupyter notebook rf_signal_eval/rf_downconversion_demo.ipynb
```
