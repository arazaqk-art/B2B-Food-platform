# B2B Food Platform

This is a Django-based B2B platform designed to connect food distributors with businesses. It allows distributors to manage their product inventory and for businesses to place orders from multiple distributors in a single cart.

## Key Features

*   **Distributor Management:** Add and manage food distributors.
*   **Product Catalog:** Distributors can list and manage their products, including price and stock.
*   **Split-Order Cart:** Businesses can add products from multiple distributors into a single shopping cart, and the system will handle creating separate orders for each distributor.
*   **User Authentication:** Separate login and registration for businesses and distributors.

## Tech Stack

*   **Backend:** Django, Django REST Framework
*   **Database:** SQLite (for development)
*   **Celery & Redis:** For handling background tasks (like sending order confirmation emails).

## 🚀 Getting Started

### Prerequisites

*   Python 3.11+
*   `pip` for package management

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd b2b-food-platform
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.
