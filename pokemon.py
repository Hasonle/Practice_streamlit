import streamlit as st
#06.09#

st.set_page_config( page_title= '포켓몬 도감',
                   page_icon='images\monsterball.png')
#css
st.markdown('''
<style>
img {max-height: 300px;}
.st-emotion-cache-1clstc5 div{
        display: flex;
        justify-content: center;
        font_size: 20px;    }
 [data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
</style>
''',unsafe_allow_html=True)

st.title('streamlit 포켓몬 도감')
st.markdown('**포켓몬**을 하나씩 추가해서 도감을 채워보세요!')

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
    {
        "name": "00년생 김지영",
        "types": ["얼음"],
        "image_url": "./images/jiyoung.jpg"
    },
    {
        "name": "엄준식",
        "types": ["노말"],
        "image_url": "./images/um.jpg"},
    {
        "name": "김춘배",
        "types": ["땅"],
        "image_url": "./images/jung.jpg"}
]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

#st.session_state
if 'pokemons' not in st.session_state:
     st.session_state.pokemons= initial_pokemons

#st.toggle

auto_complete= st.toggle('예시 데이터로 채우기')


#st.form#
with st.form(key='form'):
    col1,col2= st.columns(2)
    auto_complete=True
    with col1:
        name= st.text_input(
            label= '포켓몬 이름',
            value= example_pokemon['name'] if auto_complete else'')
    with col2:
        types= st.multiselect(
            label='포켓몬 속성',
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default= example_pokemon['types'] if auto_complete else[])
    image_url= st.text_input(
            label= '포켓몬 이미지 URL',
            value= example_pokemon['image_url'] if auto_complete else '')
    submit= st.form_submit_button(label='Submit')
    
    if submit:
        if not name:
            st.error('포켓몬의 이름을 입력해주세요.')
        elif len(types)== 0:
            st.error('포켓몬의 속성을 적어도 한개 선택해주세요.')
        else:
            st.success('포켓몬을 추가할 수 있습니다.')
            st.session_state.pokemons.append({
                'name':name,
                'types':types,
                'image_url': image_url if image_url else"./images/default.png"
            })

#st.session_State#


#여러 포켓몬 columns 사용

for i in range(0,len(st.session_state.pokemons),3):
    row_pokemons= st.session_state.pokemons[i:i+3]
    cols= st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j] :
            pokemon= row_pokemons[j]
            with st.expander(label=f"**{j+i+1}. {pokemon['name']}**",expanded=True):
                st.text(pokemon['name'])
                st.image(pokemon['image_url'])
                emoji_types=[f'{type_emoji_dict[x]} {x}' for x in pokemon['types']]
                st.text(' / '.join(emoji_types))
                delete_button = st.button(label='삭제', key=i+j,use_container_width=True) #데이터 삭제
                if delete_button:
                    print('delete button clicked!')
                    del st.session_state.pokemons[i+j]
                    st.rerun()
