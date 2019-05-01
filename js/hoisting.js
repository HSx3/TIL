// // 1. let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x)  // 정운지
//     {
//         let x = 1
//         console.log(x)  // 1
//     }
//     console.log(x)  // 정운지
// }
// // console.log(x)  // Error
// console.log(typeof x)   // undefined

// // 1-1.
// let foo
// let bar = undefined

// foo // undefined
// bar // undefined
// baz // ReferenceError baz is not defined

// // 1-2.
// // 우리가 쓴 코드
// y
// var y = 1
// y

// // JS가 이해한 코드
// var y
// y   // undefined
// y = 1   // 1
// y   // 1

// 1-3.
if (x !== 1) {
    console.log(y)  // undefined
    var y = 3
    if (y == 3) {
        var x = 1
    }
    console.log(y)  // 3
}
if (x === 1) {
    console.log(y)  // 3
}

// 1-4.
// var로 변수를 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다.
var x = 1
if (x === 1) {
    var x = 2
    console.log(x)  // 2
}
console.log(x)      // 2

// // 1-5.
// // 함수 호이스팅
// // ssafy 함수가 선언되기 전에 ssafy()로 호출된 형태
// ssafy()
// function ssafy() {
//     console.log('hoisting!')
// }

// 1-6.
// 변수에 할당한 함수는 호이스팅 되지 않는다.
ssafy()
let ssafy = function () {
    console.log('hoisting!')
}

// 일급객체의 3가지 조건 예
// 1.
const fco = function () {   // 1. 변수 fco에 함수가 저장
    return n => n + 1   // 3. return value가 익명함수
}
console.log(fco)    // 2. fco가 console.log() 함수의 인자로 전달

// num_101에 101을 담아야 한다.
const num_101 = function () {
    return n => n + 1
}
console.log(num_101()(100))