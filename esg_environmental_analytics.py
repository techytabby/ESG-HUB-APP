import streamlit as st
import plotly.express as px
import pandas as pd


# import dotenv


def activfunc():
    @st.cache
    def get_data(url):
        return pd.read_csv(url)

    @st.cache
    def get_co2_data():
        url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
        return get_data(url)

    @st.cache
    def get_warming_data():
        # OWID Climate Change impacts

        url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Climate%20change%20impacts/Climate%20change%20impacts.csv'
        return get_data(url).query("Entity == 'World' and Year <=2022")

    df_co2 = get_co2_data()

    st.subheader("World CO2 Emissions Timeline")
    st.caption("The following below graph shows the CO2 emissions per capita by country over time.")

    year = st.slider('Select year', 1750, 2022)
    fig = px.choropleth(df_co2[df_co2['year'] == year], locations="iso_code",
                        color="co2_per_capita",
                        hover_name="country",
                        range_color=(0, 25),
                        color_continuous_scale=px.colors.sequential.Reds)
    st.plotly_chart(fig, use_container_width=True)

    default_countries = ['World', 'United States', 'United Kingdom', 'EU-27', 'China', 'Australia']
    countries = df_co2['country'].unique()

    selected_countries = st.multiselect('Select country or group', countries, default_countries)

    df3 = df_co2.query('country in @selected_countries')

    fig2 = px.line(df3, "year", "co2_per_capita", color="country")

    st.plotly_chart(fig2, use_container_width=True)