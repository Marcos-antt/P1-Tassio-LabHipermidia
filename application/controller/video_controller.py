from application import app
from application.model.dao.video_Dao import VideoDAO
from application.model.entity.video import Video
from application.model.dao.categoria_Dao import CategoriaDAO
from application.model.entity.categoria import Categoria
from flask import render_template, request, current_app
from application import video_list
from application import categoria_list

@app.route("/video/<video_id>", methods=['GET'])
def video(video_id):
    video_dao = VideoDAO()
    video=video_dao.buscar_id(video_id)
    return render_template("video.html", video = video)



