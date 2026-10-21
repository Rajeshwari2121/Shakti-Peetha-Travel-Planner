# 🛕 Shakti Peetha Yatra
### An Interactive Temple Exploration and Travel Planning System Using Python and Streamlit

## 1. Project Overview

**Shakti Peetha Yatra** is an interactive, web-based pilgrimage exploration and travel planning application developed using Python, Streamlit, and Pandas.

The application focuses on the **18 Ashtadasha Shakti Peethas**, which hold religious and cultural significance in the Shakta tradition of Hinduism.

The project aims to combine traditional cultural information with modern digital technologies to create a centralized platform for exploring sacred destinations and planning pilgrimages.

The application provides temple information, location details, online photograph discovery, sightseeing information, accommodation references, transportation details, estimated travel expenses, and pilgrimage progress tracking.

**Hyderabad, Telangana, India**, is used as the reference starting location for travel planning.

The project demonstrates how data analytics, interactive web development, and visualization techniques can be integrated into a practical tourism and cultural heritage application.

---

## 2. Problem Statement

Planning a pilgrimage involving multiple Shakti Peethas can require collecting information from different websites and travel resources.

Travelers may need to research temple locations, available transportation, approximate distances, accommodation options, sightseeing destinations, and expected expenses separately.

This makes the planning process time-consuming and difficult to organize.

The **Shakti Peetha Yatra** project addresses this problem by bringing relevant information and planning tools together within a single interactive web application.

---

## 3. Project Objectives

The main objectives of the project are:

- To develop a centralized digital platform for exploring the 18 Ashtadasha Shakti Peethas.
- To provide structured information about temples, goddesses, locations, and cultural significance.
- To help users search and explore pilgrimage destinations.
- To display travel information from Hyderabad to selected destinations.
- To provide access to railway, airport, road, and transportation details available in the dataset.
- To estimate pilgrimage expenses based on user-defined travel preferences.
- To provide sightseeing and accommodation information.
- To integrate online temple photograph discovery.
- To track visited and remaining pilgrimage destinations.
- To demonstrate the practical application of Python, Pandas, Streamlit, and data visualization in tourism planning.

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web application framework |
| Pandas | Dataset loading, filtering, and processing |
| Requests | Retrieving online image search results |
| HTML | Custom interface elements |
| CSS | Website styling and layout customization |
| Google Maps | External route and location navigation |
| Wikimedia Commons API | Online photograph discovery |
| Streamlit Charts | Travel expense visualization |

### Programming Concepts Implemented

- DataFrame operations
- CSV data processing
- Conditional statements
- Functions
- Iteration and filtering
- String manipulation
- Regular expressions
- API requests
- Session-based interactive controls
- Dynamic calculations
- Web application development

---

## 5. Dataset Description

The project uses a structured CSV dataset containing information about the 18 Ashtadasha Shakti Peethas.

**Dataset File:**

`Ashtadasha_18_Shakti_Peethas_Final_No_Blanks.csv`

The dataset is the primary information source for the application.

### Dataset Information Categories

| Category | Information |
|---|---|
| Temple Identification | Shakti Peetha name and associated goddess |
| Geographical Information | Place, state, country, and region |
| Religious Information | Traditional significance and associated beliefs |
| Cultural Information | Cultural and historical descriptions |
| Natural Features | Relevant rivers, mountains, and geographical surroundings |
| Transportation | Road, railway, airport, and bus-related details |
| Travel Planning | Available distance and route information |
| Accommodation | Hotel and lodging references |
| Tourism | Nearby sightseeing destinations |
| Estimated Travel Details | Trip duration and other available planning information |

The application dynamically reads relevant columns from the dataset and displays the corresponding information.

The availability and completeness of individual fields depend on the supplied CSV data.

---

## 6. Application Architecture

The application follows a straightforward data-driven architecture.

**CSV Dataset → Pandas Data Processing → Streamlit Interface → Interactive Travel Planning**

### Stage 1: Data Loading

The application reads the CSV dataset using Pandas.

### Stage 2: Data Processing

The dataset is prepared for display, including column-name handling, text filtering, and information retrieval.

### Stage 3: User Interaction

Users select temples, search destinations, choose travel preferences, and enter budget parameters.

