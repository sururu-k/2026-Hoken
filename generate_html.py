import base64
import os

def get_base64(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

cover_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\cover-chita.jpg')
canal_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\aichi-canal.jpg')
map_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\isebay_map.jpg')
reg_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\water_regulation.jpg')
nori_img = get_base64(r'C:\Users\shieru_k\2026-Hoken\img\nori.jpg')

html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>水質汚濁と健康 — 知多の海と生活の歴史</title>
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
              <h1 class="cover-title">水質汚濁と健康<br>知多の海と生活の歴史</h1>
            </div>
            <div style="font-size: 20px; color: var(--text-sub); font-weight: bold; border-top: 1px solid var(--border-gray); padding-top: 16px;">
              テーマ：産業排水・家庭排水と貧栄養化の課題
            </div>
          </div>
          <div class="cover-media">
            <img src="''' + cover_img + '''" alt="知多の海">
          </div>
        </div>
      </section>

      <!-- Slide 2: 身近な歴史 -->
      <section>
        <div class="standard-header">
          <h2>身近な歴史：知多用水と生活排水</h2>
          <span class="header-meta">手掘りの歴史から下水道整備へ</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">手掘りで拓いた水路</div>
              <div class="content-text">小学生の頃から、毎年知多用水を手で掘り起こして水を引いた先人の苦労を聞いて育つ。</div>
              <div class="content-heading">昔の排水環境</div>
              <div class="content-text">昔は川への垂れ流しや井戸水利用、バキュームカーなど、衛生や水質管理の課題が多かった。</div>
              <div class="content-heading">昔と今の変化を探る</div>
              <div class="content-text">現在は下水道整備が進んだが、昔と今で水環境や海がどう変化したのかを調査。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + canal_img + '''" alt="愛知用水">
              </div>
              <div class="simple-caption">知多用水・愛知用水の歴史</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 3: 伊勢湾・三河湾 -->
      <section>
        <div class="standard-header">
          <h2>汚れがたまりやすい二つの海</h2>
          <span class="header-meta">伊勢湾・三河湾の閉鎖性水域</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">水深と地形の特質</div>
              <div class="content-text">伊勢湾は平均水深19.5m、三河湾は約9mと浅い。湾口が狭く海水が入れ替わりにくい閉鎖性水域。</div>
              <div class="content-heading">汚濁のリスク</div>
              <div class="content-text">工場排水や家庭の洗剤・有機物が流入すると、赤潮や底層の酸欠（貧酸素水塊）が発生しやすい。</div>
              <div class="content-heading">漁業と健康への影響</div>
              <div class="content-text">酸素不足により魚や貝が死滅するなど、生態系や地域の食文化に直結する害が発生。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + map_img + '''" alt="伊勢湾・三河湾の地図">
              </div>
              <div class="simple-caption">伊勢湾・三河湾の位置と地形</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 4: 水質規制の歴史 -->
      <section>
        <div class="standard-header">
          <h2>水質規制の歴史</h2>
          <span class="header-meta">1970年代からの工場排水対策</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">水質汚濁防止法（1970公布 / 1971施行）</div>
              <div class="content-text">工場排水の基準やルールを全国的に明確化し、汚濁物質の排出を厳密に規制。</div>
              <div class="content-heading">総量削減の導入（1980年〜）</div>
              <div class="content-text">濃度規制だけでなく、地域全体で排出荷重の総量を減らす取組（COD規制）が開始。</div>
              <div class="content-heading">窒素・リンの環境基準（1995年 / 2002年）</div>
              <div class="content-text">1995年に富栄養化対策として基準が設定され、2002年より窒素・リンの総量削減が開始。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + reg_img + '''" alt="水質規制の歩み">
              </div>
              <div class="simple-caption">水質汚濁防止法と総量削減の変遷</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 5: 貧栄養化と社会実験 -->
      <section>
        <div class="standard-header">
          <h2>規制の成果と新たな課題</h2>
          <span class="header-meta">貧栄養化と2022年〜の社会実験</span>
        </div>
        <div class="slide-body">
          <div class="two-column">
            <div>
              <div class="content-heading">貧栄養化の発生</div>
              <div class="content-text">厳しい排水規制により海は綺麗になった一方、栄養塩（窒素・リン）が不足する事態へ。</div>
              <div class="content-heading">水産業への影響</div>
              <div class="content-text">栄養不足によってノリの色落ちが発生し、アサリやイカナゴの漁獲量が激減。</div>
              <div class="content-heading">2022年度〜 栄養塩戻し社会実験</div>
              <div class="content-text">三河湾では下水浄化センター2か所の放流水の窒素・リンを国の上限まで戻す試みを運用中。</div>
            </div>
            <div>
              <div class="media-box">
                <img src="''' + nori_img + '''" alt="ノリ養殖">
              </div>
              <div class="simple-caption">ノリ・アサリ等の漁獲減少と貧栄養化</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 6: 画像がない場合でも枠が出ない1カラムスライド -->
      <section>
        <div class="standard-header">
          <h2>豊かな海を守るために</h2>
          <span class="header-meta">「汚さないこと」と「豊かな海」の両立</span>
        </div>
        <div class="slide-body">
          <div class="two-column no-image">
            <div>
              <div class="content-heading">昔と今の環境変化</div>
              <div class="content-text">昔は川への垂れ流しやバキュームカー、井戸水利用などインフラが未整備だったが、現在は下水道や浄化施設が普及。</div>
              <div class="content-heading">家庭でできる排水対策</div>
              <div class="content-text">工場の規制遵守はもちろん、台所の油・洗剤・食べ残しを流さないなど、家庭での意識と実践が重要。</div>
              <div class="content-heading">適正なバランス管理</div>
              <div class="content-text">単に水を綺麗にするだけでなく、豊かな生態系を育む栄養バランスの保たれた水質管理が求められている。</div>
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

    // 画像がない場合や読み込み失敗時に枠を非表示にして1カラム化する自動JS
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

print('Generated suishitsu-odaku-chita.html successfully')
