function myFunction() {
    let num1 = 5;
    let num2 = 4;

    document.getElementById("result").innerHTML = num1;
    document.getElementById("result1").innerHTML = num2;

    let titleText = document.getElementById("demo").firstChild.nodeValue;

    let sum = add(num1, num2);

    document.getElementById("result").innerHTML =
        "Title text: " + titleText;

    document.getElementById("result1").innerHTML =
        "Sum: " + sum;
}
function add(a, b) {
    return a + b;
}