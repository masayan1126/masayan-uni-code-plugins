Bashスクリプトテンプレート
さっそく、ここにご紹介します。


#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

usage() {
  cat << EOF # remove the space between << and EOF, this is due to web plugin issue
Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-v] [-f] -p param_value arg1 [arg2...]

Script description here.

Available options:

-h, --help      Print this help and exit
-v, --verbose   Print script debug info
-f, --flag      Some flag description
-p, --param     Some param description
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -f | --flag) flag=1 ;; # example flag
    -p | --param) # example named parameter
      param="${2-}"
      shift
      ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
  [[ -z "${param-}" ]] && die "Missing required parameter: param"
  [[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}

parse_params "$@"
setup_colors

# script logic here

msg "${RED}Read parameters:${NOFORMAT}"
msg "- flag: ${flag}"
msg "- param: ${param}"
msg "- arguments: ${args[*]-}"
あまり長くしたくないというのが私の考えでした。スクリプトのロジックまで500行もスクロールしたくありません。同時に、どんなスクリプトにも強固な基盤がほしいと思っています。しかし、Bashでは依存関係管理が全くないため、それが容易ではありません。

一つの解決策としては、すべての定型文とユーティリティ関数を含んだ別のスクリプトを用意し、それを最初に実行することです。ただし、この2つ目のファイルを常にどこにでも添付する必要があり、「シンプルなBashスクリプト」というアイデアが途中で崩れてしまうという欠点があります。そこで、テンプレートには必要最小限のものだけを組み込み、可能な限り短くすることにしました。

それでは、さらに詳しく見てみましょう。

Bashを選択

#!/usr/bin/env bash
スクリプトは伝統的にシェバンで始まります。 互換性を最大限に高めるため、 を 直接参照する/usr/bin/envのではなく、 を参照します/bin/bash 。ただし、リンク先のStackOverflowの質問のコメントを読むと、この方法でも失敗する場合があることがわかります。

早く失敗する

set -Eeuo pipefail
この set コマンドはスクリプトの実行オプションを変更します。例えば、 通常、Bashはコマンドが失敗して0以外の終了ステータスコードを返しても気にしません。ただ次のコマンドに進みます。では、次の小さなスクリプトを考えてみましょう。


#!/usr/bin/env bash
cp important_file ./backups/
rm important_file
ディレクトリが存在しない場合はどうなるでしょうか backups ? コンソールにエラーメッセージが表示されますが、対応できるようになる前に、2 番目のコマンドによってファイルがすでに削除されています。

set -Eeuo pipefail 具体的にどのようなオプションが変更され、それがどのように保護されるか についての詳細は 、数年前からブックマークしている記事を参照してください。

ただし、これらのオプションを設定することに反対する意見もいくつかあることを知っておく必要があります 。

場所を取得する

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
この行は スクリプトのディレクトリを定義し、それ に基づいて処理を実行しますcd 。なぜでしょうか？

多くの場合、スクリプトはスクリプトの場所を基準とした相対パスで操作し、ファイルをコピーしたりコマンドを実行したりしますが、その際、スクリプトディレクトリは作業ディレクトリでもあると想定しています。そして、スクリプトをそのディレクトリから実行する限り、それは事実です。

しかし、たとえば CI 構成で次のようなスクリプトを実行するとします。

/opt/ci/project/script.sh
スクリプトはプロジェクトディレクトリではなく、CIツールの全く別の作業ディレクトリで動作しています。スクリプトを実行する前にそのディレクトリに移動することで、この問題を修正できます。

cd /opt/ci/project && ./script.sh
しかし、スクリプト側で解決する方がはるかに簡単です。スクリプトがファイルを読み込んだり、同じディレクトリから別のプログラムを実行したりする場合は、次のように呼び出します。


cat "$script_dir/my_file"
同時に、スクリプトはworkdirの場所を変更しません。スクリプトが他のディレクトリから実行され、ユーザーがファイルへの相対パスを指定した場合、そのファイルを読み取ることは可能です。

掃除してみる

trap cleanup SIGINT SIGTERM ERR EXIT

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}
trap スクリプトのブロックのようなもの を想像してみてください finally 。スクリプトの最後（正常終了、エラー発生、外部シグナル発生など）で cleanup() 関数が実行されます。例えば、スクリプトによって作成されたすべての一時ファイルを削除してみるなど、この場所で処理を実行できます。

cleanup() はスクリプトの最後だけでなく、作業のどの段階でも呼び出すことができることを覚えておいてください 。クリーンアップしようとするリソースがすべて存在するとは限りません。

役立つヘルプを表示する

usage() {
  cat << EOF # remove the space between << and EOF, this is due to web plugin issue
Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-v] [-f] -p param_value arg1 [arg2...]

Script description here.

...
EOF
  exit
}
usage() スクリプトの上部に比較的近いため 、次の 2 つの方法で動作します。

すべてのオプションを知らず、スクリプト全体を調べてオプションを見つけたくない人のためにヘルプを表示する。
誰かがスクリプトを変更した場合 (たとえば、2 週間後に最初にスクリプトを書いたことを覚えていない場合) の最小限のドキュメントとして 。
ここで全ての関数をドキュメント化することに異論はありません。しかし、簡潔で分かりやすいスクリプトの使い方メッセージは最低限必要です。

