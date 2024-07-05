# EasyNovelAssistant

軽量で規制も検閲もない日本語ローカル LLM『[LightChatAssistant-TypeB](https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF)』による、簡単なノベル生成アシスタントです。  
ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。

内部で呼び出している [KoboldCpp](https://github.com/LostRuins/koboldcpp) や [Style-Bert-VITS2](https://github.com/litagin02/Style-Bert-VITS2) を直接利用することもできますし、[EasySdxlWebUi](https://github.com/Zuntan03/EasySdxlWebUi) で画像を生成しながら利用することもできます。

## 利用者の声

**記事**

- 『[【検閲なし】GPUで生成するローカルAIチャット環境と小説企画＋執筆用ゴールシークプロンプトで叡智小説生成最強に見える](https://note.com/kagami_kami/n/n3a321d926684)』[@kagami_kami_m](https://twitter.com/kagami_kami_m/status/1785313774620246194)
	- [@Emanon_14](https://twitter.com/Emanon_14/status/1787491885801783753),
	[@bla_tanuki](https://twitter.com/bla_tanuki/status/1786969054336700924),
	[@bla_tanuki](https://twitter.com/bla_tanuki/status/1786982703692382277),
- 作例『[[AI試運転]スパーリング・ウィズ・ツクモドウ](https://note.com/liruk/n/nfd0bb54903cb)』と [制作の感想](https://twitter.com/liruk/status/1785596479631204420)。

**動画**

[EasyNovelAssistantの利用検証](https://www.nicovideo.jp/watch/sm43774612),
[負けヒロインの告白](https://www.nicovideo.jp/watch/sm43754628)

**つぶやき**

[@AIiswonder](https://x.com/AIiswonder/status/1791854351457325319),
[@umiyuki_ai](https://x.com/umiyuki_ai/status/1791360673575997553),
[@dew_dew](https://x.com/dew_dew/status/1790402531459555696),
[@StelsRay](https://twitter.com/StelsRay/status/1789525236557492374),
[@kirimajiro](https://twitter.com/kirimajiro/status/1788173520612344283),
[@Ak9TLSB3fwWnMzn](https://twitter.com/Ak9TLSB3fwWnMzn/status/1787123194991931852),
[@Emanon_14](https://twitter.com/Emanon_14/status/1787317994345070865),
[@liruk](https://twitter.com/liruk/status/1787318402736115994),
[@maru_ai29](https://twitter.com/maru_ai29/status/1787059183621378073),
[@bla_tanuki](https://twitter.com/bla_tanuki/status/1786968425430167829),
[@muchkanensys](https://twitter.com/muchkanensys/status/1786991909409595529),
[@shinshi78](https://twitter.com/shinshi78/status/1786991262387888451),
[865](https://fate.5ch.net/test/read.cgi/liveuranus/1714702930/865),
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
[@mikumiku_aloha](https://twitter.com/mikumiku_aloha/status/1785300629461799372),
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

### お知らせへの反応
- [読み上げ音声に画像を割り当てて、字幕付きの動画の簡単作成に対応](https://twitter.com/Zuntan03/status/1786694765997924371)
	- [@yuki_shikihime](https://twitter.com/yuki_shikihime/status/1786718565384790201)
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

## インストールと更新

インストールや更新で困ったことが起きたら、[こちら](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E6%9B%B4%E6%96%B0) を参照してください。  

1. [`Install-EasyNovelAssistant.bat`](https://github.com/Zuntan03/EasyNovelAssistant/raw/main/EasyNovelAssistant/setup/Install-EasyNovelAssistant.bat?v=2) を右クリックして `名前をつけて保存` で、インストール先フォルダ（**英数字のパスで空白や日本語を含まない**）にダウンロードして実行します。
	- **`WindowsによってPCが保護されました` と表示されたら、`詳細表示` から `実行` します。**
	- `配布元から関連ファイルをダウンロード` することに問題がなければ `y` を入力します。
	- `Windows セキュリティ` のネットワークへのアクセス許可は `許可` してください。
1. インストールが完了すると、自動的に EasyNovelAssistant が起動します。  

インストール完了後は
- `Run-EasyNovelAssistant.bat` で起動します。
- `Update-EasyNovelAssistant.bat` で更新します。

**次のステップは [はじめての生成](https://github.com/Zuntan03/EasyNovelAssistant/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%A6%E3%81%AE%E7%94%9F%E6%88%90) です。**

## 最近の更新

### 2024/07/05

- 『[Kagemusya-7B-v1](https://huggingface.co/Local-Novel-LLM-project/kagemusya-7B-v1)』『[Shadows-MoE](https://huggingface.co/Local-Novel-LLM-project/Shadows-MoE)』『[Ninja-V3-7B](https://huggingface.co/Local-Novel-LLM-project/Ninja-V3)』を追加しました。

### 2024/06/16

- 『[Ninja-V2-7B](https://huggingface.co/Local-Novel-LLM-project/Ninja-V2-7B)』を追加しました。

### 2024/06/14

- KoboldCpp を更新する `Update-KoboldCpp.bat` と、CUDA 12版の KoboldCpp に更新する `Update-KoboldCpp_CUDA12.bat` を追加しました。
	- CUDA 12版は最近の NVIDIA GPU でより高速に動作します。

### 2024/05/29

- 『[Ninja-v1-RP-expressive-v2](https://huggingface.co/Aratako/Ninja-v1-RP-expressive-v2)』を追加しました。

### 2024/05/23

- [Aratako さんの自信作な新モデル](https://twitter.com/Aratako_LM/status/1792940043813920862) 『[Ninja-v1-RP-expressive](https://huggingface.co/Aratako/Ninja-v1-RP-expressive)』を追加しました。
	- ロールプレイ用モデルですが、他の用途でも使えそうな感触です。
	- ロールプレイ（チャット）をしたい場合は [プロンプトフォーマット](https://huggingface.co/Aratako/Ninja-v1-RP-expressive#%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88) を確認して、`KoboldCpp/koboldcpp.exe` を [直接ご利用ください](https://github.com/Zuntan03/EasyNovelAssistant/wiki/Tips#koboldcpp)。

### 2024/05/22

- [Japanese-TextGen-Kage](https://huggingface.co/dddump/Japanese-TextGen-Kage-v0.1-2x7B-gguf) の更新に対応しました。

### 2024/05/19

- `生成` メニューの `生成の開始/終了 (Shift+F5)` のトグル誤操作の対策として、`生成を開始 (F3)` と `生成を終了 (F4)` を追加しました。  
![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/gen_start_stop.png)
- [Japanese-TextGen-MoE-TEST-2x7B-NSFW](https://huggingface.co/dddump/Japanese-TextGen-MoE-TEST-2x7B-NSFW-gguf) と [Japanese-Chat-Evolve-TEST-NSFW](https://huggingface.co/dddump/Japanese-Chat-Evolve-TEST-7B-NSFW-gguf) の Ch200 差し替え版に対応しました。
	- [Japanese-Chat-Evolve-TEST-NSFW](https://huggingface.co/dddump/Japanese-Chat-Evolve-TEST-7B-NSFW-gguf) の `コンテキストサイズ上限` が `8K` から `4K` に下がっていますので、ご注意ください。

### 2024/05/17

- [Japanese-TextGen-MoE-TEST-2x7B-NSFW](https://huggingface.co/dddump/Japanese-TextGen-MoE-TEST-2x7B-NSFW-gguf) の [ファイル名変更](https://huggingface.co/dddump/Japanese-TextGen-MoE-TEST-2x7B-NSFW-gguf/commit/f39f2353116283a863d86d7406375c6904007364#d2h-964057) に対応しました。

### 2024/05/16

- [Japanese-TextGen-MoE-TEST-2x7B-NSFW](https://huggingface.co/dddump/Japanese-TextGen-MoE-TEST-2x7B-NSFW-gguf) 作者 [dddump さん](https://huggingface.co/dddump) の新モデル 2種を追加しました。
	- [Japanese-Chat-Evolve-TEST-NSFW](https://huggingface.co/dddump/Japanese-Chat-Evolve-TEST-7B-NSFW-gguf) は `コンテキストサイズ上限` を `8K` まで設定できます。
	- [Japanese-TextGen-Kage](https://huggingface.co/dddump/Japanese-TextGen-Kage-v0.1-2x7B-gguf) は `コンテキストサイズ上限` を `32K` まで設定できます。
		- Geforce RTX 3060 12GB 環境では  `コンテキストサイズ上限` が `16K` だと `GPU レイヤー` を `L33` でフルロードできます。

### 2024/05/11

大規模な更新ですので、不具合がありましたらお知らせください。

![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/tab.png)

- プロンプト入力欄がタブ付きになり、複数のプロンプトの比較や調整がやりやすくなりました。  
	![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/tabs.png)
- 複数ファイルやフォルダを開けます。ドラッグ＆ドロップにも対応しています。
	- 最近開いたフォルダや最近使ったファイルで作業状況を復元できます。
		- ファイル名順で読み込みますので、プロンプト順のコントロールに活用ください。  
		![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/recent.png)
- タブに `イントロプロンプト` を指定すると、他のタブのプロンプトを生成時に付け足せます。
	- 世界観、キャラ設定、あらすじなどをイントロとして、各章の執筆を別タブ・別ファイルで進められます。
	- 入力欄の先頭に `// intro\n` があると `イントロプロンプト` として扱います。
		- タブを右クリックして、`イントロプロンプト` で設定してください。  
		![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/intro.png)
- これらの章別執筆のサンプルを `sample/GoalSeek/` に用意しました（[@kagami_kami_m さんの記事](https://note.com/kagami_kami/n/n3a321d926684) を元にしています）。
	- `GoalSeek` のフォルダをドラッグ＆ドロップして、フォルダごと読み込みます。
	- 例えば `10-序章` タブを生成する際に、イントロプロンプトに指定した `01-執筆` が自動的に前に付け足されます。
		- 前章を記憶として付け足したり、執筆済みの章を要約して任意に付け足したりもできます。
- 最近の個性豊かな軽量モデル公開ラッシュに対応しました。
	- [Japanese-TextGen-MoE-TEST-2x7B-NSFW](https://huggingface.co/dddump/Japanese-TextGen-MoE-TEST-2x7B-NSFW-gguf)
	- [ArrowPro-7B-RobinHood](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf)
	- [ArrowPro-7B-RobinHood-toxic](https://huggingface.co/Aratako/ArrowPro-7B-RobinHood-toxic-GGUF)
	- [ArrowPro-7B-KUJIRA](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf)
	- [Fugaku-LLM-13B-instruct](https://huggingface.co/mmnga/Fugaku-LLM-13B-instruct-gguf)
- `llm_sequence.json` のフォーマットを変更しました。
	- 詳細は `EasyNovelAssistant/setup/res/default_llm_sequence.json` を参照ください。
- 入力欄タブのコンテキストメニューに `タブを複製` を追加しました。

### 2024/05/10

- [Ocuteus-v1](https://huggingface.co/Local-Novel-LLM-project/Ocuteus-v1-gguf) を KoboldCpp で試せる `KoboldCpp/Launch-Ocuteus-v1-Q8_0-C16K-L0.bat` を追加しました。
	- GPU レイヤーを増やして高速化したい場合は、bat をコピーして `Launch-Ocuteus-v1-Q8_0-C16K-L33.bat` などにリネームし、`set GPU_LAYERS=0` を `set GPU_LAYERS=33` に書き換えます。

![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/Ocuteus.png)

### 2024/05/07

- `設定` メニューに `フォント`、`フォントサイズ`、`テーマカラーの反転` を追加しました。
	- フォントの選択欄が上下にとても長くなっていますので、キーボードの上下キーで選択してください。
	- `config.json` の以下の項目を編集すれば、細かく色を設定することもできます。

```
	"foreground_color": "#CCCCCC",
	"select_foreground_color": "#FFFFFF",
	"background_color": "#222222",
	"select_background_color": "#555555",
```

![](https://raw.githubusercontent.com/wiki/Zuntan03/EasyNovelAssistant/img/ChangeLog/font_setting.png)

### 2024/05/06

- `コンテキストサイズ上限` 以上の `生成文の長さ` を指定した際に、`生成文の長さ` を自動的に短縮するようにしました。
	- アップデート後に入力欄と関係のない文章が生成されていた方は、この対応で修正されます。
	- `生成文の長さ` が 4096 以上の長文を生成する方法
		- モデルを Vecteus(4K) からLightChatAssistant や Ninja に変更
		- `コンテキストサイズ上限` を 6144 以上に設定
		- `生成文の長さ` を 4096 以上に設定
	- `コンテキストサイズ上限` を増やすと VRAM 消費も増えますので、動作しない場合はモデルの GPU レイヤー数（`L33` など）を引き下げてください。
- `sample/user.json` ファイルがあれば、他の `sample/*.json` と同じように `ユーザー` メニューを追加するようにしました。

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
