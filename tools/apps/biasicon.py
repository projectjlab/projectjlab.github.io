SLUG = 'biasicon'
PKG = 'com.offsong.wjsn_wallpaper'
CATEGORY = 'PersonalizationApplication'
SHOT_HAS_TEXT = True
THEME = dict(
    theme_color='#5b64fb', hero_bg='#5b64fb', hero_fg='#ffffff', hero_sub='rgba(255,255,255,.9)',
    hero_em='color:#ffd84d', btn_bg='#5b64fb', btn_fg='#ffffff', hero_btn_bg='#ffffff', hero_btn_fg='#5b64fb',
    accent='#5b64fb', card='#f4f5ff', line='#e3e5f3', text='#14152b', sub='#5e6178',
    kicker_css='color:#5b64fb;font-size:15px;font-weight:800',
    card_mark='content:"\\2605";color:#ffc928;margin-right:8px',
    extra_css='.sky .meaning{color:#ffd84d;opacity:1}',
)

DEMO_CSS = r'''
.try{padding:72px 0 24px;text-align:center}
.try h2{font-size:clamp(26px,4vw,34px);font-weight:800;line-height:1.35}
.try h2 b{color:#5b64fb}
.try .hint{color:#5e6178;font-size:15px;margin:8px 0 28px}
.demo{display:grid;grid-template-columns:minmax(260px,320px) minmax(260px,420px);gap:32px;justify-content:center;align-items:start;text-align:left}
.phone{background:#111;border-radius:42px;padding:12px;box-shadow:0 20px 50px rgba(20,20,80,.25)}
.screen{border-radius:32px;min-height:520px;padding:44px 18px 24px;background:linear-gradient(160deg,#2b2f6b 0%,#5b64fb 55%,#ff9ec4 100%);position:relative}
.screen .clock{color:#fff;text-align:center;font-size:44px;font-weight:300;letter-spacing:-1px}
.screen .date{color:rgba(255,255,255,.85);text-align:center;font-size:13px;margin-bottom:34px}
.home{display:grid;grid-template-columns:repeat(4,1fr);gap:20px 10px}
.app{display:flex;flex-direction:column;align-items:center;gap:6px;background:none;border:0;padding:0;cursor:pointer;font:inherit}
.app .ic{width:56px;height:56px;border-radius:16px;display:grid;place-items:center;background-size:cover;background-position:center;box-shadow:0 4px 12px rgba(0,0,0,.18);transition:transform .25s cubic-bezier(.2,1.4,.4,1)}
.app .ic svg{width:28px;height:28px;fill:#fff}
.app.photo .ic svg{display:none}
.app.pop .ic{transform:scale(1.15)}
.app .nm{color:#fff;font-size:11px;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,.4);max-width:66px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;outline:none;border-radius:4px}
.app .nm[contenteditable="true"]{background:rgba(255,255,255,.25)}
.picker h3{font-size:16px;font-weight:800;margin-bottom:10px}
.photos{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.ph{aspect-ratio:1;border-radius:14px;border:3px solid transparent;background-size:cover;background-position:center;cursor:pointer;padding:0}
.ph.sel{border-color:#5b64fb;box-shadow:0 0 0 3px #fff inset}
.ph.up{background:#f4f5ff;border:2px dashed #b9bdf5;color:#5b64fb;font-size:12px;font-weight:700;display:grid;place-items:center;line-height:1.2}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.tools button{border:1px solid #e3e5f3;background:#fff;border-radius:999px;padding:9px 16px;font:inherit;font-size:14px;font-weight:700;cursor:pointer}
.tools button.main{background:#5b64fb;border-color:#5b64fb;color:#fff}
.steps{margin-top:18px;color:#5e6178;font-size:14px;line-height:1.8}
.steps b{color:#14152b}
@media (max-width:760px){.demo{grid-template-columns:1fr;justify-items:center}.picker{width:100%;max-width:420px}}
@media (prefers-reduced-motion:reduce){.app .ic{transition:none}}
'''
THEME['extra_css'] += DEMO_CSS

