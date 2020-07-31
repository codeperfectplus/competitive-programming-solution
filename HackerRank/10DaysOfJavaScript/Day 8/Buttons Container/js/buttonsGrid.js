let btn1 = document.querySelector("#btn1");
let btn2 = document.querySelector("#btn2");
let btn3 = document.querySelector("#btn3");
let btn4 = document.querySelector("#btn4");
let btn5 = document.querySelector("#btn5");
let btn6 = document.querySelector("#btn6");
let btn7 = document.querySelector("#btn7");
let btn8 = document.querySelector("#btn8");
let btn9 = document.querySelector("#btn9");

btn5.addEventListener("click", () => {
    let bt1 = btn1.innerHTML;
    let bt2 = btn2.innerHTML;
    let bt3 = btn3.innerHTML;
    let bt4 = btn4.innerHTML;
    let bt6 = btn6.innerHTML;
    let bt7 = btn7.innerHTML;
    let bt8 = btn8.innerHTML;
    let bt9 = btn9.innerHTML;

    btn1.innerHTML = bt4;
    btn2.innerHTML = bt1;
    btn3.innerHTML = bt2;
    btn4.innerHTML = bt7;
    btn6.innerHTML = bt3;
    btn7.innerHTML = bt8;
    btn8.innerHTML = bt9;
    btn9.innerHTML = bt6;
})