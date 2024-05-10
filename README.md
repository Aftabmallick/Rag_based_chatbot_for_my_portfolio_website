
# Context Aware Chatbot for Portfolio Website

Welcome to the README for our Context-Aware Chatbot project! This chatbot is designed to provide intelligent responses to user queries on our portfolio website. Below, you'll find information on how to set up and use the chatbot, as well as an overview of its components and functionalities.

## Overview

Our chatbot system utilizes advanced natural language processing techniques to understand user queries and generate contextually relevant responses. Key features include:

- Data ingestion and transformation for processing user input.
- Embedding techniques to represent text data in a meaningful way.
- Prediction module for generating responses based on user queries.
- Pipeline architecture for systematic data processing and response generation.
- Integration with external libraries such as OpenAI for enhanced language understanding.
- User-friendly interface powered by Streamlit for seamless interaction.

## Installation

To install and set up the chatbot system locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Ensure all necessary configuration files (e.g., `.env`) are properly set up.

## Usage

Once the setup is complete, you can interact with the chatbot system in the following ways:

- Run `python app.py` to start the chatbot interface.
- Use the provided commands (`python src/pipeline/update_pipeline.py -update` or `python src/pipeline/update_pipeline.py -delete`) for updating data as needed.

## Project Structure

The project follows a modular and organized structure:

- `src/components/`: Contains modules for data ingestion, transformation, embeddings, and prediction.
- `src/pipeline/`: Houses modules for pipeline management, including answer generation and data updating.
- `src/exception.py`: Handles exceptions within the codebase.
- `src/logger.py`: Provides logging functionality for monitoring.
- `src/utils.py`: Includes utility functions used throughout the project.
- `app.py`: Entry point for the chatbot application.
- `setup.py`: Defines project dependencies and metadata.

## Contributing

We welcome contributions to our chatbot project! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure all tests pass.
4. Submit a pull request detailing your changes and any relevant information.


## Contact

For any questions or inquiries, feel free to reach out to aftabmallick007@gmail.com or https://www.linkedin.com/in/aftab-mallick/

