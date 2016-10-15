import webbrowser
   
class Movie():
    """This is a class to store movie information, title, story, poster, trailer, ratings...
    """ # will be added to __doc__ automatically
    # others
    #__name__ __module__ __dict__
    
    
    #VALID_RATINGS= ['G',"PG", "PG-13", "R"] # for constant variables
    
    def __init__(self, title, story, poster, trailer):
        
        self.title=title
        self.storyline=story
        self.poster_image_url=poster #image url
        self.trailer_youtube_url=trailer #trailer url
   
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
        
    def show_info(self):
        return self.title+'\n'+self.storyline
        
        
class TVShow(Movie): # Episodes are a nother kind os movie
    
    ''' To store tv show information, title, season, episode, trailer, tv station ...
    
    '''
    
    def __init__(self, title, story, poster, trailer, season, episode, station, ended):
        
        Movie.__init__(self, title, story, poster, trailer)

        self.season=season
        self.episode=episode
        self.station=station
        self.ended=ended
    
    def show_info(self):
        return Movie.show_info(self)+'\n'+self.season+" "+self.episode