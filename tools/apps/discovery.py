SLUG = 'discovery'
PKG = 'com.offsong.today_discovery'
CATEGORY = 'LifestyleApplication'
THEME = dict(
    theme_color='#ffffff', hero_bg='#ffffff', hero_fg='#111111', hero_sub='#555555',
    hero_em='background:linear-gradient(transparent 58%,#e6ff1f 58%)',
    btn_bg='#111111', btn_fg='#e6ff1f', hero_btn_bg='#111111', hero_btn_fg='#e6ff1f',
    accent='#111111', card='#f6f7f2', line='#e6e8df', text='#111111', sub='#5f6359',
    kicker_css='display:inline-block;background:#111;color:#e6ff1f;font-size:13px;font-weight:800;padding:4px 14px;border-radius:999px',
    card_mark='content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:#e6ff1f;border:2px solid #111;margin-right:10px;vertical-align:1px',
    extra_css='.sec-title b{background:linear-gradient(transparent 58%,#e6ff1f 58%);color:inherit}.cta.sky{background:#e6ff1f}.whom li::before{background:#e6ff1f;border:2px solid #111}',
)
L = {
'ko': dict(name='오늘의 발견: 폰 내려놓고 찾아보는 관찰 빙고', brand='오늘의 발견',
 title='오늘의 발견 - 폰 내려놓기 관찰 빙고 앱 | 스마트폰 사용 줄이기, 마음챙김 산책',
 desc='잠시 폰을 내려놓고 주변을 발견해 보세요. 매일 새로 열리는 3×3 관찰 빙고로 구름 모양, 새소리, 작은 꽃을 찾고, 빙고를 완성하면 손그림 동네 이웃을 만나요. 스마트폰 사용 줄이기를 가볍게 시작하세요.',
 kw='폰 내려놓기, 스마트폰 사용 줄이기, 디지털 디톡스, 관찰 빙고, 마음챙김 산책, 산책 앱, 일상 기록, 빙고 게임, 습관 앱',
 ogt='오늘의 발견 - 폰 내려놓고 찾아보는 관찰 빙고', ogd='폰을 잠시 내려놓고 주변을 관찰하고, 매일 작은 발견으로 빙고를 완성하고 손그림 동네 이웃을 모아보세요.',
 h1='잠시 폰을 내려놓고<br><b>주변을 발견</b>해 보세요', meaning='매일 새로 열리는 3×3 관찰 빙고',
 lead='구름 모양, 새소리, 빨간 물건 셋, 작은 꽃, 내 그림자.<br>쉬운 미션을 찾다 보면 자연스럽게 고개를 들게 돼요.<br>하루 몇 분이면 충분해요.',
 install='Google Play에서 무료로 받기', short='설치', heroalt='오늘의 관찰 빙고판과 미션 확인 화면',
 feats=[('새로운 이웃', '빙고를 완성하고<br>동네 이웃을 만나요', '빙고를 완성해 새로운 이웃을 만난 화면'),
        ('이웃 도감', '한 명씩 만나 모으는<br>우리 동네 이웃들', '52명의 손그림 이웃이 모이는 동네 이웃 도감'),
        ('발견의 달력', '하루하루 쌓인 발견을<br>달력에서 돌아봐요', '날짜별 진행도가 표시된 발견 캘린더')],
 st='<b>작은 발견</b>이 쌓이는 방법',
 cards=[('매일 새 3×3 빙고', '사람과 행동, 자연과 풍경, 거리와 사물, 소리와 감각, 작은 친절까지 다섯 가지 주제의 미션 300개가 돌아가며 나와요.'),
        ('발견했어요!', '칸을 누르면 따뜻한 한 줄 설명이 나와요. 주변에서 찾으면 [발견했어요!]로 기록해요.'),
        ('손그림 동네 이웃', '아홉 칸을 채우면 복덕방 김씨 아저씨, 앞니 빠진 꼬마처럼 개성 있는 이웃 52명을 하나씩 만나요.'),
        ('내 속도대로', '못 끝낸 판은 사라지지 않아요. 발견 캘린더에서 지난 날짜를 골라 나중에 채울 수 있어요.'),
        ('홈 화면 위젯', '이번 주 진행 상황을 홈 화면 위젯에서 한눈에 확인해요.'),
        ('가볍고 간편하게', '로그인도, 사진 촬영도, 위치 정보도 필요 없어요. Google Drive 백업도 지원해요.')],
 st2='<b>이런 분께</b> 추천해요',
 whom=['폰 내려놓기 습관을 작고 즐거운 방식으로 시작하고 싶은 분', '스마트폰 사용 줄이기를 일상에서 가볍게 실천하고 싶은 분', '산책 중 주변을 관찰하고 작은 발견을 남기고 싶은 분', '빙고와 손그림 이웃 도감을 좋아하는 분'],
 cta='오늘의 작은 장면,<br>발견해 보세요'),
'en': dict(name='Today’s Discovery: Daily Bingo', brand='Today’s Discovery',
 title='Today’s Discovery - Phone Break Observation Bingo | Mindful Walk &amp; Screen Time App',
 desc='Take a phone break and notice what’s around you. A fresh 3×3 observation bingo every day: spot a cloud shape, hear a bird, find a tiny flower, then meet a hand-drawn neighbor when you finish.',
 kw='phone break, reduce screen time, digital detox, observation bingo, mindful walk, daily bingo, habit app, mindfulness',
 ogt='Today’s Discovery - Take a phone break with daily bingo', ogd='Take a phone break with daily bingo: look up, spot small things, meet neighbors.',
 h1='Set your phone down.<br><b>Notice what’s around you.</b>', meaning='A fresh 3×3 observation bingo every day',
 lead='A cloud shape, a bird song, three red things, a tiny flower.<br>Small, easy missions that help you look up &mdash;<br>a few minutes a day is enough.',
 install='Get it on Google Play', short='Install', heroalt='Today’s observation bingo board and a mission card',
 feats=[('Meet a neighbor', 'Finish your bingo<br>Say hello to someone new', 'Meeting a new neighbor after finishing the bingo'),
        ('Your neighborhood book', 'Meet them one by one<br>Collect all 52 neighbors', 'Neighbor book with 52 hand-drawn characters'),
        ('Your discovery calendar', 'Little moments add up<br>Look back day by day', 'Monthly discovery calendar with progress circles')],
 st='How <b>small discoveries</b> add up',
 cards=[('A fresh 3×3 board', '300 missions across five themes: people, nature, streets, sounds and small kindness.'),
        ('I found it!', 'Tap a square to read a warm prompt, then mark it when you spot it in real life.'),
        ('Hand-drawn neighbors', 'Fill all nine squares to meet one of 52 neighbors, drawn in black-and-white line art.'),
        ('At your own pace', 'Unfinished boards stay. Return to any past day from the discovery calendar.'),
        ('Home screen widget', 'See this week’s progress circles at a glance.'),
        ('Simple and private', 'No login, photos or location needed. Optional Google Drive backup.')],
 st2='<b>Good</b> for you if you want to',
 whom=['Take a gentle phone break during the day', 'Make a mindful walk more playful', 'Practice noticing ordinary things', 'Collect hand-drawn characters one board at a time'],
 cta='Take a phone break,<br>find one small thing'),
}

