# Twitch Stream Analytics Project

## Project Goals
The primary goal of this project is to analyze a streamer's Twitch streams in real-time, save the analytics data to a database, and use an AI agent to query the data to improve viewer engagement. The main objectives include:

1. **Real-Time Data Collection:** Collect data from Twitch streams, including viewer count, chat messages, and stream details.
2. **Data Storage:** Store the collected data in a database for further analysis.
3. **Data Analysis:** Analyze the data to identify patterns and insights that can help improve viewer engagement.
4. **AI Integration:** Use an AI agent to query the data and provide recommendations for improving streams and reaching a wider audience.
5. **Web Interface:** Develop a web interface to view live and historical data and interact with the AI agent.

## Accomplishments

1. **Twitch Data Collection:**
   - Implemented a script to authenticate with the Twitch API and fetch live stream data.
   - Set up a MongoDB database to store stream data, including game name, start time, comments, viewer count, and transcription.

2. **Twitch Chat Integration:**
   - Developed a Twitch chat bot to connect to Twitch's IRC server and collect chat messages in real-time.
   - Stored chat messages in MongoDB with timestamps.

3. **Audio Transcription:**
   - Used FFmpeg to capture audio from Twitch streams.
   - Implemented transcription using Google Cloud Speech-to-Text API.
   - Stored transcriptions in MongoDB with timestamps.

## To Be Implemented

1. **Stream End Time Tracking:**
   - Implement logic to update the `end_time` field when a stream ends.

2. **Web Interface Development:**
   - Create a web application to visualize live and historical data.
   - Implement a chat interface to interact with the AI agent.

3. **AI Integration:**
   - Set up an AI agent using OpenAI's API to query the database and provide insights.

4. **Optimization and Testing:**
   - Optimize the data collection and analysis processes for performance and scalability.
   - Test the system with real data to ensure accuracy and reliability.

## Getting Started

To get started with the project, follow these steps:

1. Set up a MongoDB database and update the connection details in the script.
2. Replace placeholders with your actual Twitch and Google Cloud credentials.
3. Run the scripts to start collecting data and storing it in the database.

## Requirements
- Python 3.x
- MongoDB
- FFmpeg
- Google Cloud Speech-to-Text API
- Twitch API credentials

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.