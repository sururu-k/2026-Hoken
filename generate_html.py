import base64
import os

def get_base64(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

cover_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\cover-chita.jpg')
steel_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\steel.jpg')
canal_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\aichi-canal.jpg')
map_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\isebay_map.jpg')
reg_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\water_regulation.jpg')
nori_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\nori.jpg')

html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>産業排水や水質汚濁と健康</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/theme/white.min.css">
  <style>
    :root {
      --corporate-blue: #0072ba;
      --text-main: #0f172a;
      --text-sub: #475569;
      --border-gray: #cbd5e1;
      --bg-white: #ffffff;
    }
    body { background: #1e293b; margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif; }
    .reveal { background: var(--bg-white); }
    .reveal .slides section { width: 100% !important; height: 100% !important; padding: 0 !important; display: flex !important; flex-direction: column !important; }
    .standard-header { height: 90px; padding: 20px 50px 12px; border-bottom: 4px solid var(--corporate-blue); display: flex; justify-content: space-between; align-items: flex-end; background: #fff; }
    .standard-header h2 { font-size: 32px !important; font-weight: bold !important; color: var(--text-main) !important; margin: 0 !important; }
    .standard-header .header-meta { font-size: 16px; font-weight: bold; color: var(--corporate-blue); }
    .slide-body { flex: 1; padding: 30px 50px 40px; background: #fff; display: flex; align-items: center; }
    
    .two-column { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; align-items: center; width: 100%; min-height: 420px; }
    .two-column.no-image { grid-template-columns: 1fr !important; gap: 0 !important; }
    .two-column.no-image .media-box { display: none !important; border: none !important; }

    .content-heading { font-size: 23px; font-weight: bold; color: var(--text-main); margin-bottom: 8px; display: flex; align-items: center; }
    .content-heading::before { content: "■"; color: var(--corporate-blue); margin-right: 10px; font-size: 16px; }
    .content-text { font-size: 19px; line-height: 1.7; color: #1e293b; margin-bottom: 20px; padding-left: 26px; }
    
    .media-box { width: 100%; height: 420px; border: 1px solid var(--border-gray); border-radius: 6px; overflow: hidden; background: #fff; }
    .media-box img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .media-box:empty, .media-box img[src=""], .media-box img:not([src]) { display: none !important; border: none !important; }
    .simple-caption { font-size: 13px; color: var(--text-sub); text-align: center; margin-top: 6px; }
    
    .cover-body { height: 100%; padding: 50px; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center; }
    .cover-title { font-size: 40px !important; font-weight: bold !important; color: var(--text-main) !important; line-height: 1.35 !important; margin-bottom: 20px !important; }
    .cover-media { height: 440px; border: 1px solid var(--border-gray); border-radius: 6px; overflow: hidden; }
    .cover-media img { width: 100%; height: 100%; object-fit: cover; display: block; }
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Slide 1: Cover -->
      <section>
        <div class="cover-body">
          <div class="cover-content">
            <div>
              <div style="color: var(--corporate-blue); font-size: 18px; font-weight: bold; letter-spacing: 0.05em; margin-bottom: 10px;">発表資料</div>
              <h1 class="cover-title">産業排水や水質汚濁と健康<br>知多の海と生活</h1>
            </div>
          </div>
          <div class="cover-media">
            <img src="''' + cover_img + '''" alt="知多の海">
          </div>
        </div>
      </section>

      <!-- Slide 2: 知多の環境と臨海工業 -->
      <section>
        <div class="standard-header">
          <h2>知多の環境と臨海工業</h2>
          <span class="header-meta">東海・半田・武豊</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">半島と二つの海</div>
              <div class="content-text">西＝伊勢湾、東＝三河湾（知多湾・衣浦湾）。南は伊良湖水道で太平洋へ。</div>
              <div class="content-heading">工場が並ぶ海岸</div>
              <div class="content-text">東海市＝日本製鉄名古屋製鉄所、半田・武豊＝衣浦港の臨海工業地帯、火力発電所・化学工場。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + steel_img + '''" alt="日本製鉄名古屋製鉄所">
              </div>
              <div class="simple-caption">日本製鉄名古屋製鉄所（東海市）</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 3: 調べたきっかけ -->
      <section>
        <div class="standard-header">
          <h2>調べたきっかけ</h2>
          <span class="header-meta">知多用水と昔の暮らし</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">知多用水の話</div>
              <div class="content-text">私の住んでいる知多は小学校の頃から毎年知多用水を手で掘り始めた話などをされて育ってきました。</div>
              <div class="content-heading">昔と今の変化</div>
              <div class="content-text">昔と今ではかなり変わったという話も聞いたのでインターネットで調べてみました。</div>
              <div class="content-heading">昔の生活環境</div>
              <div class="content-text">昔は川に垂れ流しや井戸から水を取ることもしていて、バキュームカーなども使われていました。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + canal_img + '''" alt="知多用水">
              </div>
              <div class="simple-caption">知多用水の風景</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 4: 愛知県の海の特徴 -->
      <section>
        <div class="standard-header">
          <h2>愛知県の海の特徴</h2>
          <span class="header-meta">伊勢湾と三河湾</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">浅くて汚れやすい海</div>
              <div class="content-text">伊勢湾の深さは19.5メートル、三河湾は約9メートルと浅く、両方とも海水の入れ替わりが少なく汚れがたまりやすい海です。</div>
              <div class="content-heading">排水の影響</div>
              <div class="content-text">工場や家庭の排水に洗剤などを流すと他の海と比べて、魚や貝が死ぬことがあります。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + map_img + '''" alt="伊勢湾・三河湾の地図">
              </div>
              <div class="simple-caption">伊勢湾と三河湾の地図</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 5: 水質汚濁防止法と規制 -->
      <section>
        <div class="standard-header">
          <h2>水質汚濁防止法と規制</h2>
          <span class="header-meta">工場排水のルール</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">1970年公布・1971年施行</div>
              <div class="content-text">1970年公布、1971年施行の水質汚濁防止法により、工場排水のルールが決められました。</div>
              <div class="content-heading">1980年〜</div>
              <div class="content-text">1980年から汚れを減らす総量削減の取り組みが始まりました。</div>
              <div class="content-heading">1995年</div>
              <div class="content-text">1995年には、海域における窒素およびリンに係る環境基準が設定されました。</div>
              <div class="content-heading">2002年〜</div>
              <div class="content-text">2002年からは、窒素およびリンを対象とした総量削減が始まりました。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + reg_img + '''" alt="規制の流れ">
              </div>
              <div class="simple-caption">水質規制の流れ</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 6: 規制の成果と貧栄養化 -->
      <section>
        <div class="standard-header">
          <h2>規制の成果と貧栄養化</h2>
          <span class="header-meta">ノリ・アサリ・イカナゴの減少</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">きれいになった海の課題</div>
              <div class="content-text">規制で海はきれいになりましたが、今度は栄養が足りない貧栄養化が起き、ノリやアサリ、イカナゴが減りました。</div>
              <div class="content-heading">2022年度からの実験</div>
              <div class="content-text">三河湾では2022年度から、下水浄化センター2か所の放流水の窒素・リンを国の上限まで戻す社会実験が始まっています。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + nori_img + '''" alt="ノリ養殖">
              </div>
              <div class="simple-caption">ノリやアサリへの影響</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 7: これからの取り組み -->
      <section>
        <div class="standard-header">
          <h2>これからの取り組み</h2>
          <span class="header-meta">両立と家庭での意識</span>
        </div>
        <div class="slide-body">
          <div class="two-column no-image">
            <div>
              <div class="content-heading">両立が必要</div>
              <div class="content-text">汚さないことと、豊かな海を守ることの両立が必要です。</div>
              <div class="content-heading">家庭で気をつけること</div>
              <div class="content-text">工場のルールを守ることに加え、台所の油や洗剤、食べ残しなど、家庭の排水に気をつけることが今は大切です。</div>
              <div class="content-heading">昔と今の変化</div>
              <div class="content-text">昔はまもられていなくて川への垂れ流しや井戸水、バキュームカーの時代でしたが、現在は改善が進んでいます。</div>
            </div>
            <div>
              <div class="media-box"></div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/5.1.0/reveal.min.js"></script>
  <script>
    Reveal.initialize({
      hash: true,
      slideNumber: 'c/t',
      transition: 'fade'
    });

    document.addEventListener('DOMContentLoaded', function() {
      document.querySelectorAll('.two-column').forEach(function(col) {
        var img = col.querySelector('.media-box img');
        if (!img || !img.getAttribute('src') || img.getAttribute('src').trim() === '' || img.src === window.location.href) {
          col.classList.add('no-image');
          var mediaBox = col.querySelector('.media-box');
          if (mediaBox) mediaBox.style.display = 'none';
        }
      });
    });
  </script>
</body>
</html>
'''

with open(r'C:\Users\shieru_k\2026-Hoken\suishitsu-odaku-chita.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated 7-slide suishitsu-odaku-chita.html successfully')
