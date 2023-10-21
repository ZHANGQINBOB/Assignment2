let history = [];
const API_URL = 'http://localhost:5000/api/data';

function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function deleteLastDigit() {
    var display = document.getElementById('display');
    var currentValue = display.value;

    if (currentValue.length > 0) {
        display.value = currentValue.slice(0, -1);
    }
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    let expression = document.getElementById('display').value;
    
    // Check for empty input
    if (expression.trim() === '') {
        alert('Please enter an expression before calculating.');
        return;
    }

    try {
        let result = eval(expression);
        document.getElementById('display').value = result;
        console.log(result);

        post(expression, result);

        // Update history
        history.push(expression + ' = ' + result);
    } catch (error) {
        console.error('Error during calculation:', error);
        alert('Invalid expression. Please check your input.');
    }
}

function post(expression, result) {
    const data = {
        expression: expression,
        result: result
    };

    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok');
        }
    })
    .then(data => {
        console.log('POST request successful:', data);
    })
    .catch(error => {
        console.error('POST request error:', error);
    });
}


function updateHistory() {
    fetch(API_URL, {
        method: 'GET',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok');
        }
    })
    .then(data => {
        // Update history array
        history = data;

        // Update history record display
        let historyElement = document.getElementById('history');
        historyElement.innerHTML = '';
        for (let i = 0; i < history.length; i++) {
            let p = document.createElement('p');
            p.textContent = history[i];
            historyElement.appendChild(p);
        }
    })
    .catch(error => {
        console.error('GET request error:', error);
    });
}