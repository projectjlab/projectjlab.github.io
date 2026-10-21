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

BINGO_CSS = r'''
.play{padding:72px 0 40px;text-align:center}
.play h2{font-size:clamp(26px,4vw,34px);font-weight:800;line-height:1.35}
.play h2 b{background:linear-gradient(transparent 58%,#e6ff1f 58%)}
.play .hint{color:#5f6359;font-size:15px;margin:8px 0 28px}
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:420px;margin:0 auto}
.cell{aspect-ratio:1;border:2px dashed #c9ccc2;border-radius:14px;background:#fff;font:inherit;font-size:15px;font-weight:700;color:#111;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:8px;transition:transform .15s,background .2s,border-color .2s}
.cell:hover{transform:translateY(-2px)}
.cell .ck{width:22px;height:22px;border:2px solid #111;border-radius:6px;display:grid;place-items:center;font-size:14px;line-height:1;color:transparent}
.cell.on{background:#e6ff1f;border:2px solid #111;transform:rotate(-1.5deg)}
.cell.on:nth-child(even){transform:rotate(1.5deg)}
.cell.on .ck{background:#111;color:#e6ff1f}
.count{margin-top:18px;font-weight:700;font-size:15px}
.count i{font-style:normal;display:inline-block;min-width:1.2em}
.meet{display:none;max-width:340px;margin:28px auto 0;border:2px solid #111;border-radius:22px;padding:26px 22px;background:#fff;animation:pop .45s cubic-bezier(.2,1.4,.4,1)}
.meet.show{display:block}
.meet img{width:150px;height:auto;margin:10px auto 6px;display:block}
.meet b{font-size:18px}
.meet p{color:#5f6359;font-size:14px;margin:4px 0 14px}
.meet button{background:none;border:0;font:inherit;font-size:13px;color:#5f6359;text-decoration:underline;cursor:pointer;margin-top:10px}
@keyframes pop{from{opacity:0;transform:scale(.8) rotate(-4deg)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.meet{animation:none}.cell,.cell.on{transition:none;transform:none}}
'''
THEME['extra_css'] += BINGO_CSS


def bingo(missions, title, hint, left, done_title, nb_name, nb_desc, again, cta, img, store):
    cells = ''.join(f'<button class="cell" type="button" aria-pressed="false"><span class="ck">✓</span>{m}</button>' for m in missions)
    return f'''  <section class="play">
    <div class="wrap">
      <h2>{title}</h2>
      <p class="hint">{hint}</p>
      <div class="board" id="board">{cells}</div>
      <div class="count"><i id="cnt">0</i> / 9 {left}</div>
      <div class="meet" id="meet" role="status">
        <b>{done_title}</b>
        <img src="{img}" alt="{nb_name}" width="250" height="240">
        <b>{nb_name}</b>
        <p>{nb_desc}</p>
        <a class="btn" href="{store}">{cta}</a><br>
        <button type="button" id="again">{again}</button>
      </div>
    </div>
  </section>
<script>
(function(){{
  var cells=[].slice.call(document.querySelectorAll('#board .cell')),cnt=document.getElementById('cnt'),meet=document.getElementById('meet');
  function upd(){{var n=cells.filter(function(c){{return c.classList.contains('on')}}).length;cnt.textContent=n;meet.classList.toggle('show',n===9);if(n===9)meet.scrollIntoView({{behavior:'smooth',block:'center'}});}}
  cells.forEach(function(c){{c.addEventListener('click',function(){{c.classList.toggle('on');c.setAttribute('aria-pressed',c.classList.contains('on'));upd();}});}});
  document.getElementById('again').onclick=function(){{cells.forEach(function(c){{c.classList.remove('on');c.setAttribute('aria-pressed','false')}});upd();document.getElementById('board').scrollIntoView({{behavior:'smooth',block:'center'}});}};
}})();
</script>
'''


L['ko']['custom'] = bingo(
    ['구름 모양', '웃는 사람', '빨간 물건 셋', '새소리', '문 잡아주기', '작은 꽃', '반려동물 산책', '오래된 건물', '두 가지 소리'],
    '여기서 먼저 <b>한 판</b> 해 볼까요?', '지금 주변을 둘러보고, 찾은 칸을 눌러 보세요.', '칸 발견',
    '새로운 이웃을 발견했어요!', '학원 가방 멘 학생', '가방이 몸보다 커 보인다. 그래도 간식 이야기를 할 때는 눈이 반짝인다.',
    '다시 하기', '앱에서 매일 새 빙고 받기', 'img/neighbor.webp',
    'https://play.google.com/store/apps/details?id=com.offsong.today_discovery&hl=ko')
L['en']['custom'] = bingo(
    ['Cloud Shapes', 'A Smile', 'Three Red Things', 'Birdsong', 'Holding the Door', 'Tiny Flower', 'Pet on a Walk', 'Old Building', 'Two Sounds'],
    'Try <b>one board</b> right here', 'Look around you now, and tap each thing you find.', 'found',
    'You discovered a new neighbor!', 'Student with a Big Backpack', 'The backpack looks bigger than they are. Eyes light up when snacks come up.',
    'Play again', 'Get a new board every day', '../img/neighbor.webp',
    'https://play.google.com/store/apps/details?id=com.offsong.today_discovery&hl=en')
