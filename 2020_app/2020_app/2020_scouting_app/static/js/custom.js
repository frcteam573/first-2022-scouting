function minus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-1;
}

function plus(namein) {
var x = document.getElementsByName(namein)[0].value;
document.getElementsByName(namein)[0].value = x-(-1);
}