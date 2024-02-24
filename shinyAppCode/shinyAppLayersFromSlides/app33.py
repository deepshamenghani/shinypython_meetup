from shiny import App, render, ui
import pandas as pd
from pathlib import Path
from trait_rating_plot import create_trait_rating_plot

df = pd.read_csv(Path(__file__).parent / "dog_traits.csv", na_values = "NA")
breeds = df.breed.unique().tolist()
traits = df.trait.unique().tolist()

app_ui = ui.page_fillable(
    ui.page_sidebar(
        ui.sidebar(
            ui.input_select("inputbreed", label = "Select breed", choices = breeds, selected="Bulldogs"),
            ui.input_selectize(id = "inputtrait", label= "Select traits", choices = traits, multiple=True, selected="Adaptability Level"),
            ui.input_slider(id = "ratingmin", label="Minimum rating", min=1, max=5, value=1),
            ui.input_slider(id = "ratingmax", label="Maximum rating", min=1, max=5, value=5),
        ),
        ui.output_data_frame("dog_df"),
        ui.output_plot("breed_plot")
    ),
)

def server(input, output, session):
    @render.data_frame
    def dog_df():
        filtered_df = df[(df['trait'].isin(input.inputtrait()))]
        return filtered_df.sort_values(by=["trait", "rating"], ascending=[True, False])
    
    @render.plot
    def breed_plot():
        df_updated = df.copy()
        fig = create_trait_rating_plot(df_updated, input.inputbreed())
        return fig
    
app = App(app_ui, server)

