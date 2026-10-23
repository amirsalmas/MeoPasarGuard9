<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8"><title>MeoPanel</title>
    <style>
        body { background-color: #0f0f13; color: #d4af37; font-family: Tahoma; text-align: center; padding-top: 50px; }
        .logo { width: 120px; height: 120px; border: 2px solid #d4af37; border-radius: 50%; margin: 0 auto 20px; background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Faravahar_silver_coin.png/200px-Faravahar_silver_coin.png'); background-size: contain; background-repeat: no-repeat; background-position: center; background-color: #1a1a2e; }
        h1 { color: #d4af37; }
        .box { background: rgba(26, 26, 46, 0.9); border: 1px solid #d4af37; padding: 30px; border-radius: 15px; width: 80%; max-width: 500px; margin: 30px auto; }
        .btn { background-color: #d4af37; color: #1a1a2e; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="logo"></div>
    <h1>پنل میو پاسارگارد</h1>
    <div class="box">
        <p>به پنل مدیریت خوش آمدید. برای دریافت کانفیگ به ربات تلگرام مراجعه کنید.</p>
        <a href="https://t.me/meov2ray" target="_blank" class="btn">ورود به کانال</a>
    </div>
    <!-- پلیر آهنگ‌ها -->
    <audio id="bg-music" autoplay loop></audio>
    <script>
        const playlist = ["/static/music-panel.mp3", "/static/3_Am_Walk_Daniel.mp3"];
        let current = 0;
        const player = document.getElementById('bg-music');
        player.src = playlist[current];
        player.addEventListener('ended', () => {
            current = (current + 1) % playlist.length;
            player.src = playlist[current];
            player.play();
        });
    </script>
</body>
</html>
