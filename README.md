English version: [README_en.md](README_en.md)

# Tang Primer 25K 用 FT601 + MIPIコネクタ オリジナルベース基板

## 概要

Sipeed社の [Tang Primer 25K](https://wiki.sipeed.com/hardware/en/tang/tang-primer-25k/primer-25k.html) に搭載されている GW5A-LV25MG121 には MIPI D-PHY インターフェースが搭載されており、SoM までは配線が来ているようですが、残念ながら標準の Dock base board ではこのラインが未接続のままになっており、利用することができません。

本プロジェクトでは、MIPI D-PHY ラインを活用できるように 0.5mm ピッチ 22pin のコネクタに引き出したうえで、画像データなどを PC と交換できるように FT601 で USB3.0 接続できるオリジナルベース基板の設計データを提供します。


## 回路図

回路図は以下です。

- [rtcl-tp25k-usb3_v1.pdf](rtcl-tp25k-usb3_v1.pdf)


## KiCAD 設計データ


rtcl-tp25k-usb3 ディレクトリ以下に KiCAD 6.0 で設計したデータを格納しています。


## 免責事項

本設計データは、研究開発用の試作実験に供するものであり、利用に際して発生した如何なる損害も作者は補償いたしませんので予めご了承ください。


## ライセンス(License)

本設計データは、[クリエイティブ・コモンズ 表示-非営利 4.0 国際 ライセンス](https://creativecommons.org/licenses/by-nc/4.0/deed.ja)の下で提供されています。

製造した本基板の無断での販売や配布を行わない限りは、趣味や研究開発用途でご自由にお使いいただく事が出来ます。

また、商用に製造販売を希望される場合は、別途ライセンス契約を作者までご相談ください。[お問い合わせフォーム](https://rtc-lab.com/contact/)などからお問い合わせ頂けます。


## 作者情報

渕上 竜司(Ryuji Fuchikami)
[リアルタイムコンピューティング研究所](https://rtc-lab.com/)
