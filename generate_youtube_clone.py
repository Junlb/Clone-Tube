import os

video_folder = "videos"
output_html = "index.html"

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>My YouTube Clone with Search & Dark Mode & Responsive Videos</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #f5f5f5;
      text-align: center;
      color: #222;
      transition: background-color 0.3s, color 0.3s;
    }
    body.dark {
      background: #121212;
      color: #eee;
    }
    h1 { color: #d00000; }
    body.dark h1 { color: #ff6b6b; }
    .search-box {
      margin-bottom: 20px;
    }
    .search-box input {
      width: 300px;
      padding: 8px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      transition: background-color 0.3s, color 0.3s, border-color 0.3s;
    }
    body.dark .search-box input {
      background-color: #222;
      color: #eee;
      border-color: #555;
    }
    .video-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 30px;
      margin-top: 20px;
    }
    .video-box {
      background: white;
      padding: 10px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      max-width: 320px;
      flex: 1 1 320px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: background-color 0.3s, box-shadow 0.3s;
    }
    body.dark .video-box {
      background: #222;
      box-shadow: 0 2px 10px rgba(255,255,255,0.1);
    }
    video {
      width: 100%;
      height: auto;
      border-radius: 5px;
    }
    p {
      margin-top: 10px;
      font-weight: bold;
      font-size: 16px;
      color: inherit;
    }
    .toggle-btn {
      cursor: pointer;
      background: #d00000;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      font-size: 14px;
      margin-bottom: 20px;
      transition: background-color 0.3s;
    }
    .toggle-btn:hover {
      background: #a00000;
    }
  </style>
</head>
<body>
  <h1>🎬 My Video Gallery</h1>
  <button class="toggle-btn" onclick="toggleDarkMode()">Toggle Dark Mode</button>
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="Search videos..." onkeyup="filterVideos()" />
  </div>
  <div class="video-container" id="videoContainer">
'''

for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        video_path = f"{video_folder}/{filename}"
        name = filename.replace(".mp4", "")
        html += f'''
    <div class="video-box" data-title="{name.lower()}">
      <video controls>
        <source src="{video_path}" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <p>{name}</p>
    </div>
'''

html += '''
  </div>
  <script>
    function filterVideos() {
      const input = document.getElementById('searchInput');
      const filter = input.value.toLowerCase();
      const container = document.getElementById('videoContainer');
      const videos = container.getElementsByClassName('video-box');
      for (let i = 0; i < videos.length; i++) {
        const title = videos[i].getAttribute('data-title');
        videos[i].style.display = title.includes(filter) ? "" : "none";
      }
    }

    function toggleDarkMode() {
      document.body.classList.toggle('dark');
      if(document.body.classList.contains('dark')){
        localStorage.setItem('darkMode', 'enabled');
      } else {
        localStorage.removeItem('darkMode');
      }
    }

    window.onload = function() {
      if(localStorage.getItem('darkMode') === 'enabled'){
        document.body.classList.add('dark');
      }
    }
  </script>
</body>
</html>
'''

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Done! Open 'index.html' in your browser to see your videos with search, dark mode, and responsive video sizes.")
