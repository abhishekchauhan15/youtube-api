# YouTube Video Fetch API

This project is a Flask-based API to fetch and store YouTube videos based on a predefined search query. The videos are stored in a MongoDB database, and the API provides endpoints for paginated retrieval and searching.

## Project Structure

- `app.py`: Main Flask application file.
- `requirements.txt`: Dependencies required for the project.
- `README.md`: Project documentation.
- ...

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure MongoDB:
    - Ensure MongoDB is running.
    - Update MongoDB connection details in `app.py`.

4. Set up YouTube API Key:
    - Replace the placeholder API key in `app.py` with your YouTube API key.

5. Run the application:

    ```bash
    python app.py
    ```

6. Access the API:

    - Test connection: [http://127.0.0.1:5000/hello](http://127.0.0.1:5000/hello)
    - Paginated videos: [http://127.0.0.1:5000/videos](http://127.0.0.1:5000/videos)
    - Search videos: [http://127.0.0.1:5000/search?query=your-query](http://127.0.0.1:5000/search?query=your-query)

## API Endpoints

- `/hello`: Test API connection.
- `/videos`: Get paginated videos.
- `/search`: Search videos based on a query.

## Background Job

A background job is set up to continuously fetch and store videos from YouTube every 10 seconds.
.

## Notes

- Make sure MongoDB is properly configured and running.
- API keys should be kept secure. Consider using environment variables for sensitive information.

  ![image](https://github.com/abhishekchauhan15/youtube-api/assets/76480451/90984380-6e6c-4810-b3b0-52ba71b2d5ae)

  ![image](https://github.com/abhishekchauhan15/youtube-api/assets/76480451/1165ae1d-3302-482e-8357-dcb72b208ddf)



## Contributions

Contributions are welcome! If you find any issues or have improvements, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
