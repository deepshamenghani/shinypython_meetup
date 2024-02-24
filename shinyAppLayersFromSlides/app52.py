from shiny import App, render, ui, reactive
import pandas as pd
from pathlib import Path
from trait_rating_plot import create_trait_rating_plot

df = pd.read_csv(Path(__file__).parent / "dog_traits.csv", na_values = "NA")
breeds = df.breed.unique().tolist()
traits = df.trait.unique().tolist()
dogimg_url = "https://camo.githubusercontent.com/97a9cd3442db4582637cacccfc9546801c05c4b98d23c23b85ffde9553a401f3/68747470733a2f2f6d656469612d636c646e72792e732d6e62636e6577732e636f6d2f696d6167652f75706c6f61642f6e657773636d732f323032305f32382f313538373636312f646f67732d6167652d79656172732d6b622d696e6c696e652d3230303730372e6a7067"

app_ui = ui.page_fillable(
    ui.page_sidebar(
        ui.sidebar(
            ui.input_select("inputbreed", label = "Select breed", choices = breeds, selected="Bulldogs"),
            ui.input_selectize(id = "inputtrait", label= "Select traits", choices = traits, multiple=True, selected="Adaptability Level"),
            ui.input_slider(id = "ratingmin", label="Minimum rating", min=1, max=5, value=1),
            ui.input_slider(id = "ratingmax", label="Maximum rating", min=1, max=5, value=5),
            ui.input_action_button("apply", "Apply settings", class_="btn-secondary"),
        ),
        ui.row(
            ui.column(6, ui.card(ui.tags.img(src=dogimg_url, height="100%", width="100%"))),
            ui.column(5, 
                ui.tags.h1("Who is the goodest doggy?!?"),
                ui.markdown("TidyTuesday dataset courtesy of [KKakey](https://github.com/kkakey/dog_traits_AKC/blob/main/README.md) sourced from the [American Kennel Club](https://www.akc.org/).")
            ),
        ),
        ui.layout_columns(
            ui.card(
            ui.card_header("Select the traits to update this plot"),
            ui.output_data_frame("dog_df"),
            ),
            ui.card(
                ui.card_header("Select the breed to update this plot"),
                ui.output_plot("breed_plot")
            ),
            gap = "2rem",
            col_widths={"sm": (5, 7)},
            height = "400px"
        )
    ),
)

def server(input, output, session):
    @reactive.Calc
    def filtered_ratings():
        filtered_rating = df[(df['rating'] >= input.ratingmin()) &
                     (df['rating'] <= input.ratingmax())]
        return filtered_rating.sort_values(by=["trait", "rating"], ascending=[True, False])
    
    @render.data_frame
    @reactive.event(input.apply, ignore_none=False)
    def dog_df():
        filtered_df = filtered_ratings()[(filtered_ratings()['trait'].isin(input.inputtrait()))]
        return filtered_df.sort_values(by=["trait", "rating"], ascending=[True, False])
    
    @render.plot
    @reactive.event(input.apply, ignore_none=False)
    def breed_plot():
        fig = create_trait_rating_plot(filtered_ratings(), input.inputbreed())
        return fig
    
app = App(app_ui, server)