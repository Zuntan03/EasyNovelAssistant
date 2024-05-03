# EasyNovelAssistant

軽量で規制も検閲もない日本語ローカル LLM『[LightChatAssistant-TypeB](https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF)』による、簡単なノベル生成アシスタントです。  
ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。

内部で呼び出している [KoboldCpp](https://github.com/LostRuins/koboldcpp) や [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) を直接利用することもできますし、[EasySdxlWebUi](https://github.com/Zuntan03/EasySdxlWebUi) で画像を生成しながら利用することもできます。

## 利用者の声

- [EasyNovelAssistant と EasySdxlWebUi で、絵と文章と音声をローカル PC で同時生成](https://twitter.com/Zuntan03/status/1786165587573715394)
	- [@StelsRay](https://twitter.com/StelsRay/status/1786289235324207593),
	[@hysierra](https://twitter.com/hysierra/status/1786300104338731172),
	[@currnya](https://twitter.com/currnya/status/1786357838492946803),
	[984](https://bbs.punipuni.eu/test/read.cgi/vaporeon/1712647603/984)
- [EasyNovelAssistant の音声読み上げ対応](https://twitter.com/Zuntan03/status/1785252082343440723)
	- [@StelsRay](https://twitter.com/StelsRay/status/1785338281485553757)
	[@555zamagi](https://twitter.com/555zamagi/status/1785259670141374741),
	[879](https://mercury.bbspink.com/test/read.cgi/onatech/1702817339/879),
	[@kurayamimousou](https://twitter.com/kurayamimousou/status/1786379824187220016)

### 記事

- 『[【検閲なし】GPUで生成するローカルAIチャット環境と小説企画＋執筆用ゴールシークプロンプトで叡智小説生成最強に見える](https://note.com/kagami_kami/n/n3a321d926684)』[@kagami_kami_m](https://twitter.com/kagami_kami_m/status/1785313774620246194)
- 作例『[[AI試運転]スパーリング・ウィズ・ツクモドウ](https://note.com/liruk/n/nfd0bb54903cb)』と[制作の感想](https://twitter.com/liruk/status/1785596479631204420)。

### つぶやき

[@kurayamimousou](https://twitter.com/kurayamimousou/status/1786377248033136794),
[@boxheadroom](https://twitter.com/boxheadroom/status/1786031076617703640),
[@luta_ai](https://twitter.com/luta_ai/status/1785933828730802214),
[0026](https://mercury.bbspink.com/test/read.cgi/onatech/1714642045/26),
[@liruk](https://twitter.com/liruk/status/1785596479631204420),
[@kagami_kami_m](https://twitter.com/kagami_kami_m/status/1785805841410691320),
[@AonekoSS](https://twitter.com/AonekoSS/status/1785327191859122446),
[@maaibook](https://twitter.com/maaibook/status/1785540609627054413),
[@corpsmanWelt](https://twitter.com/corpsmanWelt/status/1785878852792901738),
[@kiyoshi_shin](https://twitter.com/kiyoshi_shin/status/1785363555132596593),
[@AINewsDev](https://twitter.com/AINewsDev/status/1784241585183658138),
[@kgmkm_inma_ai](https://twitter.com/kgmkm_inma_ai/status/1785149941448663443),
[@AonekoSS](https://twitter.com/AonekoSS/status/1784650868195024996),
[@StelsRay](https://twitter.com/StelsRay/status/1785338281485553757),
[@mikumiku_aloha](https://twitter.com/mikumiku_aloha/status/1785300629461799372), <!--  -->
[@kagami_kami_m](https://twitter.com/kagami_kami_m/status/1784446620916146273),
[@2ewsHQJgnvkGNPr](https://twitter.com/2ewsHQJgnvkGNPr/status/1784123670451130527),
[@ainiji981](https://twitter.com/ainiji981/status/1784140730094805215),
[@Neve_AI](https://twitter.com/Neve_AI/status/1784207868549542307),
[@WreckerAi](https://twitter.com/WreckerAi/status/1784245468798836773),
[@ai_1610](https://twitter.com/ai_1610/status/1784075370330992763),
[@kagami_kami_m](https://twitter.com/kagami_kami_m/status/1783113042576003282),
[@kohya_tech](https://twitter.com/kohya_tech/status/1782920101328732513),
[@kohya_tech](https://twitter.com/kohya_tech/status/1782563778993000538),
[@G13_Yuyang](https://twitter.com/G13_Yuyang/status/1782653077683855810),
[0611](https://mercury.bbspink.com/test/read.cgi/onatech/1694810015/611),
[0549](https://mercury.bbspink.com/test/read.cgi/onatech/1694810015/549)

## インストールと更新

インストールや更新で困ったことが起きたら、[こちら](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E6%9B%B4%E6%96%B0) を参照してください。  

1. [`Install-EasyNovelAssistant.bat`](https://github.com/Zuntan03/EasyNovelAssistant/raw/main/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat?v=2) を右クリックして `名前をつけて保存` し、インストール先フォルダ（**パスが英数字で空白を含まない**）にダウンロードして実行します。
	- **`WindowsによってPCが保護されました` と表示されたら、`詳細表示` から `実行` します。**
	- `配布元から関連ファイルをダウンロード` することに問題がなければ `y` を入力します。
	- `Windows セキュリティ` のネットワークへのアクセス許可は `許可` してください。
1. インストールが完了すると、自動的に EasyNovelAssistant が起動します。  

インストール完了後は
- `Run-EasyNovelAssistant.bat` で起動します。
- `Update-EasyNovelAssistant.bat` で更新します。

**次のステップは [はじめての生成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90) です。**


## 最近の更新情報

### 2024/05/04

- 急な開発で混み合ったり古くなったりしたドキュメントを整理しています。

### 2024/05/03

- LLM 入出力のコンテキストサイズの上限を `モデル` - `コンテキストサイズ上限` メニューで指定するようにしました。
	- デフォルト値は `4K` で、VRAM 8GB 環境で `LightChatAssistant-2x7B-IQ4_XS` の `L30` か `L33` が動作します。
	- 長い文章を取り扱いたい場合は、より大きなコンテキストサイズを指定します。  
	ただし GPU レイヤー数に応じて消費 VRAM が増えます。
- [mmnga/Vecteus-v1-gguf](https://huggingface.co/mmnga/Vecteus-v1-gguf), [mmnga/Ninja-v1-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-128k-gguf), [mmnga/Ninja-v1-NSFW-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-128k-gguf) の IQ4_XS 版をダウンロードできるようにしました。
- コンテキストウィンドウの仕様変更に備えて、`KoboldCpp/Run-*-L0.bat` を起動時に再生成するようにしました。
	- 当初から「[bat ファイルをコピーして、set GPU_LAYERS=0 あたりをお好みに変更してご利用ください。](https://github.com/Zuntan03/EasyNovelAssistant?tab=readme-ov-file#tips)」とは案内しておりましたが、失われて困る変更がありましたらコピーしてから更新してください。
- ファイルの保存時に上書きするファイルがある場合は、`log/` にバックアップするようにしました。
	- うっかり上書きしてしまったら `log/` を覗いてみてください。

### 2024/05/02

- `ファイル` メニューに `ファイル監視` を追加して、お好みのテキストエディタと連携できるようになりました。  
	あなたの手に馴染んだテキストエディタで入力を保存すると、EasyNovelAssistant が自動で読み込みます。  
	これもローカル LLM の利点ですね。  
	![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/file_watch.png)
- メニュー周りを整理しました。
	- `特集テーマ` メニューと `作例や記事` メニューを追加しました。
	- `モデル` メニューをカテゴリ分けしました。
	- `ツール` メニューを追加しました。
- 注意書きを追加しました。
	- AVX2 をサポートしていない CPU では、`koboldcpp_cublas.dll` の初期化に失敗します。
		- `KoboldCpp/koboldcpp.exe` で KoboldCpp を直接起動して、動作する起動オプションを探します。
			- 例）`Presets:` を `CLBlast NoAVX2(Old CPU)` にして、`GPU ID:` を NVIDIA 系にする。
		- KoboldCpp が起動している状態で `Run-EasyNovelAssistant.bat` で EasyNovelAssistant を起動すると、そのまま利用できます。
- Linux 版の KoboldCpp のバージョンを 1.64 に上げました。
	- ファイル名が `koboldcpp-linux-x64` から `koboldcpp-linux-x64-cuda1150` に変更されていますので更新してください。
- 「」の無い文章を読み上げなくなっていた不具合を修正しました。

### Vecteus や Ninja の使い方

![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/Ninja.png)

1. 自動で起動している `[元祖] LightChatAssistant-TypeB-2x7B-IQ4_XS` のコマンドプロンプトを閉じます。
1. `モデル` メニューから `Vecteus` や `Ninja` の `L0` を選びます。
	- `L0` の数値を上げれば上げるほど高速に動作しますが、VRAM が必要になります。
	- Vecteus IQ4_XS (コンテキストウィンドウ 4K) は VRAM 6GB でも全 33 レイヤーが載ります。
	- Ninja 128K はコンテキストウィンドウと GPU レイヤーで、VRAM をトレードオフすることになります。

Vecteus と Ninja の個人の感想

- Vecteus Q4_K のコスパが凄まじい。~~ぜひ IQ4_XS 版を触ってみたい。~~
	- Vecteus のコンテキスト広げた版にも期待。
- Ninja も 128K でない版を 4K コンテキストで動かしていると良好。
	- 128K 版ではコンテキスト 16K あたりから品質に悪影響があるような気がする？（LCA 32K 感覚比）
		- とりあえず 128K 版を 8K 運用。
- Ninja に Instruction format を適用すると、申し訳される？
- ~~Ninja の量子化が Q_8_0 までしか無い。IQ4_XS 版を触ってみたい。~~

### 2024/05/01

- モデルに [`Ninja-v1-NSFW-128k-Q_8_0`](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-NSFW-128k-GGUF), [`Ninja-v1-NSFW-Q_8_0`](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-NSFW-GGUF), [`Ninja-v1-128k-Q_8_0`](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-128k-GGUF), [`Ninja-v1-Q_8_0`](https://huggingface.co/Local-Novel-LLM-project/Ninja-v1-GGUF), [`Vecteus-v1-Q4_K`](https://huggingface.co/Local-Novel-LLM-project/Vecteus-v1-gguf), [`umiyuki-Japanese-Chat-Umievo-itr001-7b-Q4_K_M`](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) を追加しました。
- `テンプレート` メニューに `ゴールシーク: 小説企画からプロッティング` と `ゴールシーク: 生成した設定とプロットで執筆` を追加しました。
	- 使い方は『[【検閲なし】GPUで生成するローカルAIチャット環境と小説企画＋執筆用ゴールシークプロンプトで叡智小説生成最強に見える](https://note.com/kagami_kami/n/n3a321d926684)』を確認ください。
	- `ヘルプ` の `ゴールシーク` からも上記記事を確認できます。
- 読み上げ文章の抽出ロジックを変更しました。
	- より文脈に沿った読み上げになりますが、文末ノイズが乗る可能性があります。
		- 個別に対処しますので、文末ノイズが乗る文面がありましたら、連絡をください。

### 2024/04/30

[![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/StyleBertVits2.png)](https://twitter.com/Zuntan03/status/1785252082343440723)  
[動画 DL](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/StyleBertVits2.mp4)

- [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) による読み上げに対応しました。  
	- 中クリックによる手動読み上げと、`キャラ名「～」` セリフフォーマットによる生成時自動読み上げに対応しています。
	- `Style-Bert-VITS2/` フォルダ内は通常の Style-Bert-VITS2 として利用できます。
		- Style-Bert-VITS2 のチュートリアル: [YouTube](https://www.youtube.com/watch?v=aTUSzgDl1iY), [ニコニコ](https://www.nicovideo.jp/watch/sm43391524)
		- `Style-Bert-VITS2/Editor.bat` で、音程調整ありの音声生成ができます。
		- モデルの追加は `Style-Bert-VITS2/model_assets/` にフォルダを作ってモデルのファイルを配置します。
			- 例）`Style-Bert-VITS2/model_assets/` に [`tsukuyomi-chan/`](https://huggingface.co/ayousanz/tsukuyomi-chan-style-bert-vits2-model) フォルダを作成して、[`.safetensors`](https://huggingface.co/ayousanz/tsukuyomi-chan-style-bert-vits2-model/resolve/main/tsukuyomi-chan_e200_s5200.safetensors) と [`config.json`](https://huggingface.co/ayousanz/tsukuyomi-chan-style-bert-vits2-model/resolve/main/config.json) と [`style_vectors.npy`](https://huggingface.co/ayousanz/tsukuyomi-chan-style-bert-vits2-model/resolve/main/style_vectors.npy) を保存するとモデルを利用できます。
			- 他のモデル: [Anneli](https://booth.pm/ja/items/5511064), [Anneli-nsfw](https://booth.pm/ja/items/5511852)
		- `Style-Bert-VITS2/App.bat` でお手元の音声データからモデルを作成できます。
			- 音声の分割、読みの追加など学習に必要な機能が一通り揃っています。詳細は [公式ページ](https://github.com/litagin02/Style-Bert-VITS2#%E5%AD%A6%E7%BF%92) を参照ください。

#### 読み上げ利用手順

1. EasyNovelAssistant を起動したら、[`読み上げ`] - [`Style-Bert-VITS2 をインストール"`] でインストールの完了を待ちます。
1. インストールが完了したら [`読み上げ`] - [`読み上げサーバーを立ち上げる`] で読み上げサーバーの起動を待ちます。
	- `Style-Bert-VITS2 読み上げサーバー` に `00-00 00:00:00 |  INFO  | server_fastapi.py:306 | server listen: http://127.0.0.1:5000` が表示されたら起動完了です。
	- **LLM(KoboldCpp) で VRAM ギリギリまで GPU レイヤーを増やしていた場合は、VRAM を 2GB 程度開けるために GPU レイヤーを 5 枚程度(Run-LightChatAssistant-2x7B-IQ4_XS 換算) 減らしてください。**
	- **VRAM が 6GB 未満の場合は [`読み上げ`] - [`GPU を使用する`] を無効にします。**
	- KoboldCpp と同様に `Style-Bert-VITS2/Server.bat` や `Style-Bert-VITS2/ServerCpu.bat` で、あらかじめ読み上げサーバーを立ち上げておくこともできます。
1. 読み上げサーバーが起動したら、[`読み上げ`] メニューで読み上げの有効/無効、音量、スピード、声の選択ができます。
1. 中クリックで読み上げたり、[`読み上げサンプル`] メニューを参考に生成時に自動で読み上げたりできます。
	- **重要！ [`設定`] メニューで名前を設定するのを忘れないでください！**

**[過去の更新履歴](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E6%9B%B4%E6%96%B0%E5%B1%A5%E6%AD%B4)**

## ドキュメント

### EasyNovelAssistant

- [インストールと更新](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E6%9B%B4%E6%96%B0)
	- インストールと更新の詳細説明とトラブルシューティングです。
- [はじめての生成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90)
	- EasyNovelAssistant のチュートリアルです。
- [Tips](https://github.com/Zuntan03/EasyNovelAssistant/wiki/Tips)
	- ちょっとした情報です。
- [更新履歴](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E6%9B%B4%E6%96%B0%E5%B1%A5%E6%AD%B4)
	- 過去の更新履歴です。

## ライセンス

このリポジトリの内容は以下を除き [MIT License](./LICENSE.txt) です。

- インストール時に [ダウンロードするモノの一覧](https://github.com/Zuntan03/EasyNovelAssistant/blob/48350f45c838e4cda4f2a977c446e1f4141c858f/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat#L31) を表示します。
- `EasyNovelAssistant/setup/res/tkinter-PythonSoftwareFoundationLicense.zip` は Python Software Foundation License です。
- [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) がダウンロードする [JVNV](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvnv_corpus) 派生物は [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) です。
