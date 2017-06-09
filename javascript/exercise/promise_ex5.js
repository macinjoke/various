
async function executeAsync1(n) {
  for (let i=0; i < n; ++i) {
    const msg = await delayAndRandom();
    console.log(msg)
  }
  return 'executeAsync1 is done'
}

async function executeAsync2(n) {
  for (let i=0; i < n; ++i) {
    const msg = await delayAndRandom();
    console.log(msg)
  }
  return 'executeAsync2 is done'
}

async function executeExecuteAsync() {
  const msg1 = await executeAsync1(2);
  console.log(msg1);
  console.log('-------');
  const msg2 = await executeAsync2(4);
  console.log(msg2);
}

console.log('start')
executeExecuteAsync()
  .then(() => {
    console.log("全部成功したよ！");
  }).catch(() => {
    console.log("途中で失敗したみたい...");
  })
console.log('end')

function delayAndRandom() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // 90%の確率で0以外が入り、10%の確率で0が入る
      const isSuccess = Math.random() * 10 | 0;

      // デバッグ時は以下のコンソールを差しこんでおくと状況を把握しやすいかもです。
      console.log((isSuccess) ? "成功したっ" : "失敗した…");

      // 成功時はresolveを呼び、失敗時はrejectを呼ぶ
      isSuccess ? resolve('200') : reject('503');
    }, 1000);
  });
}