### Stage 4: Information Processing

The application retrieves temple details, calculates estimated expenses, and generates relevant information based on user selections.

### Stage 5: Result Presentation

Results are displayed using interactive cards, information sections, metrics, images, charts, and progress indicators.

---

## 7. Application Modules

### 7.1 Home Dashboard

The Home Dashboard is the main entry point of the application.

It provides an overview of the pilgrimage exploration system.

**Features:**

- Displays the total number of sacred destinations.
- Identifies Hyderabad as the reference starting city.
- Shows the currently selected Shakti Peetha.
- Presents temple names and location summaries.
- Provides navigation to other application modules.

**Purpose:**

To give users a clear introduction to the application and its available pilgrimage destinations.

### 7.2 Temple Explorer

The Temple Explorer module provides detailed information about individual Shakti Peethas.

Users can select a temple through the application's sidebar.

The module organizes available information into four sections:

**Temple Details**

Displays relevant information from the dataset, including location, goddess, cultural information, and other available attributes.

**Online Photos**

Provides a photograph search feature using the Wikimedia Commons API.

Users can search for online images associated with the selected temple.

Images are displayed within the application when matching results are returned.

**Sightseeing**

Displays available information about nearby tourist attractions and provides a Google Maps search link for additional sightseeing options.

**Hotels**

Displays accommodation-related information from the dataset and provides a link to search for hotels near the destination.

**Purpose:**

To provide a convenient interface for discovering sacred destinations and exploring their surrounding facilities.

**Important:** Online photograph search results are not automatically verified as photographs of the exact selected temple.

### 7.3 Travel Planner

The Travel Planner module helps users explore transportation information for their selected pilgrimage destination.

**Starting Location:** Hyderabad, Telangana, India.

**Features:**

- Displays available road distance information.
- Shows the nearest railway station when included in the dataset.
- Displays destination airport information when available.
- Presents transportation and route-related details.
- Provides Google Maps directions from Hyderabad to the selected destination.

**Purpose:**

To help travelers understand the geographical and transportation requirements of their pilgrimage.

The application does not directly book transportation tickets or provide live transport schedules.

### 7.4 Budget Planner

The Budget Planner is an interactive module designed to estimate pilgrimage expenses.

Users can enter:

- Number of travelers
- Number of travel days
- Preferred travel mode
- Hotel room cost per night
- Food cost per person per day

The application supports three travel modes:

- Bus
- Train
- Car

#### Budget Calculation

The total estimated travel expense is calculated as:

**Total Estimated Cost = Transportation Cost + Accommodation Cost + Food Cost**

Transportation expenses are estimated using the destination's available road distance and illustrative cost factors.

Accommodation expenses depend on the number of travelers, rooms required, trip duration, and hotel rate.

Food expenses depend on the number of travelers, number of days, and daily food budget.

#### Budget Visualization

The module presents:

- Estimated transportation cost
- Estimated accommodation cost
- Estimated food cost
- Overall estimated trip expense
- A bar chart comparing expense categories

**Purpose:**

To provide a simple and interactive financial planning tool for pilgrims.

**Limitation:** Budget results are illustrative estimates rather than live transport fares or verified hotel quotations. The bus and train estimates also use road distance as a proxy.

### 7.5 My Yatra – Pilgrimage Progress Tracker

The My Yatra module allows users to track their pilgrimage progress.

**Features:**

- Select temples already visited.
- Display the number of completed destinations.
- Calculate pilgrimage completion percentage.
- Display a progress bar.
- Identify remaining temples.

#### Completion Percentage

**Completion Percentage = (Number of Temples Visited / Total Number of Temples) × 100**

For example, if a user has visited 6 out of 18 temples:

**Completion Percentage = (6 / 18) × 100 = 33.33%**

**Purpose:**

To help users monitor pilgrimage progress and identify destinations they have not yet visited.

**Limitation:** The current implementation stores selections only during the active Streamlit session. It does not provide permanent user accounts or persistent travel history.

---

## 8. User Interface Design

The application uses a customized interface developed with Streamlit and CSS.

### Design Features

