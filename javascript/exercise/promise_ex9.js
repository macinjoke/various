
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

async function buy_by_oturi() {
  let result;
  let payment = 500;
  console.log(payment + '円からスタート')
  while(true) {
    result = await promiseBuyApple(payment)
    console.log(result)
    payment = result
  }
}

buy_by_oturi()
  .then((data) => {
    console.log(data)
  })
  .catch((data) => {
    console.log(data)
  })
