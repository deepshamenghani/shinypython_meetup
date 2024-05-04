from shiny import App, render, ui, reactive
import pandas as pd
from pathlib import Path
from trait_rating_plot import create_trait_rating_plot
from shinyswatch import theme

df = pd.read_csv(Path(__file__).parent / "dog_traits.csv", na_values = "NA")
breeds = df.breed.unique().tolist()
traits = df.trait.unique().tolist()
dogimg_url = "https://images.unsplash.com/photo-1444212477490-ca407925329e?q=80&w=1856&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

app_ui = ui.page_fillable(
    theme.minty(),
    ui.page_sidebar(
        ui.sidebar(
            ui.input_select("inputbreed", label = "Select breed", choices = breeds, selected="Bulldogs"),
            ui.input_selectize(id = "inputtrait", label= "Select traits", choices = traits, multiple=True, selected="Adaptability Level"),
            ui.input_checkbox("show", "Set limits for ratings", False),
            ui.panel_conditional(
                "input.show", 
                ui.input_slider(id = "ratingmin", label="Minimum rating", min=1, max=5, value=1),
                ui.input_slider(id = "ratingmax", label="Maximum rating", min=1, max=5, value=5),
            ),
            ui.input_action_button("apply", "Apply settings", class_="btn-secondary"),
            bg="#f6e7e8", open="open"
        ),
        ui.row(
            ui.column(6, ui.tags.img(src=dogimg_url, height="90%", width="100%")),
            ui.column(5,
                ui.panel_absolute(  
                    ui.panel_well(
                        ui.tags.h1("Who is the goodest doggy?!?"),
                        ui.markdown("Data: Synthetic dog trait ratings inspired by TidyTuesday dataset courtesy of [KKakey](https://github.com/kkakey/dog_traits_AKC/blob/main/README.md) sourced from the [American Kennel Club](https://www.akc.org/)."),
                        ui.markdown("Photo by [Anoir Chafik](https://unsplash.com/@anoirchafik?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/selective-focus-photography-of-three-brown-puppies-2_3c4dIFYFU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)")
                    ),
                    width="400px",  
                    right="75px",  
                    draggable=False,  
                )
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