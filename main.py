from flask import Flask
from time import time

app = Flask(__name__)


@app.route("/")
def tested_fog():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>THE FOG IS COMING</title>
</head>
<body>
    <h1 id="fogText"></h1>

    <script>
        var fogCount = Math.floor(Date.now() / 10000000);
        var fogString = "THE FOG IS COMING";
        for (var i = 0; i < fogCount; i++) {
            fogString += " THE FOG IS COMING";
        }
        document.getElementById("fogText").innerText = fogString;
    </script>
</body>
</html> 
    """

if __name__ == "__main__":
    app.run(port=9014)