SHOT_HAS_TEXT = True

BINGO_CSS = r"""
.play{padding:72px 0 40px;text-align:center}
.play h2{font-size:clamp(26px,4vw,34px);font-weight:800;line-height:1.35}
.play h2 b{background:linear-gradient(transparent 58%,#e6ff1f 58%)}
.play .hint{color:#5f6359;font-size:15px;margin:8px 0 28px}
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:420px;margin:0 auto}
.cell{aspect-ratio:1;border:2px dashed #c9ccc2;border-radius:14px;background:#fff;font:inherit;font-size:15px;font-weight:700;color:#111;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:8px;transition:transform .15s,background .2s,border-color .2s}
.cell:hover{transform:translateY(-2px);border-color:#111}
.cell .ck{width:22px;height:22px;border:2px solid #111;border-radius:6px;display:grid;place-items:center;font-size:14px;line-height:1;color:transparent}
.cell.on{background:#e6ff1f;border:2px solid #111;transform:rotate(-1.5deg)}
.cell.on:nth-child(even){transform:rotate(1.5deg)}
.cell.on .ck{background:#111;color:#e6ff1f}
.count{margin-top:18px;font-weight:700;font-size:15px}
.count i{font-style:normal;display:inline-block;min-width:1.2em}
.bwrap{position:relative;max-width:420px;margin:0 auto}
.dim{position:absolute;inset:-10px;border-radius:22px;background:rgba(17,17,17,.38);opacity:0;pointer-events:none;transition:opacity .2s;z-index:5}
.dim.show{opacity:1;pointer-events:auto}
.sheet{position:absolute;left:50%;top:50%;width:88%;transform:translate(-50%,-50%) scale(.85);opacity:0;pointer-events:none;background:#fff;border:2px solid #111;border-radius:22px;padding:24px 22px 18px;transition:transform .28s cubic-bezier(.2,1.3,.4,1),opacity .2s;z-index:6;text-align:left;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.sheet.show{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:auto}
.sheet .tag{display:inline-block;background:#111;color:#e6ff1f;font-size:12px;font-weight:800;padding:3px 10px;border-radius:999px;margin-bottom:10px}
.sheet h3{font-size:21px;font-weight:800;margin-bottom:6px}
.sheet p{color:#5f6359;font-size:15px;line-height:1.65;margin-bottom:18px}
.sheet .found{width:100%;background:#111;color:#fff;border:0;border-radius:14px;padding:14px;font:inherit;font-size:16px;font-weight:700;cursor:pointer}
.sheet .found.undo{background:#fff;color:#111;border:2px solid #111}
.sheet .close{display:block;margin:10px auto 0;background:none;border:0;font:inherit;font-size:14px;color:#5f6359;cursor:pointer}
.meet{display:none;max-width:340px;margin:28px auto 0;border:2px solid #111;border-radius:22px;padding:26px 22px;background:#fff;animation:pop .45s cubic-bezier(.2,1.4,.4,1)}
.meet.show{display:block}
.meet img{width:150px;height:auto;margin:10px auto 6px;display:block}
.meet b{font-size:18px}
.meet p{color:#5f6359;font-size:14px;margin:4px 0 14px}
.meet button{background:none;border:0;font:inherit;font-size:13px;color:#5f6359;text-decoration:underline;cursor:pointer;margin-top:10px}
@keyframes pop{from{opacity:0;transform:scale(.8) rotate(-4deg)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.meet{animation:none}.cell,.cell.on,.sheet,.dim{transition:none}.cell,.cell.on{transform:none}}
"""
THEME['extra_css'] += BINGO_CSS


