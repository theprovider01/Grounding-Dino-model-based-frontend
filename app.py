from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Clickable Title</title>
        <script>
            function calculateScore() {
                document.getElementById('score').innerText = "Score: " + Math.floor(Math.random() * 100);
            }
        </script>
    </head>
    <body>
        <h1 onclick="calculateScore()" style="cursor: pointer; color: blue;">Click Me to Calculate Score</h1>
        <p id="score">Score: --</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
