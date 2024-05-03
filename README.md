# EasyNovelAssistant

軽量で規制も検閲もない日本語ローカル LLM『[LightChatAssistant-TypeB](https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF)』による、簡単なノベル生成アシスタントです。  
ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。

内部で呼び出している [KoboldCpp](https://github.com/LostRuins/koboldcpp) や [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) を直接利用することもできますし、[EasySdxlWebUi](https://github.com/Zuntan03/EasySdxlWebUi) で画像を生成しながら利用することもできます。

## 利用者の声

- [絵と文章と音声をローカル PC で同時生成](https://twitter.com/Zuntan03/status/1786165587573715394)
	- [@StelsRay](https://twitter.com/StelsRay/status/1786289235324207593),
	[@hysierra](https://twitter.com/hysierra/status/1786300104338731172),
	[@currnya](https://twitter.com/currnya/status/1786357838492946803),
	[984](https://bbs.punipuni.eu/test/read.cgi/vaporeon/1712647603/984)
- [音声読み上げ対応](https://twitter.com/Zuntan03/status/1785252082343440723)
	- [@StelsRay](https://twitter.com/StelsRay/status/1785338281485553757)
	[@555zamagi](https://twitter.com/555zamagi/status/1785259670141374741),
	[879](https://mercury.bbspink.com/test/read.cgi/onatech/1702817339/879)


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

## 最近の更新情報

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

## 動作環境

- 最近の NVIDIA ビデオカードを積んだ Windows PC で動作します。
	- 動作確認はできていませんが、Linux 版もあります。
- 動作確認環境: Windows 11, RAM 64GB, Geforce 3060 12GB
	- RAM 16GB, VRAM 4GB 程度でも、`7B-Q3` などの小さなモデルなら動作します。

RAM 16GB, Geforce GTX 1660 Ti (VRAM 3.3GB / 6.0GB), Ryzen 5 3600X で `3.5 tokens/sec (T/s)` です。  
Geforce RTX 3060 12GB なら `13.5 T/s` です。

![](./img/Gtx1660Ti.png)

## インストールと更新

問題が発生したら [インストールのトラブルシューティング](#インストールのトラブルシューティング) を確認してください。  

1. [`Install-EasyNovelAssistant.bat`](https://github.com/Zuntan03/EasyNovelAssistant/raw/main/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat?v=2) を右クリックからダウンロードして、**パスが英数字のインストール先フォルダ** でダブルクリックして実行します。
	- **`WindowsによってPCが保護されました` と表示されたら、`詳細表示` から `実行` します。**
		- 注意書きに問題がなければ `y` を入力します。
	- `Windows セキュリティ` のネットワークへのアクセス許可は `キャンセル` でも動作します。
1. インストールが終了すると、自動的に EasyNovelAssistant が起動します。  
	- 次回以降は `Run-EasyNovelAssistant.bat` で起動します。

更新は `Update-EasyNovelAssistant.bat` を実行します。

[Linux 版（moc67331 さん作）](https://github.com/Zuntan03/EasyNovelAssistant/issues/1) の [`Install-EasyNovelAssistant.sh`](https://github.com/Zuntan03/EasyNovelAssistant/raw/main/EasyNovelAssistant/setup/Install-EasyNovelAssistant.sh?v=0) も同様に、インストール先フォルダで実行してインストールします。  
動作確認をしてませんので、動かなかったらパッチをください。
読み上げはインストール先に [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) をインストールして、`EasyNovelAssistant/setup/res/config.yml` を `Style-Bert-VITS2/` にコピーすれば動作するかもです。

### はじめての生成

![](./img/init.png)

1. メニューの [`生成`] - [生成の開始/終了] で、左の入力欄の続きの文章が右下の生成欄に生成されます。  
	- 生成が終わると生成結果が右上の出力欄に追加されて、同じ条件で生成を続けます。
1. 右上の欄に気に入った続きの文章があれば、範囲選択して中クリックで入力欄に転送します。
	- 次からは更新された入力欄の続きを生成します。  
	**`F5` で生成を中断して、すぐに新しい条件での生成を開始できます。**

## [！重要！] モデルと GPU レイヤー数の選択

- **初期設定は VRAM 4GB でも動作するモデルと GPU レイヤー数なので、動作がとても遅くなっています。**
	- GPU レイヤーはモデルを数十層に分けて、何層分を高速な VRAM に置くかを指定する値です。  
	モデルの全層を VRAM に置くと、動作が数倍速くなります。
	- モデルのサイズが大きいと推論がより高度になりますが、動作速度が遅くなり、 総 GPU レイヤー数も増えます。
- **GPU の VRAM 容量にあったモデルと GPU レイヤー数を設定することで、より高度なモデルが数倍高速に動作します。**

### VRAM 利用状況の確認

![](./img/task.png)

1. Windows のタスクバーを右クリックして、`タスクマネージャー` を起動します。
1. `パフォーマンス` タブで `NVIDIA Geforce` の GPU を選択します。
1. `専用 GPU メモリ` の `VRAM 使用量 / VRAM 容量` を確認します。
	- **VRAM 残量 (容量 - 使用量) が 1GB を切るぐらいのモデルと GPU レイヤー数を設定するのが目的です。**
1. 新しいモデルサーバーを立ち上げるために、立ち上げ済みのモデルサーバーを閉じます。  
	![](./img/server.png)

### モデルと GPU レイヤーの設定例

メニューの [`モデル`] から、モデルと GPU レイヤー数 `L(数値)` を選びます。  
**VRAM に収まらない場合は以下のようなメッセージが表示されますので、より小さいモデルや低い GPU レイヤー数を指定してください。**
```
Could not load text model: \EasyNovelAssistant\KoboldCpp\LightChatAssistant-TypeB-2x7B_iq4xs_imatrix.gguf
続行するには何かキーを押してください . . .
```
**また、動作はするが明らかに遅い（1~2秒に 1文字しか出力されない、など）場合も、GPU レイヤー数を減らしてみてください。**  

> **速度の参考値**  
> RAM 16GB, Geforce GTX 1660 Ti (VRAM 3.3GB / 6.0GB), Ryzen 5 3600X で `3.5 tokens/sec (T/s)` です。  
> Geforce RTX 3060 12GB なら `13.5 T/s` です。

- **VRAM 4GB は初期設定の `LightChatAssistant-TypeB-2x7B-IQ4_XS` の `L1` で、もし動作しなければ `L0` を選びます。**
	- 動作が重い場合はより小さな `SniffyOtter-7B-Novel-Writing-NSFW-IQ4_XS` も選択肢です。  
	メニューの [`テンプレート`] - [`SniffyOtter-7B-Novel-Writing-NSFW`] で [プロンプトフォーマット](https://huggingface.co/Aratako/SniffyOtter-7B-Novel-Writing-NSFW#%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88) に沿ってご利用ください。
- **VRAM 8GB は `LightChatAssistant-TypeB-2x7B-IQ4_XS` の `L10` ~ `L14` を選びます。**
- **VRAM 12GB は `LightChatAssistant-TypeB-2x7B-IQ4_XS` の `L20` ~ `L25` を選びます。**
	- 設定を詰めた手元の Geforce 3600 12GB 環境では、後述の bat で `L27` にしています。
		- 画面表示や[アプリ描画](https://www.gigafree.net/Windows/set-gpu-per-app/)を、オンボード GPU に任せて VRAM を空けます。
		- `Win + Ctrl + Shift + B` でグラフィックスドライバをリセットできます（おまじない）。
- **VRAM 16GB 以上は `LightChatAssistant-TypeB-2x7B-IQ4_XS` の `L33` や、より大きな `LightChatAssistant-4x7B-IQ4_XS` で可能な範囲のレイヤー数を指定します。**
	- 量子化レベルは `IQ4_XS` が今の安牌っぽいです。
	- より規模の大きいモデルを選ぶよりも、すべての GPU レイヤーを VRAM に載せたほうが満足度が高くなりがちです。

GPU レイヤーを `L0` などで利用すると、[EasySdxlWebUi](https://github.com/Zuntan03/EasySdxlWebUi) の forge による画像生成と同時に利用できます。  
文章と画像の生成待ち時間を、交互に生成物を確認することで解消できます。  
生成文章の状況に合わせた画像生成用のプロンプト生成も、探りがいのある分野です。

RAM 64GB, VRAM 12GB 以上の環境で巨大な CommandR 系のモデルを `L4` など立ち上げ、寝る前や外出前に仕込んでおくのもアリです。  
が、放置する価値のあるプロンプトかを確認しておかないと、起きたときや帰ったときにがっかりすることになります。  

RAM 64GB だと超カツカツですが、[CommandR+ の `IQ4_XS` が `L4` で動いた実績](https://twitter.com/Zuntan03/status/1778441181741158764) があります（が、64GB ではカツカツすぎて色々工夫が必要です）。

## サンプルについて

- **サンプルはそのまま生成するだけでなく、自分好みに書き換えてください。**
	- まずは `設定` メニューで名前を変更したり、キャラの特徴を書き換えたり・書き加えたりしてみましょう。
	- 心に響く文章が生成されたら、出力欄の該当文章を範囲選択して中クリックで入力欄に付け足して続きを生成します。
		- 想定と異なるストーリーが生成された場合は、想定するストーリーの出だしまでを入力欄に記載します。
- サンプルの内容によっては、[`生成`] - [`生成文の長さ`] を [`4096`] などと長く設定したほうが合う場合があります。
- サンプルは `LightChatAssistant-TypeB-2x7B-IQ4_XS` で動作を確認しています。
	- 他のモデルでは入力欄右クリックメニューの `指示タグの挿入` などが必要になる場合があります。
	- **EasyNovelAssistant は自動的に指示タグを挿入していません。**
- EasyNovelAssistant は起動時にサンプルを更新しますので、いつの間にかサンプルが増えている可能性があります。
- サンプルはネット上の記事などのプロンプトを元に微調整したものです。  
	- 『[最新AI Claude 3で長編小説執筆支援【GPT-4を超えた⁉︎】](https://kakuyomu.jp/works/16818093074043995181)』 [まとめ](https://kakuyomu.jp/works/16818093074043995181/episodes/16818093074305285059)
	- 『[5ch プロンプトまとめ](https://rentry.org/gpt0721)』

## TIPS

- 速度優先のモデルでGenerate Foreverをして、SSR が来たら採用する考え方の UI です。
	- アホな文章が生成されはじめたら、`F5` ですぐに次の生成に移れます。
	- 生成結果には番号を振ってありますので、「～なものの番号を5つ挙げて、理由も添えて」とより賢い LLM に頼むこともできます（出力のログは `log/` にあります）。
- EasyNovelAssistant は `KoboldCpp/` にモデルを `L0` で立ち上げる bat ファイルを生成します。
	- この bat ファイルでモデルサーバーを起動すると、`LightChatAssistant` の起動時に自動的に接続し、終了時にモデルサーバーを終了しません。
	- bat ファイルをコピーして、`set GPU_LAYERS=0` あたりをお好みに変更してご利用ください。
- モデルサーバー起動中に [`http://localhost:5001`](http://localhost:5001) を開くと、[EasyLightChatAssistant](https://github.com/Zuntan03/EasyLightChatAssistant) のように KoboldCpp の Web UI を利用できます。
- モデルを追加するには `EasyNovelAssistant/setup/res/default_llm.json` を参考にしつつ、`llm.json` にモデルを追加します。
- 指示タグを追加するには `EasyNovelAssistant/setup/res/default_llm_sequence.json` を参考にしつつ、`llm_sequence.json` にモデルを追加します。
	- 辞書のキーがモデルファイル名に含まれていると、その指示タグが使用されます。

## トラブルシューティング

### インストールのトラブルシューティング

- 英数字のみで空白を含まないパスにインストールします。
- PC の管理者権限がないとインストールに失敗することがあります。
- ウィルスチェックソフトのアバストが有効だとインストールに失敗します。
- グラフィックスドライバが古いと、起動に失敗することがあります。
	- ドライバを更新したら `NVIDIA コントロールパネル` の `3D 設定の管理` で、`CUDA - システム メモリ フォールバック ポリシー` を `システム メモリ フォルバックなしを優先` にします。
- AVX2 をサポートしていない CPU では、`koboldcpp_cublas.dll` の初期化に失敗します。
	- `KoboldCpp/koboldcpp.exe` で KoboldCpp を直接起動して、動作する起動オプションを探します。
		- 例）`Presets:` を `CLBlast NoAVX2(Old CPU)` にして、`GPU ID:` を NVIDIA 系にする。
	- KoboldCpp が起動している状態で `Run-EasyNovelAssistant.bat` で EasyNovelAssistant を起動すると、そのまま利用できます。

## ドキュメント

- [更新履歴](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E6%9B%B4%E6%96%B0%E5%B1%A5%E6%AD%B4)
	- 過去の更新履歴です。

## ライセンス

このリポジトリの内容は以下を除き [MIT License](./LICENSE.txt) です。

- インストール時に [ダウンロードするモノの一覧](https://github.com/Zuntan03/EasyNovelAssistant/blob/48350f45c838e4cda4f2a977c446e1f4141c858f/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat#L31) を表示します。
- `EasyNovelAssistant/setup/res/tkinter-PythonSoftwareFoundationLicense.zip` は Python Software Foundation License です。
- [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) がダウンロードする [JVNV](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvnv_corpus) 派生物は [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) です。
