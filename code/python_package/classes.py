# defining statistic classes
class Statistics():
    STATS_COLUMNS      = ["mean", "median", "var", "std", "sem"]
    PLOT_PARAM         = ""
    y_name= None
    def __init__(self, input_df, param, output_df=pd.DataFrame({}), gpvar="month"):
        self.input_df  = input_df
        self.param     = param
        self.gpvar     = gpvar
        self.output_df = output_df
        
    def set_gpvar(self, gpvar):
        self.gpvar     = gpvar
        
    def set_stats(self,sort_by=["mean","std"]):
        self.output_df = self.input_df.groupby([self.gpvar]).agg({self.param:Statistics.STATS_COLUMNS})
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
        if i in Statistics.STATS_COLUMNS:
            Statistics.set_label(self.param,i)
            bar_chart (self.output_df,
                       Statistics.PLOT_PARAM,
                       self.output_df[(self.param,j)],
                       self.gpvar,
                       Statistics.y_name)
        else:
            raise ValueError(f"input variable {i} is not in the dataframe")
    
    @classmethod
    def set_label(cls,tag,i):
        cls.PLOT_PARAM      = (tag,i) 
        cls.y_name = "average " + i
        