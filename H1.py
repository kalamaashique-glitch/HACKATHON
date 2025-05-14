
import cv2
import pandas as pd
import streamlit as st

# Load colors dataset
colors = pd.read_csv('colors.csv', names=['Color', 'ColorName', 'Hex', 'R', 'G', 'B'], header=None)

def get_color_name(R, G, B):
    minimum = float('inf')
    cname = ''
    for i in range(len(colors)):
        d = abs(R - colors.loc[i, 'R']) + abs(G - colors.loc[i, 'G']) + abs(B - colors.loc[i, 'B'])
        if d < minimum:
            minimum = d
            cname = colors.loc[i, 'ColorName']
    return cname

# Streamlit UI
st.title('Color Detection App')
image_file = st.file_uploader('Upload an Image', type=['jpg', 'png', 'jpeg'])

if image_file:
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), 1)
    st.image(image, channels='BGR')

    if st.button('Detect Color'):
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                b, g, r = image[y, x]
                color_name = get_color_name(r, g, b)
                st.write(f'Color: {color_name}, RGB: ({r}, {g}, {b})')

        cv2.imshow('Image', image)
        cv2.setMouseCallback('Image', click_event)
        cv2.waitKey(0)