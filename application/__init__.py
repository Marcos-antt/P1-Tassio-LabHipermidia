from flask import Flask
import os
from application.model.entity.categoria import Categoria
from application.model.entity.video import Video

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)


video1 = Video(1,"Ryu Vs Ken","Da hadukee Ryu!",'img/img_video/stf.jpg','stf1.mp4')
video2 = Video(2,"Naruto Vs Sasuke","Rivalidade e Amizade.",'img/img_video/shonen1.jpg','shonen1.webm')
video2 = Video(3,"Naruto Vs Sasuke","Rivalidade e Amizade.",'img/img_video/shonen1.jpg','shonen1.webm')
video2 = Video(3,"Naruto Vs Sasuke","Rivalidade e Amizade.",'img/img_video/shonen1.jpg','shonen1.webm')

video_list = [video1, video2]

categoria_list = []
categoria1 = Categoria(1,"Luta","Nesta Categoria você irá acompanhar os melhores animes de luta",'img/img_categoria/stf1.jpg',[video1])
categoria2 = Categoria(2,"Shonen","Nesta Categoria você irá acompanhar os melhores animes do estilo Shonen",'img/img_categoria/shonen1.jpg',[video2])
categoria_list = [categoria1,categoria2]

from application.controller import index_controller
from application.controller import video_controller

