import streamlit as st

st.set_page_config(page_title="자기소개 앱", page_icon="👋")

page = st.sidebar.selectbox(
    "페이지 선택",
    ["홈", "자기소개"]
)

if page == "홈":
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    st.info("왼쪽 사이드바에서 '자기소개' 페이지를 선택하면 자기소개 템플릿을 볼 수 있어요.")
else:
    st.title("👋 자기소개")
    st.markdown("#### 안녕하세요!\n\n여기에 간단한 자기소개를 작성해보세요.")

    st.subheader("기본 정보")
    st.markdown(
        "- 이름: **김수경**\n"
        "- 직업 / 역할: **대학생**\n"
        "- 나이: **20**\n"
    )

    st.subheader("소개 문구")
    st.write(
        "안녕하세요! 저는 김수경입니다. 만나서 반가워유~~~~."
    )

    st.subheader("추가 정보")
    st.markdown(
        "- 이번주 목표: **마라탕 먹기**\n"
        "- 이번달 목표: **마라탕 조금 먹기**\n"
    )
    st.image(
        "https://images.unsplash.com/photo-1582388673400-38c4d407e5c6?auto=format&fit=crop&w=812&q=80",
        caption="마라탕 사진",
        use_column_width=True,
    )

    st.caption("이 부분은 나중에 자유롭게 수정하시면 됩니다.")
