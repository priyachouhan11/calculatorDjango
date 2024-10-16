const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = "";
}

function removeLastElement(){
    display.value = display.value.slice(0,-1);
}

function calculate() {
    try {
        var x = document.getElementById('display').value;
        x = x.replace(/×/g, '*').replace(/÷/g, '/');
        x = x.replace(/x/g, '*').replace(/×/g, '*');
        x = x.replace(/(\d+(\.\d+)?)%/g, '($1/100)');
        
        var y = eval(x);
        
        document.getElementById('display').value = y;
    } 
    catch (err) {
        document.getElementById('display').value = "Error";
    }
}