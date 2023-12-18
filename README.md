# my_Top_Ten


my_top_ten

This project is a Python application that utilizes the TMDb (The Movie Database) API to retrieve and display movie information.

Prerequisites:

Before running this project, you need to make sure you have the following:

Python 3.x installed on your machine

An API key from TMDb. You can obtain one by registering for a free account on the TMDb website: https://www.themoviedb.org/

Installation

Clone the project repository to your local machine:

``` python

git clone https://github.com/Shahid-Sheimi/my_top_ten.git

```

Navigate to the project directory:

``` python

cd my_top_ten

```

Install the project dependencies:

`` python 

pip install -r requirements.txt


```

Create a .env file in the project directory and add your TMDb API key to it:


TMDB_API_KEY=YOUR_API_KEY

Replace YOUR_API_KEY with your actual TMDb API key.

Usage

Run the following command to start the application:

bash

Copy code

python manage.py runserver 

python manage.py makemigrations 

python manage.py migrate 



The application will prompt you to enter a movie title. It will then fetch information about the movie from the TMDb API and display it in the console.

Contributing

If you would like to contribute to this project, you can:

Fork the repository

Create a new branch for your changes

Make your changes and commit them

Push your changes to your fork

Submit a pull request to the original repository

License

This project is licensed under the MIT License.

Acknowledgements

This project makes use of the TMDb API, which provides movie data. You can find more information about the TMDb API in their documentation: https://developers.themoviedb.org/3/getting-started/introduction

Before running this project, you need to make sure you have the following:

Python 3.x installed on your machine

An API key from TMDb. You can obtain one by registering for a free account on the TMDb website: https://www.themoviedb.org/

Build the Docker image by running the following command in the same directory as the Dockerfile:

bash

Copy code

docker build -t my_top_ten .

This will build the Docker image with the tag "my_top_ten" (you can choose any name you prefer), using the current directory (containing the Dockerfile) as the build context.

Step 5: Run a Docker container from the built image using the following command:

bash

Copy code

docker run -p 8000:8000 my_top_ten

This will start a Docker container from the image, and map port 8000 on the host to port 8000 on the container, allowing you to access the Django application in your local browser at http://localhost:8000/.