def bingo(missions, t, img, store):
    import json
    cells = ''.join(f'<button class="cell" type="button" aria-haspopup="dialog"><span class="ck">✓</span>{m[0]}</button>' for m in missions)
    data = json.dumps([m[1] for m in missions], ensure_ascii=False)
    return f"""  <section class="play">
    <div class="wrap">
      <h2>{t['title']}</h2>
      <p class="hint">{t['hint']}</p>
      <div class="bwrap">
        <div class="board" id="board">{cells}</div>
        <div class="dim" id="dim"></div>
        <div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="shT">
          <span class="tag">{t['tag']}</span>
          <h3 id="shT"></h3>
          <p id="shD"></p>
          <button type="button" class="found" id="shB"></button>
          <button type="button" class="close" id="shC">{t['close']}</button>
        </div>
      </div>
      <div class="count"><i id="cnt">0</i> / 9 {t['left']}</div>
      <div class="meet" id="meet" role="status">
        <b>{t['done']}</b>
        <img src="{img}" alt="{t['nb']}" width="250" height="240">
        <b>{t['nb']}</b>
        <p>{t['nbd']}</p>
        <a class="btn" href="{store}">{t['cta']}</a><br>
        <button type="button" id="again">{t['again']}</button>
      </div>
    </div>
  </section>
<script>
(function(){{
  var D={data},FOUND="{t['found']}",UNDO="{t['undo']}";
  var cells=[].slice.call(document.querySelectorAll('#board .cell')),cnt=document.getElementById('cnt'),meet=document.getElementById('meet');
  var sheet=document.getElementById('sheet'),dim=document.getElementById('dim'),T=document.getElementById('shT'),P=document.getElementById('shD'),B=document.getElementById('shB'),cur=-1;
  function upd(){{var n=cells.filter(function(c){{return c.classList.contains('on')}}).length;cnt.textContent=n;var was=meet.classList.contains('show');meet.classList.toggle('show',n===9);if(n===9&&!was)setTimeout(function(){{meet.scrollIntoView({{behavior:'smooth',block:'center'}})}},320);}}
  function open(i){{cur=i;var on=cells[i].classList.contains('on');T.textContent=cells[i].textContent.replace('✓','');P.textContent=D[i];B.textContent=on?UNDO:FOUND;B.classList.toggle('undo',on);sheet.classList.add('show');dim.classList.add('show');B.focus({{preventScroll:true}});}}
  function close(){{sheet.classList.remove('show');dim.classList.remove('show');if(cur>-1)cells[cur].focus({{preventScroll:true}});cur=-1;}}
  cells.forEach(function(c,i){{c.addEventListener('click',function(){{open(i)}})}});
  B.onclick=function(){{if(cur<0)return;cells[cur].classList.toggle('on');upd();close();}};
  document.getElementById('shC').onclick=close;dim.onclick=close;
  document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&cur>-1)close();}});
  document.getElementById('again').onclick=function(){{cells.forEach(function(c){{c.classList.remove('on')}});upd();document.getElementById('board').scrollIntoView({{behavior:'smooth',block:'center'}});}};
}})();
</script>
"""


