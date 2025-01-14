# Imports:
import io
from PIL import Image
import streamlit as st
import pandas as pd


# Title
st.title("Projet Downscaling")

# Text desciption presentation
st.write("Lorem ipsum dolor sit amet. Et consequatur velit sit fugit dolor a tenetur iure id ipsum molestiae ex molestiae provident? Et nostrum labore ut dolorem vitae et minus eaque eum quasi quisquam quo fuga minus aut nemo nihil cum delectus consequatur. Ad asperiores reprehenderit qui aliquam dicta ab voluptas praesentium. Et possimus porro et voluptas perspiciatis quo dicta nobis ut natus impedit. Id itaque consectetur id sunt ullam qui consequatur repellat aut optio quas sed pariatur dolores sed voluptates voluptatem aut voluptatum laboriosam.")

# An image of the model
image = Image.open('téléchargement.png')
st.image(image, caption='Image du modele', use_container_width=True)

# Text desciption of the model
st.write("Lorem ipsum dolor sit amet. Non nihil sint eum dolor aliquam At suscipit sint est nobis temporibus qui quos deleniti ut accusamus expedita sit adipisci accusantium.")

#Exemple of tables : -----------------------------------------------------------------------
#-Simple : 
data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Âge": [25, 30, 35],
    "Score": [95, 85, 90],
}
df = pd.DataFrame(data)
#-Styliser avec pandas si besoin
styled_df = df.style.map(
    lambda x: "color: red;" if isinstance(x, (int, float)) and x < 90 else "color: black;"
)
st.table(df)
st.table(styled_df)
#-Codé avec html pour controle total
html_code = """
<style>
    table {
        width: 50%;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid black;
        padding: 10px;
        text-align: center;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
</style>
<table>
    <thead>
        <tr>
            <th>Nom</th>
            <th>Âge</th>
            <th>Score</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>25</td>
            <td>95</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>30</td>
            <td>85</td>
        </tr>
        <tr>
            <td>Charlie</td>
            <td>35</td>
            <td>90</td>
        </tr>
    </tbody>
</table>
"""
st.markdown(html_code, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------

# Example of LR simulation
#video output_video with h264 codec
video_file_LR = open('output_video_h264.mp4', 'rb')
video_bytes_LR = video_file_LR.read()
st.video(video_bytes_LR)
st.text("Exemple de simulation LR")
video_file_LR.close()

# Example of HR output
#video output_video with h264 codec
video_file_HR = open('output_video_h264.mp4', 'rb')
video_bytes_HR = video_file_HR.read()
st.video(video_bytes_HR)
st.text("Exemple de sortie HR")
video_file_HR.close()

# Example of zoomed HR difficulties
#video output_video with h264 codec
video_file_zommedHR = open('output_video_h264.mp4', 'rb')
video_bytes_zommedHR = video_file_zommedHR.read()
st.video(video_bytes_zommedHR)
st.text("Exemple de zoom sur les difficultés HR")
video_file_zommedHR.close()

# Example of zoomed LR difficulties
#video output_video with h264 codec
video_file_zoomedLR = open('output_video_h264.mp4', 'rb')
video_bytes_zoomedLR = video_file_zoomedLR.read()
st.video(video_bytes_zoomedLR)
st.write("Exemple de zoom sur les difficultés LR")
video_file_zoomedLR.close()

# Our generation without interpolation
#video output_video with h264 codec
video_file_noInter = open('output_video_h264.mp4', 'rb')
video_bytes_noInter = video_file_noInter.read()
st.video(video_bytes_noInter)
st.text("Notre génération sans interpolation")
video_file_noInter.close()

# Our generation with interpolation
#video output_video with h264 codec
video_file_Inter = open('output_video_h264.mp4', 'rb')
video_bytes_Inter = video_file_Inter.read()
st.video(video_bytes_Inter)
st.text("Notre génération avec interpolation")

video_file_Inter.close()

# Our generation with interpolation + residual connections
#video output_video with h264 codec
video_file_InterResid = open('output_video_h264.mp4', 'rb')
video_bytes_InterResid = video_file_InterResid.read()
st.video(video_bytes_InterResid)
st.text("Notre génération avec interpolation + connexions résiduelles")