素敵なメッセージを印刷する

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}
まず、 setup_colors() テキストに色を使いたくないのであれば、この機能は削除してください。毎回Googleでコードを検索しなくても済むなら、もっと頻繁に色を使うだろうと分かっているので、この機能は残しています。

第二に、これらの 色はコマンドではなく 関数でのみ使用されることを意図しています msg()echo 。

この msg() 関数は、スクリプト出力以外のすべてのものを出力するために使用します。これにはエラーだけでなく、すべてのログとメッセージが含まれます。12 Factor CLI Appsの素晴らしい 記事を引用します。

簡単に言うと、stdoutは出力用、stderrはメッセージ用です。〜CLIアプリの構築 に 少し詳しい
Jeff Dickey

そのため、ほとんどの場合、色を使用するべきではありません stdout 。

で印刷されたメッセージ はストリームmsg() に送信され stderr 、カラーなどの特殊シーケンスをサポートします。 stderr 出力が対話型端末でない場合、または標準パラメータのいずれか が渡された場合、カラーは無効になります。

使用法：


msg "This is a ${RED}very important${NOFORMAT} message, but not a script output value!"
が対話型ターミナルではない場合の動作を確認するには stderr 、上記のような行をスクリプトに追加します。次に、 stderr に リダイレクトしstdout てパイプで に 渡しますcat。パイプ操作により、出力はターミナルに直接送られるのではなく、次のコマンドに送られるため、色は無効になるはずです。

./test.sh 2>&1 | cat
This is a very important message, but not a script output value!
任意のパラメータを解析する

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -f | --flag) flag=1 ;; # example flag
    -p | --param) # example named parameter
      param="${2-}"
      shift
      ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
  [[ -z "${param-}" ]] && die "Missing required parameter: param"
  [[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}
スクリプト内でパラメータ化が適切な場合は、通常そうします。スクリプトが1か所でしか使用されない場合でもそうです。そうすることで、コピーして再利用しやすくなります。多くの場合、すぐにそれが実現します。また、何かをハードコードする必要がある場合でも、通常はBashスクリプトよりも上位のレベルで、より適切な場所があります。

CLIパラメータに は、フラグ、名前付きパラメータ、位置引数 の3つの主要な種類があります 。このparse_params() 関数はこれらすべてをサポートしています。

ここで扱われていない唯一の共通パラメータパターンは、 複数の1文字フラグを連結したもの-abです。2つのフラグを ではなく として 渡すには 、-a -b追加のコードが必要になります。

ループ while はパラメータを手動で解析する方法です。他の言語では 組み込みパーサー や 利用可能なライブラリのいずれかを使用する必要がありますが、これはBashです。

テンプレートには、 サンプルフラグ（-f）と名前付きパラメータ（ ）が含まれています。これらを変更またはコピーするだけで、他のパラメータを追加できます。 その後、 を更新することを忘れないでください。-pusage()

ここで重要なのは、Bashの引数解析に関するGoogleの最初の検索結果をそのまま受け取るだけでは見落とされがちな、 不明なオプションに対してエラーをスローすることです。スクリプトが不明なオプションを受け取ったということは、ユーザーがスクリプトで実行できない処理を実行させたいと考えていることを意味します。そのため、ユーザーの期待とスクリプトの動作は大きく異なる可能性があります。何か問題が発生する前に、実行を完全に阻止する方が賢明です。

Bash でパラメータを解析する方法は 2 つあります。 と です getopt 。 これらを使用することには賛否両論getoptsがあります 。macOS ではデフォルトで は全く異なる動作 をし 、 のような長いパラメータをサポートしていない ため、 これらのツールは最適ではないと感じました。 getoptgetopts--help

テンプレートの使用
インターネットで見つかるほとんどのコードと同様に、コピーして貼り付けるだけです。

まあ、実のところ、それはかなり正直なアドバイスでした。Bashには、これと同等の汎用的なものはありません npm install 。

コピーした後は、次の 4 つの点だけ変更する必要があります。

usage() スクリプトの説明を含むテキスト
cleanup() コンテンツ
のパラメータ parse_params() – と は--help そのまま --no-colorに、例のパラメータを置き換えます: -f と -p
実際のスクリプトロジック
携帯性
このテンプレートをMacOS（デフォルトの古いBash 3.2）と複数のDockerイメージ（Debian、Ubuntu、CentOS、Amazon Linux、Fedora）でテストしました。問題なく動作しました。

当然ですが、Alpine LinuxのようにBashが存在しない環境では動作しません。Alpineはミニマルシステムとして、非常に軽量なash（Almquistシェル）を使用しています。

ほぼどこでも使えるBourne Shell互換のスクリプトを使う方が良いのではないかという疑問も湧きます 。少なくとも私の場合は、答えは「いいえ」です。Bashの方が安全で強力（それでもまだ使いにくいですが）なので、滅多に使わないLinuxディストリビューションのサポートが不足していることは許容できます。

