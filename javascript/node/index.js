// Node10
  
// const promise = (message, msec) => new Promise((resolve, reject) => {
//   setTimeout(() => {
//     console.log(message);
//     resolve();
//   }, msec);
// });


async function promise(message, mesc) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(message);
      resolve(mesc);
    }, mesc)
  })
}

console.log("start")
console.log("=====")

const printMessage = async () => {
  // 2200秒で終わる
  try {
    await promise('hello', 1000)
    await promise('async', 200)
    await promise('world', 1000)
  } catch(e) {
    console.log("えらーだおｚ")
    console.log(e)
  }

  console.log('-------')
  // 1000秒で終わる
  await Promise.all([
    promise('hello', 1000),
    promise('async', 200),
    promise('world', 1000)
  ]).then((result) => {
    console.log("complete", result)
  })
  console.log("=====")
  console.log("end")
}

printMessage()