- Maroon, cream, and gold-inspired color scheme
- Interactive sidebar navigation
- Temple information cards
- Search and selection controls
- Tab-based information display
- Interactive budget inputs
- Summary metrics
- Cost visualization
- Pilgrimage progress indicators

The interface is designed to organize information clearly and make the application accessible to users with basic computer knowledge.

---

## 9. Search and Filtering

The application provides a text-based search feature.

Users can search for relevant temple names, places, states, countries, and goddess-related information where supported by the dataset.

### Search Process

1. The user enters a search term.
2. The application searches relevant dataset columns.
3. Matching destinations are identified.
4. The filtered results are made available for selection.
5. The user can explore the selected temple.

The search functionality uses Pandas-based text filtering.

---

## 10. Data Processing and Analytics

Pandas is used to manage and retrieve information from the CSV dataset.

The application performs operations such as:

- Reading CSV files
- Identifying relevant dataset columns
- Filtering temple records
- Retrieving selected destination information
- Extracting numeric distance values
- Calculating travel expenses
- Computing pilgrimage completion percentages
- Preparing data for charts

### Visualization

The application includes a bar chart comparing transportation, accommodation, and food expenses.

It also uses numerical indicators and progress bars to communicate travel-related information.

These features demonstrate the integration of basic data analytics and interactive visualization into a tourism planning application.

---

## 11. Key Project Features

- Exploration of 18 Ashtadasha Shakti Peethas
- Interactive temple selection
- Temple information display
- Location-based search
- Online photograph discovery
- Sightseeing information
- Accommodation references
- Hyderabad-based travel planning
- Google Maps navigation
- Travel budget estimation
- Expense visualization
- Pilgrimage progress tracking
- Customized Streamlit interface

---

## 12. Practical Applications

### Religious Tourism

Provides a digital resource for exploring sacred pilgrimage destinations.

### Travel Planning

Helps users review available transportation information and plan journeys.

### Budget Management

Supports preliminary financial planning through estimated expense calculations.

### Cultural Heritage Exploration

Presents information about religious destinations and their cultural significance.

### Educational Applications

Demonstrates the application of Python and interactive web technologies to a real-world dataset.

---

## 13. Project Outcomes

The project successfully demonstrates the development of an interactive, data-driven pilgrimage planning application.

### Major Outcomes

1. Developed a centralized application for exploring the 18 Ashtadasha Shakti Peethas.
2. Integrated structured temple and travel information into an interactive interface.
3. Implemented temple search and selection functionality.
4. Incorporated online image discovery and external map navigation.
5. Developed a user-defined travel budget calculator.
6. Implemented cost visualization using interactive charts.
7. Added pilgrimage progress tracking.
8. Demonstrated the use of Python, Pandas, Streamlit, and API integration in a practical application.

---

## 14. Project Limitations

The current implementation has several limitations:

- Online image search results may not represent the exact temple.
- Some temple and travel details depend on the completeness of the CSV dataset.
- Transport and hotel prices are not retrieved in real time.
- Budget calculations are illustrative estimates.
- Google Maps directions open through an external link.
- The pilgrimage checklist is not permanently saved.
- The application does not include ticket booking or hotel reservation functionality.
- International pilgrimage destinations may require additional visa, permit, or border-access verification.

---

## 15. Future Enhancements

The project can be extended with the following features:

- Verified temple photograph galleries
- Interactive geographical maps within the application
- Live transportation and accommodation information
- Multi-temple itinerary generation
- Personalized pilgrimage recommendations
- User authentication and saved travel histories
- Downloadable travel itineraries
- Mobile-friendly enhancements
- Regional language support
- More detailed travel analytics dashboards
- Improved distance and expense estimation
- Integration with authorized travel and accommodation services

---

## 16. Conclusion

**Shakti Peetha Yatra** is a data-driven pilgrimage exploration and travel planning application developed using Python and Streamlit.

The project combines structured information about the 18 Ashtadasha Shakti Peethas with interactive temple exploration, destination search, travel planning, estimated budget calculations, and pilgrimage progress tracking.

It demonstrates how programming, data processing, web development, and visualization techniques can be applied to cultural tourism and pilgrimage planning.

The application provides a foundation for developing more advanced digital pilgrimage management systems with improved geographical information, personalized travel planning, and additional interactive features.
