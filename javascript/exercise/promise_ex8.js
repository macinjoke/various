
function promiseBuyApple(payment){
  return new Promise(function(resolve, reject){
    setTimeout(() => {
      if(payment >= 150){
        resolve(payment-150);
      }else{
        reject('金額が足りません。');
      }
    }, 1000)
  });
}

promiseBuyApple(400).then(function(change){
  console.log('おつりは' + change + '円です');
  return promiseBuyApple(change);
}).then(function(change){
  console.log('おつりは' + change + '円です');
  return promiseBuyApple(change);
}).then(function(change){
  console.log('おつりは' + change + '円です');
}).catch(function(error){
  console.log('エラーが発生しました：' + error);
});

