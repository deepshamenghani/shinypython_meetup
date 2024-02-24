from shiny import App, render, ui
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "dog_traits.csv", na_values = "NA")
breeds = df.breed.unique().tolist()
traits = df.trait.unique().tolist()

app_ui = ui.page_fillable(
    ui.output_data_frame("dog_df")
)

def server(input, output, session):
    @render.data_frame
    def dog_df():
        return df
    
app = App(app_ui, server)
