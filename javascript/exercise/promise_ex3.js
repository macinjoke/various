
asyncFunc(function*() {
  // 4回Promiseを待機する。
  // rejectされた時は、自動的にこの関数が中断されるからtry-catchで囲む必要もない。
  for (let i = 0; i < 4; ++i) {
    yield delayAndRandom();
  }
}).then(() => {
  // 全てresolveが呼ばれた場合、この関数が実行される
  console.log("全部成功したよ！");
}).catch(() => {
  // 途中1回でもreject関数が呼ばれた場合、この関数が実行される
  console.log("途中で失敗したみたい…");
});

function asyncFunc(gen) {
  return new Promise((resolve, reject) => {
    // ジェネレータからイテレータを作成する
    const iter = gen();

    // 内部再帰的関数を実行する
    asyncFuncRec();

    // 実際に再帰する内部関数を定義する
    function asyncFuncRec(arg) {
      try {
        // イテレータを一つ進めてPromiseを1つ取り出す
        // その際に、ひとつ前のPromise実行時の結果を次のPromiseに与える
        const {value: promise, done} = iter.next(arg);

        // 終了条件を満たしていたら、resolveとする
        if (done) {
          resolve(arg);
          return;
        }

        promise
        // resolveされた際に、この関数を再帰的に呼ぶためにthenでつなげる
          .then((data) => {
            asyncFuncRec(data);
          })
          // rejectされた際には、その結果をこの関数自体の失敗として扱い、橋渡する
          .catch((err) => {
            reject(err);
          });
      }
      catch (err) {
        // 実行中に何らかの同期的なエラーが発生したら失敗として扱い、橋渡する
        reject(err);
      }
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
