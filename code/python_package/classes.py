# --------------------------------------------------------------------------------------------------------
# ------------------------------------------------ Classes -----------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 1. dependencies and setup -----------------------------------------------------------------------------/
from python_package.helpers import *  # liberaries and functions
# -------------------------------------------------------------------------------------------------------/

# 2. defining statistic classes -------------------------------------------------------------------------/
class Statistics():
    stat_var     = ["mean", "median", "var", "std", "sem"]
    m            = ""
    y_name       = None
    def __init__(self, input_df, param, output_df=pd.DataFrame({}), gpvar="month"):
        self.input_df  = input_df
        self.param     = param
        self.gpvar     = gpvar
        self.output_df = output_df
        
    def set_gpvar(self, gpvar):
        self.gpvar     = gpvar
        
    def set_stats(self,sort_by=["mean","std"]):
        self.output_df = self.input_df.groupby([self.gpvar]).agg({self.param:Statistics.stat_var})
        self.output_df = self.output_df.sort_values([(self.param,i) for i in sort_by],ascending=True)
        
    def get_stats(self):
        return self.output_df
    
    def save_stats(self):
        self.output_df.to_csv(OUTPUT_PATH+self.param+".csv")
        
    def get_month_value(self):
        low_month=self.output_df.index[0]
        print(f"""Month with Lowest Value: {low_month}""")
        high_month=self.output_df.index[-1]
        print(f"""Month with Highest Value: {high_month}""")
    
    def set_plot(self,i="mean",j="std"):                 
        if i in Statistics.stat_var:
            Statistics.set_label(self.param,i)
            bar_chart (self.output_df,
                       Statistics.m,
                       self.output_df[(self.param,j)],
                       self.gpvar.capitalize(),
                       Statistics.y_name)
        else:
            raise ValueError(f"input variable {i} is not in the dataframe")
    
    @classmethod
    def set_label(cls,tag,i):
        cls.m      = (tag,i) 
        cls.y_name = "Average " + tag.capitalize()
# -------------------------------------------------------------------------------------------------------/        

# 3. defining news scraping classes ---------------------------------------------------------------------/ 
class Mars_News():
    mars_list     = []
    name=""
    
    def __init__(self, articles):
        self.articles  = articles
        
    def set_news_summary(self):
        for article in self.articles:
            title = article.find("div", class_="content_title").text
            preview = article.find("div", class_="article_teaser_body").text
            news_dict = {
                "title": title,
                "preview": preview
            }
            Mars_News.mars_list.append(news_dict)
        
    def get_news_summary(self):
        return Mars_News.mars_list
    
    def dataframe(self):
        self.news_df=pd.DataFrame(Mars_News.mars_list)
        return self.news_df
    
    def save_results(self, name_id="News"):
        Mars_News.set_name(name_id)
        self.news_df.to_csv(OUTPUT_PATH+Mars_News.name+".csv")
        json_save_file = open(OUTPUT_PATH+Mars_News.name+".json", "w")
        js.dump(Mars_News.mars_list, json_save_file, indent=4)
        json_save_file.close()  
        
    
    @classmethod
    def set_name(cls,name_id):
        cls.name      = name_id.capitalize()+"_Result_Data" 
# -------------------------------------------------------------------------------------------------------/
