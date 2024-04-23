Determining workspace structure

Deciding which workspace information to collect

Gathering workspace info

# Bird-Watching Application

This application is a simple bird-watching tool that fetches and displays bird sightings based on user-defined geographical parameters. It uses the eBird API to fetch recent bird sightings and displays them on a map.

## Features

- Fetch bird sightings based on latitude, longitude, and radius.
- Display bird sightings on a map with markers.
- Each marker provides information about the bird sighting, including the common name, scientific name, and observation date.

## How to Run

This application is built with Python and uses the Streamlit library for the web interface. To run the application, you need to have Python installed on your machine.

1. Clone the repository:

```sh
git clone <repository-url>
```

2. Navigate to the project directory:

```sh
cd <project-directory>
```

3. Install the required Python packages:

```sh
pip install -r requirements.txt
```

4. Run the application:

```sh
streamlit run main.py
```

The application will start and be accessible at `http://localhost:8501`.

## Code Structure

The main logic of the application is contained in the [`main`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22main%22%5D "main.py") function in [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FMario%20Venere%20Neto%2FDocuments%2FProjetos%20Pessoais%2FGITHUB_CLONES%2FSIMPLEEBIRD%2FSimple_eBird%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Mario Venere Neto\Documents\Projetos Pessoais\GITHUB_CLONES\SIMPLEEBIRD\Simple_eBird\main.py"). This function sets up the Streamlit interface and calls the [`fetch_bird_sightings`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22fetch_bird_sightings%22%5D "main.py") function to fetch bird sightings based on the user's input.

The [`fetch_bird_sightings`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22fetch_bird_sightings%22%5D "main.py") function sends a GET request to the eBird API and returns the response data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.