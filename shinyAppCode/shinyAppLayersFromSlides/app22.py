from shiny import App, render, ui
import pandas as pd
from pathlib import Path
from trait_rating_plot import create_trait_rating_plot

df = pd.read_csv(Path(__file__).parent / "dog_traits.csv", na_values = "NA")
breeds = df.breed.unique().tolist()
traits = df.trait.unique().tolist()

app_ui = ui.page_fillable(
    ui.output_data_frame("dog_df"),
    ui.output_plot("breed_plot")
)

def server(input, output, session):
    @render.data_frame
    def dog_df():
        return df
    
    @render.plot
    def breed_plot():
        fig = create_trait_rating_plot(df, "Bulldogs")
        return fig
    
app = App(app_ui, server)
