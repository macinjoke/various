
// 再帰的な処理でラップした関数を呼ぶことで解決する
delayAndRandomN(4) // 4秒なので4を渡す
  .then(() => {
    // 全てresolveが呼ばれた場合、この関数が実行される
    console.log("全部成功したよ！");
  })
  .catch(() => {
    // 途中1回でもreject関数が呼ばれた場合、この関数が実行される
    console.log("途中で失敗したみたい…");
  });

function delayAndRandomN(limit) {
  // 0秒の時は即完了させる
  if (!limit--) return Promise.resolve();

  return new Promise((resolve, reject) => {
    // 内部再帰的関数を実行する
    delayAndRandomRec();

    // 実際に再帰する内部関数を定義する
    function delayAndRandomRec() {
      // とりあえず実行して1秒待ってみる
      delayAndRandom()
        .then(() => {
          // まだ実行回数が残っていたら再帰的に呼び出す。
          // 実行回数が残ってなければ、全部成功したので完了させる。
          (limit--) ? delayAndRandomRec() : resolve();
        })
        // 1度でも失敗した時は即失敗扱いとして終了させる
        .catch(reject);
    }
  });
}

function delayAndRandom() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // 90%の確率で0以外が入り、10%の確率で0が入る
      const isSuccess = Math.random() * 10 | 0;

      // デバッグ時は以下のコンソールを差しこんでおくと状況を把握しやすいかもです。
      console.log((isSuccess) ? "成功したっ" : "失敗した…");

      // 成功時はresolveを呼び、失敗時はrejectを呼ぶ
      isSuccess ? resolve() : reject();
    }, 1000);
  });
}

