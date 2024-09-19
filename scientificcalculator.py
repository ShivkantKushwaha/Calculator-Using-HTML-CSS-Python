from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with result placeholder
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="calculator">
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="post">
            <input type="number" name="num1" placeholder="First number" required>
            <select name="operation" required>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <input type="number" name="num2" placeholder="Second number" required>
            <button type="submit">Calculate</button>
        </form>
        <div class="result">
            <p id="output">{{ result }}</p>
        </div>
    </div>
</body>
</html>
'''

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation"

@app.route('/', methods=['GET'])
def home():
    return render_template_string(html_template, result="")

@app.route('/calculate', methods=['POST'])
def calculate_route():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    result = calculate(num1, num2, operation)
    return render_template_string(html_template, result=f"The result is: {result}")

if __name__ == '__main__':
    app.run(debug=True)
