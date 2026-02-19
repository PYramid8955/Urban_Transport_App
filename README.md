# Urban Transport App

> The app was developed to use multiple algorithms in order to generate an efficient route from an initial map (graph).

### The backend
> It works by generating clusters from the initial graph and finding hubs in those, then representing an abstracted graph using those hubs and running the same thing on that, until you get a single route (cluster) that connects the whole routes graph.
> The sequence in which each node is visited within routes is calculated using simulated annealing.
> It was a requirement not to use dijkstra (and some other algorithms), therefore A* was used (which is less efficient for Betweeness Centrality, but as it is run only once in the start, it's not a problem).

### The frontend
> The on the front-end side the user can view the routes and get the fastest route from station A to station B.
> We also include a log-in infrastructure for admins, that can delete an edge (road in construction), the route being redirrected automatically for that part.
> Also, the min-cost flow problem is solved for the most efficient way of distributing buses from garages to routes, which can be viewed from admin mode.
Admin mode access credinals:
> username: `owner`
> password: `pass12`

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PYramid8955/year_project.git
cd year_project
````

---

### 2️⃣ Create a Virtual Environment inside the project

Create the virtual environment in the root folder of the project:

#### 🔹 On macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔹 On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

After activation, your terminal should display `(venv)`.

---

### 3️⃣ Install Requirements

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

---

## 🚀 Running the Project

The server must be started **inside the `backend` folder**.

```bash
cd backend
uvicorn app.api.v1.api:app --reload
```

* `--reload` enables automatic reload when code changes.
* `app.api.v1.api:app` points to the FastAPI application instance.

---

## 🌐 Access the Application

Once the server is running, open your browser and go to:

```
http://localhost:8000
```

### 📚 Interactive API Documentation

FastAPI automatically generates interactive documentation:

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

You can test all endpoints directly from `/docs`.

---
