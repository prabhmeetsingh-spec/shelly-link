from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name1 = request.args.get("name1", "Prabhmeet")
    name2 = request.args.get("name2", "Shelly the Rabbit")

    return f"""
<!DOCTYPE html>
<html>
<head>
  <title>Special Surprise 💖</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {{
      margin: 0;
      height: 100vh;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: Arial, sans-serif;
      overflow: hidden;
    }}

    .card {{
      background: white;
      padding: 25px;
      border-radius: 25px;
      text-align: center;
      box-shadow: 0 15px 30px rgba(0,0,0,0.3);
      max-width: 90%;
    }}

    h1 {{
      color: #e60073;
      font-size: 26px;
    }}

    .animals {{
      font-size: 60px;
      margin: 15px 0;
      animation: float 2s infinite ease-in-out;
    }}

    @keyframes float {{
      0% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-15px); }}
      100% {{ transform: translateY(0); }}
    }}

    .hidden-message {{
      display: none;
      font-size: 18px;
      color: #ff1493;
      margin-top: 15px;
    }}

    button {{
      margin-top: 15px;
      padding: 10px 20px;
      border: none;
      border-radius: 20px;
      background: #ff1493;
      color: white;
      font-size: 16px;
    }}

    .heart {{
      position: absolute;
      color: red;
      font-size: 20px;
      animation: fall 5s linear infinite;
    }}

    @keyframes fall {{
      0% {{
        transform: translateY(-10vh);
        opacity: 1;
      }}
      100% {{
        transform: translateY(110vh);
        opacity: 0;
      }}
    }}
  </style>
</head>

<body>

  <!-- Background Music -->
  <audio autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
  </audio>

  <div class="card">
    <h1>💖 {name1} loves {name2} 💖</h1>

    <div class="animals">🐰 🐒</div>

    <button onclick="reveal()">🎁 Click for Surprise</button>

    <div class="hidden-message" id="msg">
      Forever together 💕✨
    </div>
  </div>

  <script>
    function reveal() {{
      document.getElementById("msg").style.display = "block";
    }}

    function createHeart() {{
      const heart = document.createElement("div");
      heart.className = "heart";
      heart.innerHTML = "❤️";
      heart.style.left = Math.random() * 100 + "vw";
      heart.style.fontSize = (20 + Math.random() * 20) + "px";
      document.body.appendChild(heart);

      setTimeout(() => heart.remove(), 5000);
    }}

    setInterval(createHeart, 300);
  </script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
