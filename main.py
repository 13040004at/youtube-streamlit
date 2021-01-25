import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000)
# highlight_max(axis=0) = 列の中で最大なものをハイライトするmin(axis=1なら最小行)
# Pandasの機能
# st.table(df.style.highlight_max(axis=0)) static(静的)なテーブルを作りたい時に使用する。
# 「動的」なテーブルを使いたい時は dataframe()
# 詳しくは Streamlit公式ページの「Docs」→「REFERENCE GUIDES」→「API reference」→「Display data」
# 参照： https://docs.streamlit.io/en/stable/api.html#display-data


# マジックコマンド
# 詳しくは Streamlit公式ページの「Docs」→「REFERENCE GUIDES」→「API reference」→「Display text」
# 参照： https://docs.streamlit.io/en/stable/api.html#display-text
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# チャートを描画、マップをプロット
# 詳しくは Streamlit公式ページの「Docs」→「REFERENCE GUIDES」→「API reference」→「Display charts」
# 参照： https://docs.streamlit.io/en/stable/api.html#display-text
chart_data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)
st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [34.97, 137.04],
    columns=['lat','lon'] #longitude=緯度,latitude=経度
)
st.map(map_data)

# 画像を表示
# 詳しくは Streamlit公式ページの「Docs」→「REFERENCE GUIDES」→「API reference」→「Display media」
# 参照： https://docs.streamlit.io/en/stable/api.html#display-data

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') # プログレスバーの上のテキスト表示
    bar.progress(i + 1) # プログレスバーの表示
    time.sleep(0.1)

'Done!!!!!'

# 埋め込まれているチェックボックスにチェックを入れると「True」以下を処理。「False」ではなにもしない。
if st.checkbox('Show Image'):
    img = Image.open('kariya_office.jpg')
    st.image(img, caption='アルゴ株式会社 刈谷事業所', use_column_width=True)
# use_column_width=True → 実際のレイアウトの横幅に合わせて表示する

# セレクトボックスの埋め込み
option = st.selectbox(
    'あなたが好きな数字を教えてください、', 
    list(range(1, 11))
)
'あなたの好きな数字は、',option, 'です。'


# テキストボックスとスライダーをサイドバーに埋め込み
text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
st.sidebar.write('あなたの趣味：', text)

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50) # 0=最小値,100=最大値,50=デフォルト値
st.sidebar.write('コンディション：', condition)

# 詳しくは Streamlit公式ページの「Docs」→「REFERENCE GUIDES」→「API reference」→「Display interactive widgets」

# 2カラムレイアウトにする(左右)表示
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
        right_column.write('ここは右カラム')

# エキスパンダーの追加
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



