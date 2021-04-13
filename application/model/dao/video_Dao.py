from application.model.entity.video import Video
from application import video_list
from application import categoria_list

class VideoDAO:
    def __init__(self):
        self._video_list = video_list
    
    def definir_categoria(self, categoria_list):
        for categoria in categoria_list:
            for video in categoria.get_video_lista():
                video.set_categoria(categoria)

    def listar_video(self):
        return self._video_list
    
    def buscar_id(self,id):
        for i in self._video_list:
            if str(i.get_id()) == id:
                return i
                
            
            
        
    