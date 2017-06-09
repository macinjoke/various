
// asyncFunc関数に渡してたジェネレータを、async関数にする
(async () => {
  // 4回Promiseを待機する。
  // rejectされた時は、自動的にこの関数が中断されるからtry-catchで囲む必要もない。
  for (let i = 0; i < 4; ++i) {
    // yieldと書いてた部分をawaitにする
    await delayAndRandom();
  }
})().then(() => {
  // 全てresolveが呼ばれた場合、この関数が実行される
  console.log("全部成功したよ！");
}).catch(() => {
  // 途中1回でもreject関数が呼ばれた場合、この関数が実行される
  console.log("途中で失敗したみたい…");
});

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

