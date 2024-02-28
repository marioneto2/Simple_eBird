import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
import random

# Function to fetch bird sightings from eBird API
def fetch_bird_sightings(lat, lon, radius):
    url = f"https://api.ebird.org/v2/data/obs/geo/recent?lat={lat}&lng={lon}&dist={radius}"
    headers = {"X-eBirdApiToken": "6espeb0ltr5a"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit app
def main():
    st.title("Bird-Watching Application")

    # Sidebar
    st.sidebar.header("Search Parameters")
    lat = st.sidebar.number_input("Latitude", value=-15.603534)
    lon = st.sidebar.number_input("Longitude", value=-56.056648)
    radius = st.sidebar.slider("Radius (km)", min_value=1, max_value=100, value=10)

    # Fetch bird sightings
    bird_sightings = fetch_bird_sightings(lat, lon, radius)
    if bird_sightings:
        st.success(f"Found {len(bird_sightings)} bird sightings within {radius} km radius.")

        mymap = folium.Map(location=[lat, lon], zoom_start=10)
        for sighting in bird_sightings:
            # Add small random offset to latitude and longitude
            lat_offset = random.uniform(-0.0001, 0.0001)
            lon_offset = random.uniform(-0.0001, 0.0001)
            marker_lat = sighting["lat"] + lat_offset
            marker_lon = sighting["lng"] + lon_offset

            folium.Marker([marker_lat, marker_lon],
                          popup=f"{sighting['comName']} ({sighting['sciName']})\n{str(sighting['obsDt'])}",
                          icon=folium.Icon(color="blue")).add_to(mymap)

        # Display map
        folium_static(mymap)
    else:
        st.error("Failed to fetch bird sightings. Please check your input parameters or try again later.")

if __name__ == "__main__":
    main()
