import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

def create_trait_rating_plot(df, selected_breed):
    # Filter the DataFrame based on the selected breed.
    filtered_df = df[df['breed'] == selected_breed].sort_values(by='rating', ascending=True)  
    
    # Create a horizontal bar plot
    fig, ax = plt.subplots(figsize=(12, 8)) 

    ax.barh(filtered_df['trait'], filtered_df['rating'], color='#cbe6de')  
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title(f'Ratings by Trait for {selected_breed}')

    # Set x-axis to show only integer values
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    
    # Set square boundary (spines) to light gray
    ax.spines['top'].set_color('#D3D3D3')
    ax.spines['bottom'].set_color('#D3D3D3')
    ax.spines['left'].set_color('#D3D3D3')
    ax.spines['right'].set_color('#D3D3D3')
    
    ax.tick_params(axis='x', which='major', labelsize=7)
    ax.tick_params(axis='y', which='major', labelsize=7)
    plt.tight_layout(pad=6.0)  # Adjust layout to make room for the content
    plt.subplots_adjust(left=0.3)
    
    return fig
