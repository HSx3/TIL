// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)   // non-block, callback stack에 저장 후 다음을 실행
// console.log('end of program')

// // python code처럼 동작하게 하려면?
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)

// function first() {
//     console.log('first')
// }
// function second() {
//     console.log('second')
// }
// function third() {
//     console.log('third')
// }
// first()
// setTimeout(second, 1000)
// third()

// func1()를 호출했을때
// 아래와 같이 콘솔에 출력
// func1
// func3
// func2

// // 1.
// function func1() {
//     console.log('func1')
//     setTimeout(func2, 1000)
//     func3()
// }
// function func2() {
//     console.log('func2')
// }
// function func3() {
//     console.log('func3')
// }
// func1()

// 2. 
function func1() {
    console.log('func1')
    func2()
}
function func2() {
    setTimeout(() => console.log('func2'), 1000)
    func3()
}
function func3() {
    console.log('func3')
}
func1()

// const num_101 = function () {
//     return n => n + 1
// }
// console.log(num_101()(100))