ICONS = {
    'phone': '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z"/>',
    'msg': '<path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8l-4 4V6a2 2 0 0 1 2-2Z"/>',
    'cam': '<path d="M9 4 7.2 6H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-3.2L15 4H9Zm3 4.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Z"/>',
    'gal': '<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Zm1 13h14l-4.5-6-3.5 4.5-2.5-3L5 17Z"/>',
    'cal': '<path d="M7 2v2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-2V2h-2v2H9V2H7Zm-2 8h14v10H5V10Z"/>',
    'music': '<path d="M9 18a3 3 0 1 1-2-2.8V5l12-2v11a3 3 0 1 1-2-2.8V6.3L9 7.6V18Z"/>',
    'map': '<path d="M12 2a7 7 0 0 1 7 7c0 5.2-7 13-7 13S5 14.2 5 9a7 7 0 0 1 7-7Zm0 4.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5Z"/>',
    'set': '<path d="m19.4 13 .1-1-.1-1 2.1-1.6-2-3.5-2.5 1a7.4 7.4 0 0 0-1.7-1L15 3h-4l-.4 2.6c-.6.3-1.2.6-1.7 1l-2.5-1-2 3.5L6.5 11l-.1 1 .1 1-2.1 1.6 2 3.5 2.5-1c.5.4 1.1.7 1.7 1L11 21h4l.4-2.6c.6-.3 1.2-.6 1.7-1l2.5 1 2-3.5-2.2-1.9ZM13 15.5a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z"/>',
}
COLORS = {'phone': '#34c759', 'msg': '#ffcc00', 'cam': '#5c6670', 'gal': '#ff6b8a', 'cal': '#ff3b30', 'music': '#af52de', 'map': '#2d9cdb', 'set': '#8e8e93'}


def demo(t):
    apps = ''.join(
        f'<button class="app" type="button" data-k="{k}"><span class="ic" style="background-color:{COLORS[k]}">'
        f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[k]}</svg></span><span class="nm">{nm}</span></button>'
        for k, nm in zip(ICONS, t['names']))
    img = 'img/demo/' if t['lang'] == 'ko' else '../img/demo/'
    photos = ''.join(f'<button class="ph" type="button" style="background-image:url({img}p{i}.webp)" aria-label="{t["photo"]} {i}"></button>' for i in range(1, 11))
    return f'''  <section class="try">
    <div class="wrap">
      <h2>{t['title']}</h2>
      <p class="hint">{t['hint']}</p>
      <div class="demo">
        <div class="phone"><div class="screen">
          <div class="clock" id="clk">9:41</div><div class="date">{t['date']}</div>
          <div class="home" id="home">{apps}</div>
        </div></div>
        <div class="picker">
          <h3>{t['pick']}</h3>
          <div class="photos" id="photos">{photos}<label class="ph up">{t['mine']}<input type="file" accept="image/*" id="up" hidden></label></div>
          <div class="tools">
            <button type="button" class="main" id="shuffle">{t['shuffle']}</button>
            <button type="button" id="rename">{t['rename']}</button>
            <button type="button" id="reset">{t['reset']}</button>
          </div>
          <p class="steps">{t['steps']}</p>
        </div>
      </div>
    </div>
  </section>
<script>
(function(){{
  var apps=[].slice.call(document.querySelectorAll('#home .app')),phs=[].slice.call(document.querySelectorAll('#photos .ph:not(.up)')),sel=null,editing=false;
  var names=apps.map(function(a){{return a.querySelector('.nm').textContent}});
  function pick(p){{phs.forEach(function(x){{x.classList.remove('sel')}});p.classList.add('sel');sel=p.style.backgroundImage;}}
  function apply(a,bg){{var ic=a.querySelector('.ic');ic.style.backgroundImage=bg;a.classList.add('photo','pop');setTimeout(function(){{a.classList.remove('pop')}},260);}}
  phs.forEach(function(p){{p.addEventListener('click',function(){{pick(p)}})}});
  pick(phs[0]);
  apps.forEach(function(a){{a.addEventListener('click',function(){{if(editing)return;if(sel)apply(a,sel);}})}});
  document.getElementById('shuffle').onclick=function(){{apps.forEach(function(a,i){{setTimeout(function(){{apply(a,phs[Math.floor(Math.random()*phs.length)].style.backgroundImage)}},i*70)}})}};
  document.getElementById('reset').onclick=function(){{apps.forEach(function(a,i){{var ic=a.querySelector('.ic');ic.style.backgroundImage='';a.classList.remove('photo');a.querySelector('.nm').textContent=names[i]}})}};
  var rb=document.getElementById('rename');
  rb.onclick=function(){{editing=!editing;apps.forEach(function(a){{var n=a.querySelector('.nm');n.contentEditable=editing;}});rb.textContent=editing?'{t['done']}':'{t['rename']}';if(editing)apps[0].querySelector('.nm').focus();}};
  apps.forEach(function(a){{a.querySelector('.nm').addEventListener('keydown',function(e){{if(e.key==='Enter'){{e.preventDefault();this.blur()}}}})}});
  document.getElementById('up').addEventListener('change',function(e){{var f=e.target.files[0];if(!f)return;var r=new FileReader();r.onload=function(){{var b=document.createElement('button');b.type='button';b.className='ph';b.style.backgroundImage='url('+r.result+')';var up=document.querySelector('#photos .up');up.parentNode.insertBefore(b,up);phs.push(b);b.addEventListener('click',function(){{pick(b)}});pick(b);}};r.readAsDataURL(f);}});
  var c=document.getElementById('clk');function tick(){{var d=new Date();c.textContent=d.getHours()+':'+('0'+d.getMinutes()).slice(-2)}}tick();setInterval(tick,30000);
}})();
</script>
'''