L['ko']['custom'] = bingo([
    ('구름 모양', '하늘을 올려다보고 무언가를 닮은 구름을 찾아보세요. 동물, 과자, 얼굴… 무엇으로 보이나요?'),
    ('웃는 사람', '주변에서 웃고 있는 사람을 찾아보세요. 미소 하나로도 하루가 조금 밝아져요.'),
    ('빨간 물건 셋', '빨간 물건 세 개를 찾아보세요. 생각보다 빨리 찾을지도 몰라요.'),
    ('새소리', '잠시 귀를 기울여 새소리를 들어 보세요. 어디쯤에서 들려오나요?'),
    ('문 잡아주기', '뒤에 오는 사람을 위해 문을 잡아 주거나, 누군가 잡아 준 문을 지나가 보세요.'),
    ('작은 꽃', '길가나 화단에 핀 작은 꽃을 찾아보세요. 이름을 몰라도 괜찮아요.'),
    ('반려동물 산책', '산책 중인 강아지나 반려동물을 찾아보세요. 꼬리가 어떻게 움직이나요?'),
    ('오래된 건물', '오래되어 보이는 건물이나 간판을 찾아보세요. 어떤 이야기가 있을까요?'),
    ('두 가지 소리', '눈을 감고 서로 다른 소리 두 가지를 찾아보세요. 바람, 발소리, 차 소리…'),
], dict(title='여기서 먼저 <b>한 판</b> 해 볼까요?', hint='칸을 눌러 미션을 확인하고, 주변에서 찾으면 [발견했어요!]를 눌러 보세요.', left='칸 발견',
        done='새로운 이웃을 발견했어요!', nb='학원 가방 멘 학생', nbd='가방이 몸보다 커 보인다. 그래도 간식 이야기를 할 때는 눈이 반짝인다.',
        again='다시 하기', cta='앱에서 매일 새 빙고 받기', found='발견했어요!', undo='체크 해제하기', close='닫기', tag='오늘의 미션'),
   'img/neighbor.webp', 'https://play.google.com/store/apps/details?id=com.offsong.today_discovery&hl=ko')
L['en']['custom'] = bingo([
    ('Cloud Shapes', 'Look up and find a cloud that looks like something. An animal, a snack, a face?'),
    ('A Smile', 'Spot someone smiling nearby. One smile can brighten the whole day.'),
    ('Three Red Things', 'Find three red things. It might be quicker than you think.'),
    ('Birdsong', 'Pause and listen for a bird. Where is the sound coming from?'),
    ('Holding the Door', 'Hold the door for someone behind you, or walk through one held for you.'),
    ('Tiny Flower', 'Find a small flower by the road or in a planter. No need to know its name.'),
    ('Pet on a Walk', 'Spot a dog or pet out for a walk. How is its tail moving?'),
    ('Old Building', 'Find a building or sign that looks old. What story might it have?'),
    ('Two Sounds', 'Close your eyes and pick out two different sounds. Wind, footsteps, traffic…'),
], dict(title='Try <b>one board</b> right here', hint='Tap a square to read the mission, then tap [I found it!] when you spot it.', left='found',
        done='You discovered a new neighbor!', nb='Student with a Big Backpack', nbd='The backpack looks bigger than they are. Eyes light up when snacks come up.',
        again='Play again', cta='Get a new board every day', found='I found it!', undo='Uncheck', close='Close', tag='Today’s mission'),
   '../img/neighbor.webp', 'https://play.google.com/store/apps/details?id=com.offsong.today_discovery&hl=en')
