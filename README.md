# LangChain Agent API

## Description

The LangChain Agent API is a robust and scalable backend solution that simplifies inventory management by leveraging FastAPI and LangChain's AI capabilities. This project allows for efficient interaction with stock inventories, providing CRUD (Create, Read, Update, Delete) functionalities for inventory items. It integrates AI agents capable of handling various tasks related to inventory through natural language queries.

## Features

- **CRUD Operations:** Easily add, view, update, and delete inventory items.
- **AI Integration:** Use LangChain AI tools to manage inventory through natural language queries.
- **Asynchronous Operations:** Fast and efficient non-blocking operations using FastAPI and SQLAlchemy Async.
- **Configuration Management:** Environment variable support via `dotenv` for secure configuration.
- **Modular Design:** Well-structured codebase with clear separation of app layers and components, facilitating easy maintenance and extension.

## Installation

To run the LangChain Agent API locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/langchain-agent-api.git
   cd langchain-agent-api
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the root directory of your project and add the following variables:

   ```plaintext
   DATABASE_URL=your_database_url
   INVENTORY_API_URL=http://localhost:8000
   ```

5. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

## Usage

Use the following API endpoints to interact with the system:

- **Get all stocks:** `GET /stock/all`
- **Get stocks by category:** `GET /stock/categories/{category}`
- **Add a new stock item:** `POST /stock/add` with JSON payload
- **Delete a stock item by ID:** `DELETE /stock/delete/{stock_id}`

### Example

To add a new stock item to the inventory, send a POST request to `/stock/add` with the following JSON body:

```json
{
  "category": "electronics",
  "item": "headphones",
  "quantity": 50
}
```

### AI Agent Query

Use the AI agent to process a natural language query by sending a POST request to `/agent/query` with the following JSON body:

```json
{
  "query": "Add 20 jeans to the clothes category"
}
```

## License

This project is licensed under the terms of the [MIT License](https://github.com/KrishiDevani15/CRUD_Ai_Agent/blob/main/LICENSE).

---

This README provides a comprehensive overview of the LangChain Agent API project, covering its key functionalities and setup process. Make sure to customize the example URLs, endpoints, and sample payloads to reflect the actual implementation and unique aspects of your project.