L = {
'ko': dict(name='최애콘 - 최애 아이콘 꾸미기 &amp; 홈화면 테마', brand='최애콘',
 title='최애콘 - 최애 아이콘 꾸미기 앱 | 아이돌 앱 아이콘 바꾸기, 홈화면 테마',
 desc='앱 아이콘을 좋아하는 아이돌 사진으로 바꿔 주는 아이콘 꾸미기 앱. 보이그룹·걸그룹 최애를 고르고 한번에 꾸미기, 아이콘 이름 변경, 알림 배지까지. 홈 화면을 최애로 가득 채워 보세요.',
 kw='최애콘, 아이콘 꾸미기, 앱 아이콘 바꾸기, 아이돌 아이콘, 케이팝 아이콘, 홈화면 꾸미기, 홈화면 테마, 아이콘 팩, 최애 배경화면',
 ogt='최애콘 - 최애 사진으로 앱 아이콘 꾸미기', ogd='최애 사진으로 앱 아이콘을 바꾸고 홈 화면을 꾸며 보세요. 한번에 꾸미기, 이름 변경, 알림 배지까지.',
 h1='최애 사진으로<br><b>앱 아이콘 꾸미기</b>', meaning='내 홈 화면을 최애로 가득',
 lead='좋아하는 그룹을 고르고, 앱을 누르고, 사진만 고르면 끝.<br>랜덤 버튼 한 번으로 모든 아이콘을 한꺼번에 채울 수도 있어요.',
 install='Google Play에서 무료로 받기', short='설치', heroalt='최애콘 최애 고르기와 내 앱 아이콘 꾸미기 화면',
 feats=[('최애부터 골라요', '', '보이그룹·걸그룹 중 좋아하는 그룹을 고르는 화면'),
        ('한번에 꾸미기', '', '여러 앱 아이콘을 아이돌 사진으로 한번에 바꾸는 화면'),
        ('진짜 홈 화면에 쏙', '', '최애 사진 아이콘으로 꾸민 실제 홈 화면')],
 st='<b>최애콘</b>으로 이렇게 꾸며요',
 cards=[('최애부터 골라요', '보이그룹·걸그룹 중 좋아하는 그룹을 여러 개 골라요. 목록에 없는 그룹은 직접 입력하면 많이 찾는 그룹부터 추가돼요.'),
        ('한번에 꾸미기', '다음 앱으로 자동으로 넘어가서 여러 아이콘을 빠르게 바꿔요. 실행 취소·다시 실행도 돼요.'),
        ('내 사진으로도 OK', '앨범에서 고르거나 카메라로 바로 찍어서 아이콘으로 만들 수 있어요.'),
        ('아이콘 이름도 내 마음대로', '"전화" 대신 최애 이름으로. 언제든 기본값으로 되돌릴 수 있어요.'),
        ('알림 배지도 그대로', '꾸민 아이콘에도 카톡 같은 앱의 알림 개수를 표시할 수 있어요(선택).')],
 st2='<b>이런 분께</b> 추천해요',
 whom=['홈 화면을 최애로 꾸미고 싶은 케이팝 팬', '아이콘 하나하나 바꾸기 번거로웠던 분', '홈 화면 테마·아이콘 팩을 찾던 분'],
 foot='최애콘은 팬이 만든 비공식 앱이며, 아티스트 및 소속사와 관련이 없어요. 아이콘 적용 시 홈 앱의 추가 확인 창이 표시될 수 있어요.',
 cta='오늘부터 홈 화면은<br>최애로 가득'),
'en': dict(name='Bias Icon - Kpop Icon Changer', brand='Bias Icon',
 title='Bias Icon - Kpop Icon Changer | Idol App Icons &amp; Aesthetic Home Screen Themes',
 desc='A K-pop icon changer that turns your app icons into photos of your favorite idols. Pick your bias, decorate every icon in one go, rename icons and keep notification badges.',
 kw='kpop icon changer, kpop icons, idol app icons, bias icon, icon changer, home screen theme, aesthetic icons, kpop icon pack',
 ogt='Bias Icon - Make your app icons all about your bias', ogd='Turn your app icons into your bias. Kpop icon changer &amp; home screen themes.',
 h1='Make your app icons<br><b>all about your bias</b>', meaning='Fill your home screen with your bias',
 lead='Pick your groups, tap an app, choose a photo &mdash; done.<br>Hit shuffle to fill every icon at once.',
 install='Get it on Google Play', short='Install', heroalt='Bias Icon group picker and app icon editor',
 feats=[('Pick your bias first', '', 'Choosing boy groups and girl groups'),
        ('Decorate in one go', '', 'Changing many app icons to idol photos at once'),
        ('Right on your home screen', '', 'A real home screen decorated with idol icons')],
 st='Decorate with <b>Bias Icon</b>',
 cards=[('Pick your bias first', 'Choose boy groups and girl groups. Can&rsquo;t find yours? Type it in and we&rsquo;ll add the most requested groups.'),
        ('Decorate in one go', 'Jumps to the next app automatically, with undo and redo.'),
        ('Use your own photos', 'Choose from your gallery or take a photo with the camera.'),
        ('Rename your icons', 'Swap &ldquo;Phone&rdquo; for your bias&rsquo;s name. Reset anytime.'),
        ('Notification badges', 'Show notification counts on your custom icons too (optional).')],
 st2='<b>Made</b> for',
 whom=['K-pop fans who want a bias-themed home screen', 'Anyone tired of changing icons one by one', 'Fans looking for kpop icon packs and aesthetic themes'],
 foot='Bias Icon is an unofficial fan-made app and is not affiliated with any artist or agency. Your home app may ask you to confirm when adding icons.',
 cta='Your home screen,<br>all about your bias'),
}

