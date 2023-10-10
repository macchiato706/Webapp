import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Show Progressbar')
'Start!'

latest_interaction=st.empty()
bar = st.progress(0)

for i in  range(100):
    latest_interaction.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.001)

'Done!'

left_column, right_colmun = st.columns(2)
button = left_column.button('Show text in right_colmun')
if button:
    right_colmun.write('This is right_colmun')

expander = st.expander('Request')
expander.write('White discription')




'''



text = st.text_input('What is your hobby?')
'Your hobby: ', text

cd = st.slider('How about your condition?', 0,100,50)
'Your condition: ', cd


option = st.selectbox(
    'Tell me your favorite number ',
    list(range(1,11))
)

'Your favorite number is ', option, '.' 




if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Maiko', use_column_width=True)






df= pd.DataFrame(
   np.random.rand(100,2)/[50,50] + [35.69, 139.70],
   columns=['lat','lon']
)
'''
#st.dataframe(df)
#st.dataframe(df.style.highlight_max(color = 'lightgreen', axis = 0))
#st.area_chart(df)
#st.map(df)




