# Calculator API

## Overview

This project is a simple, Flask-based calculator API that provides basic arithmetic operations (addition, subtraction, multiplication, and division) through a RESTful interface. It's designed to be easily deployable on Vercel, making it accessible as a serverless function.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)


## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Xemum0/calc.git
   cd calc
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the API locally:

1. Start the Flask development server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

3. You can now make requests to the API, for example:
   ```
   http://localhost:5000/add/5/3
   ```

## API Documentation

### Base URL

When deployed, the base URL for all API endpoints will be:

```
https://calculatorsapi.vercel.app/
```



### Endpoints

#### Perform Calculation

Endpoint: `/<operation>/<number1>/<number2>`

Method: GET

Available operations:
- `add`: Addition
- `minus`: Subtraction
- `multiply`: Multiplication
- `divide`: Division

Parameters:
- `operation`: The arithmetic operation to perform (add, minus, multiply, divide)
- `number1`: The first operand (a floating-point number)
- `number2`: The second operand (a floating-point number)

#### Response Format

Success Response :
```json
 {
  "status": 200,
  "result": "the result of {operation} {number1} and {number2} is {result}"
   }

```

Error Response (400 Bad Request, 422 Unprocessable Entity, or 500 Internal Server Error):
```json
{
  "status": 400,
  "error": "Error description ('Invalid operation' or 'Division by zero' or 'An unexpected error occurred')"
}
```

### Examples


 1. Addition:
   ```
   https://calculatorsapi.vercel.app/add/5/3
   ```
   Response:
   ```json
   {
  "result": "the result of add 5.0 and 3.0 is 8.0",
  "status": "success"
   }
   ```

2. Division:
   ```
   https://calculatorsapi.vercel.app/divide/10/2
   ```
   Response:
   ```json
   {
  "result": "the result of divide 10.0 and 2.0 is 5.0",
  "status": "success"
   } ```
   


3. Division by Zero:
   ```
  https://calculatorsapi.vercel.app/divide/5/0
   ```
   Response:
   ```json
   {
  "message": "Division by zero",
  "status": "error"
  } ```



## Deployment

This API is designed to be deployed on Vercel. To deploy:

1. Install the Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts to deploy your application

After deployment, you'll receive a URL where your API is hosted.




