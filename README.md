# Rate Limiter & Micro Projects



### Overview

This project focuses on the development of a rate limiter system implemented in Python along with various micro projects. The rate
limiter system is designed to regulate the number of requests per time interval, with a flexible user interface for toggling between
different limiting techniques and customizing request limits. The project also includes the implementation of microservices using
different technologies to determine the optimal solution. Future goals involve deploying the system in a clustered, cloud-based
environment.



### File Structure
```
Client/
├── tsconfig.json
├── tailwind.config.ts
├── postcss.config.js
├── package.json
├── package-lock.json
├── next.config.mjs
├── README.md
├── .gitignore
├── .eslintrc.json
├── src/
│   ├── favicon.ico
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
└── public/
    ├── next.svg
    └── vercel.svg

server-py/
├── .gitignore
├── .python-version
├── README.md
├── __main__.py
└── requirements.txt
```


### Setup Instructions

##### Client (Next.js)

1. Navigate to the Client directory.
2. Run npm install to install dependencies.
3. Start the development server with npm run dev.
4. Open http://localhost:3000 in your browser to access the application.

##### Server (Python)

1. Navigate to the server-py directory.
2. Create a virtual environment with python -m venv .venv.
3. Activate the virtual environment:
    * Linux/Mac: source .venv/bin/activate
    * Windows: .venv\Scripts\activate
4. Install required packages with pip install -r requirements.txt.



### Usage

Once both the client and server environments are set up, interact with the rate limiter system via the client-side user interface. Detailed instructions on interacting with specific components can be found in their respective directories.



### Authors
<br>Sean Ippolito
<br>Sean Celik
<br>Sean Pearce



### Contribution Guidelines

Contributions to the project are welcome! Please follow the guidelines outlined below. For any questions or suggestions, feel free to open an issue or reach out to the project maintainers.



### Additional Information

##### Client (Next.js) README

This Next.js project is initialized with create-next-app and serves as the frontend component of the rate limiter system. Refer to the individual README file within the Client directory for more detailed information on setup, usage, and deployment.

##### Server (Python) README

The server-side Python application implements the rate limiter backend. Refer to the individual README file within the server-py directory for setup instructions, goals, and additional project details.
