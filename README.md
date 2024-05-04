# EasyNovelAssistant

軽量で規制も検閲もない日本語ローカル LLM『[LightChatAssistant-TypeB](https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF)』による、簡単なノベル生成アシスタントです。  
ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。

内部で呼び出している [KoboldCpp](https://github.com/LostRuins/koboldcpp) や [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) を直接利用することもできますし、[EasySdxlWebUi](https://github.com/Zuntan03/EasySdxlWebUi) で画像を生成しながら利用することもできます。

## 利用者の声

- (New!) [読み上げ音声に画像を割り当てて、字幕付きの動画の簡単作成に対応](https://twitter.com/Zuntan03/status/1786694765997924371)
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
- 作例『[[AI試運転]スパーリング・ウィズ・ツクモドウ](https://note.com/liruk/n/nfd0bb54903cb)』と [制作の感想](https://twitter.com/liruk/status/1785596479631204420)。

### つぶやき

[186](https://fate.5ch.net/test/read.cgi/liveuranus/1714702930/186),
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

1. [`Install-EasyNovelAssistant.bat`](https://github.com/Zuntan03/EasyNovelAssistant/raw/main/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat?v=2) を右クリックして `名前をつけて保存` で、インストール先フォルダ（**英数字のパスで空白を含まない**）にダウンロードして実行します。
	- **`WindowsによってPCが保護されました` と表示されたら、`詳細表示` から `実行` します。**
	- `配布元から関連ファイルをダウンロード` することに問題がなければ `y` を入力します。
	- `Windows セキュリティ` のネットワークへのアクセス許可は `許可` してください。
1. インストールが完了すると、自動的に EasyNovelAssistant が起動します。  

インストール完了後は
- `Run-EasyNovelAssistant.bat` で起動します。
- `Update-EasyNovelAssistant.bat` で更新します。

**次のステップは [はじめての生成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90) です。**


## 最近の更新情報

#### [動画の作成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E5%8B%95%E7%94%BB%E3%81%AE%E4%BD%9C%E6%88%90) に対応しました。

読み上げ音声に画像を割り当てて、字幕付きの動画の簡単作成に対応。以下作成手順。

1. [読み上げたい音声](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90#%E8%AA%AD%E3%81%BF%E4%B8%8A%E3%81%92%E3%81%AE%E5%88%A9%E7%94%A8) と [音声に割り当てたい画像](https://github.com/Zuntan03/EasySdxlWebUi) を用意します。
1. `ツール` の `動画の作成` で音声と動画のペアを再生順に合わせて選択します。
	- `キャンセル` すると次に進みます。
1. 動画の保存先を指定します。

- 動画ファイルと同じ名前のフォルダに、再生成用の `.bat` ファイルと字幕用の `.srt` ファイルがあります。
	- **字幕が動画の横幅に収まらない場合は `.srt` ファイルで字幕を改行し、 `.bat` ファイルで再生成してください。**
	- `*.bat` ファイルを編集して [FFmpeg](https://ffmpeg.org/) の詳細なオプションを指定することもできます。

### 2024/05/04

- [動画の作成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E5%8B%95%E7%94%BB%E3%81%AE%E4%BD%9C%E6%88%90) に対応しました。
	- 読み上げ音声に画像を割り当てて、字幕付きの動画を簡単に作成します。
- 急な開発で混み合ったり古くなったりしたドキュメントを整理しました。
	- 最初のインストールから音声読み上げまでがスムーズになったはずです。
	- 詰まる記述がありましたら、お知らせください。
- 読み上げ間隔を設定できるようにしました。

### 2024/05/03

- LLM 入出力のコンテキストサイズの上限を `モデル` - `コンテキストサイズ上限` メニューで指定するようにしました。
	- デフォルト値は `4K` で、VRAM 8GB 環境で `LightChatAssistant-2x7B-IQ4_XS` の `L30` か `L33` が動作します。
	- 長い文章を取り扱いたい場合は、より大きなコンテキストサイズを指定します。  
	ただし GPU レイヤー数に応じて消費 VRAM が増えます。
- [mmnga/Vecteus-v1-gguf](https://huggingface.co/mmnga/Vecteus-v1-gguf), [mmnga/Ninja-v1-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-128k-gguf), [mmnga/Ninja-v1-NSFW-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-128k-gguf) の IQ4_XS 版をダウンロードできるようにしました。
- コンテキストウィンドウの仕様変更に備えて、`KoboldCpp/Run-*-L0.bat` を起動時に再生成するようにしました。
	- 当初より「bat ファイルをコピーして、set GPU_LAYERS=0 あたりをお好みに変更してご利用ください。」と案内しておりましたが、失われて困る変更がありましたらコピーしてから更新してください。
- ファイルの保存時に上書きするファイルがある場合は、`log/` にバックアップするようにしました。
	- うっかり上書きしてしまったら `log/` を覗いてみてください。

**[過去の更新履歴](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E6%9B%B4%E6%96%B0%E5%B1%A5%E6%AD%B4)**

## ドキュメント

### EasyNovelAssistant

- [インストールと更新](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E6%9B%B4%E6%96%B0)
	- インストールと更新の詳細説明とトラブルシューティングです。
- [はじめての生成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90)
	- EasyNovelAssistant のチュートリアルです。
- [モデルと GPU レイヤー数の選択](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%A8-GPU-%E3%83%AC%E3%82%A4%E3%83%A4%E3%83%BC%E6%95%B0%E3%81%AE%E9%81%B8%E6%8A%9E)
	- 多様なモデルを効率的に利用する方法です。
- [Tips](https://github.com/Zuntan03/EasyNovelAssistant/wiki/Tips)
	- ちょっとした情報です。
- [動画の作成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E5%8B%95%E7%94%BB%E3%81%AE%E4%BD%9C%E6%88%90)
	- 読み上げ音声に画像を割り当てて、字幕付きの動画を簡単に作成します。
- [更新履歴](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E6%9B%B4%E6%96%B0%E5%B1%A5%E6%AD%B4)
	- 過去の更新履歴です。

## ライセンス

このリポジトリの内容は以下を除き [MIT License](./LICENSE.txt) です。

- インストール時に [ダウンロードするモノの一覧](https://github.com/Zuntan03/EasyNovelAssistant/blob/48350f45c838e4cda4f2a977c446e1f4141c858f/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat#L31) を表示します。
- `EasyNovelAssistant/setup/res/tkinter-PythonSoftwareFoundationLicense.zip` は Python Software Foundation License です。
- [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) がダウンロードする [JVNV](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvnv_corpus) 派生物は [CC BY-SA 4.0 DEED](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) です。
