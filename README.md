![moon logo](https://drive.google.com/uc?export=view&id=1WiQWrc3bD_dn11NhajC_Fxz8og-HLxCp)

Our product simplifies the objection management process for electronic Nomination Agreements (eNA) by consolidating it onto a single platform. This streamlines negotiation on eNA points, saving time for purchasers and facilitating reaching agreement with suppliers.

**Key Benefits:**

* Centralized Objection Management: All eNAs are listed on a single platform, enabling purchasers to easily track their progress and status.
* Easy Review and Editing: Each objection can be controlled, reviewed, and edited by the respective eNA purchaser, ensuring accuracy and transparency.
* Departmental Routing: The platform automatically routes objections to the relevant departments for review and response.
* Negotiation Support: Purchasers can utilize responses from responsible parties to effectively negotiate with suppliers.
* Finalized Contract Generation: Once all eNAs are finalized, an amended version is generated as a structured document ready to be attached to the original contract and sent to the supplier.
Overall, our product simplifies and streamlines the objection management process, saving time and effort for both purchasers and suppliers.

# Solution Diagram

<img src="https://drive.google.com/uc?export=view&id=1PcEoG_uzhAVaiSz7VxDSnBwk2PKPI0NZ" width=500>

# **Moon Handover: Modules**
## Module Documentation: Email Notifications

**Overview:**
The Email Notifications module facilitates the automatic sending of email notifications to alert departments and personnel about important updates or tasks. It comprises two main components: a router for handling incoming HTTP requests to trigger email sending and a utility service for actually sending the emails.

**Functionality:**
1. **Router (/routes/email.ts):**
    - The router defines an HTTP POST endpoint ('/') for receiving requests to send emails.
    - Upon receiving a request, it extracts the recipient's email address, email subject, and email body from the request body.
    - It then attempts to send the email using the `sendEmail` function from the utility service.
    - If successful, it responds with a JSON object indicating success and any relevant message. If an error occurs, it logs the error and responds with a 500 status code along with an error message.

2. **Email Service (/utils/emailService.ts):**
    - The `sendEmail` function is responsible for actually sending emails.
    - It uses the Nodemailer library to create a transporter with Gmail service credentials obtained from environment variables (`process.env.EMAIL_USER` and `process.env.EMAIL_PASSWORD`).
    - The email options (sender, recipient, subject, and body) are defined and passed to the transporter.
    - The email is sent asynchronously, and upon successful sending, it logs the response and returns a success message. If an error occurs, it logs the error and throws an exception.

**Deployment Considerations:**
- Ensure that environment variables `EMAIL_USER` and `EMAIL_PASSWORD` are correctly set to valid Gmail credentials.
- Securely manage and protect the environment variables, especially sensitive ones like passwords, using methods such as environment variables, configuration files, or a secrets manager.

**Integration:**
- Integrate this module into your backend system by mounting the router in your Express application.
- Make sure to handle errors gracefully, especially when dealing with sensitive data like email credentials.

**Example:**
```typescript
import express from 'express';
import emailRouter from './routes/email';

const app = express();

// Mount the email router
app.use('/email', emailRouter);

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
```
**Next steps**
Ensure proper configuration and error handling to leverage automatic email notifications effectively.


## Module Documentation: eNA Point Finder Module

**Description**

The eNA Point Finder module is designed to locate and retrieve specific points identified by their associated numbers from a database. This module is particularly useful for applications requiring the retrieval of text or data associated with specific numeric identifiers, such as articles, documents, or records.

**Code Overview**

`enaArticles.ts`

This file contains the controller functions responsible for handling requests related to eNA points.

`getAllNumbers`

- **Description:** Retrieves all available numbers of eNA points from the database.
- **HTTP Method:** GET
- **Route:** `/numbers`
- **Functionality:**
  - Establishes a connection to the PostgreSQL database.
  - Executes a SQL query to select all numbers from the `ena_article` table.
  - Responds with the retrieved numbers in JSON format.
- **Error Handling:**
  - Logs and returns a 500 status code in case of database connection or query errors.

`getTextByNumber`

- **Description:** Retrieves the text associated with a specific eNA point number from the database.
- **HTTP Method:** GET
- **Route:** `/text/:number`
- **Functionality:**
  - Extracts the eNA point number from the request parameters.
  - Establishes a connection to the PostgreSQL database.
  - Executes a SQL query to select the text associated with the provided eNA point number from the `ena_article` table.
  - Responds with the retrieved text in JSON format if found, otherwise returns a 404 status code.
- **Error Handling:**
  - Logs and returns a 500 status code in case of database connection or query errors.

`enaArticles.ts`

This file contains the route definitions for handling requests related to eNA points.

- Imports the controller functions `getAllNumbers` and `getTextByNumber`.
- Defines routes for retrieving all numbers (`/numbers`) and text by number (`/text/:number`).

**Example**

Suppose you have a database containing articles indexed by eNA points, where each article is associated with a unique number. Using this module and code, you can easily retrieve all available eNA point numbers or obtain the text of a specific eNA point by its number.

_Retrieving All eNA Point Numbers_

- **HTTP Request:**
  ```
  GET /numbers
  ```
- **Response:**
  ```json
  {
    "message": "Numbers retrieved successfully",
    "data": [123, 456, 789]
  }
  ```

_Retrieving Text by eNA Point Number_

- **HTTP Request:**
  ```
  GET /text/123
  ```
- **Response:**
  ```json
  {
    "message": "Text retrieved successfully",
    "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
  }
  ```

In this example, requesting the text associated with eNA point number 123 returns the corresponding text stored in the database.

## **Module Documentation: Centralized eNA Negotiations Management**

**Overview**
The eNA Negotiations Management Modules provides a centralized solution for efficiently managing electronic negotiation agreements (eNA) within the system. It allows users to add, retrieve, and access negotiation details through a set of RESTful API endpoints.

**Functionality**

1. **Adding a Negotiation:**
   - Endpoint: POST `/negotiation/`
   - Description: Adds a new negotiation to the system with provided details such as eNA number, company information, and contact emails.
   - Request Body Parameters:
     - `ena`: Electronic negotiation agreement number
     - `company`: Name of the company associated with the negotiation
     - `address`: Address of the company
     - `duns`: DUNS number of the company
     - `supplier`: Name of the supplier
     - `supplier_email`: Email of the supplier
     - `engineer`: Name of the engineer
     - `engineer_email`: Email of the engineer
     - `po`: Purchase order number
     - `po_email`: Email associated with the purchase order
   - Response:
     - HTTP Status Code 201 on success with JSON response containing the added negotiation details.
     - HTTP Status Code 400 if a negotiation with the same eNA number already exists.
     - HTTP Status Code 500 on server error.

2. **Fetching All Negotiations**
   - Endpoint: GET `/negotiation/`
   - Description: Retrieves all negotiations from the system with optional parameters for pagination and filtering by purchase order number.
   - Query Parameters:
     - `skip`: Number of records to skip (for pagination)
     - `limit`: Maximum number of records to return (for pagination)
     - `po`: Filter by purchase order number
   - Response:
     - HTTP Status Code 200 on success with JSON response containing an array of negotiation objects.
     - HTTP Status Code 500 on server error.

3. **Fetching PO Email by eNA**
   - Endpoint: GET `/negotiation/:ena/po-email`
   - Description: Retrieves the email associated with the purchase order of a negotiation based on the provided eNA number.
   - Path Parameter:
     - `ena`: Electronic negotiation agreement number
   - Response:
     - HTTP Status Code 200 on success with JSON response containing the purchase order email.
     - HTTP Status Code 404 if no negotiation found with the provided eNA number.
     - HTTP Status Code 500 on server error.

## **Module Documentation: Centralized Management of eNA Objections**

**Overview**

The centralized management Module provides a convenient location to handle eNA (presumably a system or entity) objections effectively. It offers an overview of open eNA incidents, facilitating streamlined management and resolution processes.

**Functionality**

The Module consists of backend routes and controllers implemented using Express.js, a popular Node.js web application framework.

**Code Structure**

1. **Routes (objection.ts):**
   - Defines the endpoints for adding objections and retrieving objections by eNA.
   - POST endpoint ('/') for adding objections.
   - GET endpoint ('/:ena') for retrieving objections by eNA identifier.

2. **Controllers (objection.ts):**
   - Contains functions to handle HTTP requests and interact with the database.
   - `addObjection`: Handles the addition of objections to the database.
   - `getObjectionsByEna`: Retrieves objections based on the provided eNA identifier.

**Implementation**

1. **Adding Objections (addObjection):**
   - Accepts POST requests with parameters including eNA identifier, article number, reason, and suggestion.
   - Inserts the objection details into the database table named "objection".
   - Responds with a success message and the inserted objection data.

2. **Retrieving Objections by eNA (getObjectionsByEna):**
   - Accepts GET requests with the eNA identifier as a parameter.
   - Queries the database for objections associated with the provided eNA identifier.
   - Responds with a list of objections matching the eNA identifier.

**Error Handling:**

- Proper error handling is implemented, ensuring robustness against database connection issues or query failures.
- Errors are appropriately logged, and relevant HTTP status codes are returned to the client.

**Example Usage:**

Suppose there's a system managing objections raised by different entities within an organization. Developers can utilize the provided routes to integrate objection management functionality into the system's backend. For instance:
- When an objection is raised, a POST request is sent to the '/objection' endpoint with relevant details.
- To view objections related to a specific eNA, a GET request is made to '/objection/:ena', where ":ena" is replaced with the eNA identifier.

This Module enhances operational efficiency by centralizing objection management, allowing authorized users to track, address, and resolve objections effectively.

## **Module Documentation: AI suggested final agreement RAG module Documentation**

**Overview**
Large Language Models (LLMs) are trained on vast datasets, yet they lack training on your specific data. Retrieval-Augmented Generation (RAG) addresses this gap by incorporating your data alongside the existing datasets accessible to LLMs.
The RAG module is an important component of our system, focusing on generating contextually relevant responses by combining retrieval and generation techniques. Leveraging the LlamaIndex library, it integrates advanced text processing capabilities with an external AI model (OpenAI's GPT-3.5 Turbo) to generate contextually relevant answers. RAG is particularly suitable for scenarios requiring precise and informative responses, such as negotiations or inquiries within a corporate environment.

<img src="https://docs.llamaindex.ai/en/stable/_static/getting_started/basic_rag.png" width="600">

**Functionality**

The RAG module consists of the following functionalities:

1. **Contextual Response Synthesis**
   - The module accepts incoming queries along with contextual information.
   - It leverages LlamaIndex's capabilities to synthesize responses based on the provided context and query.

2. **Integration with OpenAI**
   - Utilizes the GPT-3.5 Turbo model from OpenAI to generate responses.
   - Configurable parameters such as model settings and temperature ensure flexibility in response generation.
   - OpenAI places a high priority on data security and privacy. According to the information provided in the extracts: Data sent to the OpenAI API is not used to train or improve OpenAI models.

3. **Knowledge Retrieval** 
   - Retrieves relevant knowledge from a knowledge base or corpus based on the provided context.
   - Incorporates retrieved knowledge into the response generation process, enriching the generated responses.
   - Input context is represented as a document using LlamaIndex's `Document` class.

4. **Response Refinement**
   - Custom response prompts are generated to provide clear and concise answers to queries.
   - Configurable parameters such as model settings and temperature enable customization of response generation.

**Usage**

1. **Initialization**
   - Upon receiving a request, the RAG module initializes the OpenAI model with specified settings.
   - It creates a document object representing the provided context.

2. **Response Synthesis**
   - Combines retrieved knowledge with generative techniques to produce contextually relevant responses.
   - A custom prompt is generated based on the context and query, guiding the AI model to produce relevant responses.
   - LlamaIndex's ResponseSynthesizer orchestrates the response generation process, ensuring coherence and accuracy.

3. **Query Execution**
   - The document, along with the generated prompt which contains the Supplier name, eNA point number and Reason for objection, is passed to the OpenAI model for eNA final agreement text generation.
   - The model processes the input and generates a response based on the context and query.

4. **Error Handling**
   - Robust error handling mechanisms are implemented to handle exceptions gracefully.
   - Errors encountered during response synthesis or query execution are logged and appropriate error responses are returned.

**Integration**

The RAG module seamlessly integrates with existing Express.js applications:
- It exposes an endpoint '/rag' to receive HTTP POST requests containing context and queries (Supplier name, eNA point number and Reason for objection).
- Upon receiving a request, it invokes the response synthesis process and returns the generated response to the client.

**Deployment**

- The RAG module can be deployed as part of the broader application stack.
- It relies on external dependencies such as LlamaIndex and OpenAI's GPT-3.5 Turbo model.
- Deployment configurations, including port settings and environment variables, can be managed using tools like dotenv.
**Note:** Ensure compatibility with Node.js version 18 or higher for optimal functionality, as required by LlamaIndex.


## **Maintaining the Local text.ts File for RAG**

The local text.ts file serves as a crucial resource for the retrieval part of the Retrieval-Augmented Generation (RAG) module. It contains essential data points such as 'Supplier', 'eNApoint number', 'Reason for objection', 'Comments', and 'Final agreement text', formatted as paragraphs. Regular updates, ideally 1-2 times a month, ensure that the RAG module suggests pre-defined and approved final agreement wordings for a wide range of cases. 

For privacy and compliance purposes, sensitive data such as 'Comments' and 'Final agreement text' can be anonymized either manually or through automated processes. Tools like Google's De-identification API, Microsoft Presidio, or open-source models for Personally Identifiable Information (PII) masking such as ai4privacy can assist in this process.

**Next Steps**

* Consider implementing a data pipeline that automatically transforms information stored in the database into the text file format. This pipeline would extract relevant data fields ('Supplier', 'eNApoint number', 'Reason for objection', 'Comments', and 'Final agreement text') from the database and organize them into paragraphs within text file(s). In this case the ingestion function should be updated according to the format of the text file. Automating this process streamlines data management and ensures the text file remains updated with the latest information from the database.
* Storing the indexes in the vector database such as Pinecone or ChromaDB can be considered as the next step of updating the RAG module.
* Consider exploring cost-saving opportunities by transitioning to open-source Large Language Models (LLMs) such as `open-mistral-7b` from Mistral AI or `gemma-1.1-7b-it` from Google. These open-source LLMs offer powerful language processing capabilities while potentially reducing maintenance costs associated with proprietary solutions. Evaluate the suitability of these models for your application's requirements and budget constraints to make an informed decision about the transition.

# **Moon Handover: Product Roadmap**

As we transition the Moon app to its next phase, we're excited to share our plans for upcoming features and enhancements. Here's a glimpse into the most critical 10 features that are remaining on our roadmap:

1. **Login Page Enhancement:** Enhance the login page to improve user experience and security.
   
2. **Departments Filtering:** Implement advanced filtering options to streamline navigation and organization within departments.
   
3. **Assigning Responsible Personnel:** Introduce functionality to assign and manage responsible personnel for specific tasks or incidents.
      
4. **Visibility of MAN Comment Column:** Enhance visibility and accessibility of MAN comment columns for improved collaboration and decision-making.
   
5. **MAN Comment History:** Provide access to the history of MAN comments for better tracking and auditing purposes.
   
6. **Export Functionality:** Introduce export functionality to allow users to export data for further analysis or reporting.
   
7. **PDF Format Support:** Enable exporting data in PDF format for easy sharing and printing.
   
8. **Excel Format Support:** Provide support for exporting data in Excel format, ensuring compatibility with various data analysis tools.
   
9. **Status of eNA Incidents:** Implement a feature to track and display the status of eNA incidents, providing transparency and accountability.

# **Developer guide**
## **Repo structure**
<details>
  <summary><b>Backend</b></summary>

```
└── .📁backend-express
    └── .env
    └── .env.template
    └── .gitignore
    └── .prettierrc
    └── const.ts
    └── 📁constants
        └── prompt.ts
        └── template.ts
        └── text.ts
        └── userData.ts
    └── 📁controllers
        └── enaArticles.ts
        └── negotiation.ts
        └── objection.ts
        └── openai.ts
    └── db.ts
    └── index.ts
    └── package-lock.json
    └── package.json
    └── pnpm-lock.yaml
    └── 📁routes
        └── email.ts
        └── enaArticles.ts
        └── negotiation.ts
        └── objection.ts
        └── rag.ts
    └── tsconfig.json
    └── 📁utils
        └── emailService.ts
        └── openai.ts
```

</details>

<details>
  <summary><b>Frontend</b></summary>


```
└── .📁frontend
    └── .DS_Store
    └── .env.template
    └── .eslintrc.cjs
    └── .gitignore
    └── .prettierrc
    └── Dockerfile
    └── README.md
    └── index.html
    └── nginx.conf
    └── package-lock.json
    └── package.json
    └── pnpm-lock.yaml
    └── postcss.config.js
    └── 📁public
        └── dps_favicon.png
        └── dps_touchicon.png
    └── 📁src
        └── .DS_Store
        └── App.css
        └── App.tsx
        └── 📁assets
            └── DPS.svg
            └── Upload.svg
            └── arrow-down.svg
            └── arrow-up.svg
            └── avatar.jpg
            └── create_btn.svg
            └── delete-icon.svg
            └── doneLoading.svg
            └── eightyPercentLoading.svg
            └── fortyPercentLoading.svg
            └── generic-photo.png
            └── login.png
            └── sixtyPercentLoading.svg
            └── stageFour.png
            └── stageOne.png
            └── stageThree.png
            └── stageTwo.png
            └── startNewCommunication.png
            └── submitButton.png
            └── tenPercentLoading.svg
            └── twentyPercentLoading.svg
        └── 📁components
            └── .DS_Store
            └── addCommentsForm.tsx
            └── allCommentsTable.tsx
            └── communicationInformationForm.tsx
            └── departmentCard.tsx
            └── emptyWorklistDisplay.tsx
            └── navbar.tsx
            └── startCommunicationDisplay.tsx
            └── worklistTable.tsx
        └── const.ts
        └── index.css
        └── main.tsx
        └── oldApp.tsx
        └── 📁pages
            └── CommunicationInfo.tsx
            └── allComments.tsx
            └── commentsSubmitted.tsx
            └── contracts.tsx
            └── emptyWorklist.tsx
            └── login.tsx
            └── supplierCommentsForm.tsx
            └── worklist.tsx
        └── vite-env.d.ts
    └── tailwind.config.js
    └── tsconfig.json
    └── tsconfig.node.json
    └── vite.config.ts
```

</details>


## Database Diagram

<img src="https://drive.google.com/uc?export=view&id=1UKJzPodaoHNQy9ITEyEtlMMvgvquSaCZ" width=800>

## Deployment Guide
1. Clone this project
2. Make sure you have Node.JS, React, npm, and Tailwind CSS installed.
3. Set up your local PostgreSQL DB using the `DB_setup.txt` file provided and configure it properly in your local `.env` file.
4. Run `npm install` in both `../backend-express` and `../frontend` folders.
5. Run `npm run dev` in both `../backend-express` and `../frontend` folders to start the backend and frontend.
6. You should be able to see the login page on http://localhost:8080/

## Secrets

### OpenAI 

**Secret Name**

OPENAI_API_KEY

**Obtain**
To obtain an OpenAI API key, follow these steps:

1. Login Open AI account.
1. Go to [API Keys Page](https://platform.openai.com/api-keys).
1. Click "Create new secret key" button.
1. Put it as a secret to the Github Actions page.


# Rag_contract_finder_and_experiments