L['ko']['custom'] = demo(dict(lang='ko', title='지금 바로 <b>꾸며 볼까요?</b>', hint='사진을 고르고 아이콘을 눌러 보세요. 내 사진도 넣어 볼 수 있어요.',
    names=['전화', '메시지', '카메라', '갤러리', '캘린더', '음악', '지도', '설정'], date='오늘도 최애와 함께',
    pick='사진 고르기', photo='사진', mine='+<br>내 사진', shuffle='랜덤으로 채우기', rename='이름 바꾸기', done='완료', reset='처음으로',
    steps='<b>1.</b> 오른쪽에서 사진을 골라요<br><b>2.</b> 홈 화면의 아이콘을 누르면 바로 바뀌어요<br><b>3.</b> 이름 바꾸기를 누르고 아이콘 이름도 바꿔 보세요<br>※ 내 사진은 이 브라우저 안에서만 쓰이고 어디에도 올라가지 않아요.'))
L['en']['custom'] = demo(dict(lang='en', title='Try it <b>right now</b>', hint='Pick a photo, then tap an icon. You can add your own photo too.',
    names=['Phone', 'Messages', 'Camera', 'Gallery', 'Calendar', 'Music', 'Maps', 'Settings'], date='Another day with my bias',
    pick='Pick a photo', photo='Photo', mine='+<br>My photo', shuffle='Shuffle all', rename='Rename', done='Done', reset='Reset',
    steps='<b>1.</b> Pick a photo on the right<br><b>2.</b> Tap any icon on the home screen to change it<br><b>3.</b> Tap Rename to edit icon names<br>* Your photo stays in this browser and is never uploaded.'))
