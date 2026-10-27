# IntelliGraph — AI-Based Knowledge Graph for Academic Learning

**DSA-II academic project | Prototype v1.0**

IntelliGraph is a prerequisite-aware academic learning path planner. It models topics and their prerequisite relationships as a directed graph, identifies all prerequisites for a selected goal, omits topics the learner marks as already mastered, and returns an explainable prerequisite-first sequence with study suggestions.

## Implemented features
- Adjacency-list directed graph
- DFS cycle detection; cyclic dependencies and self-dependencies are rejected
- Transitive prerequisite discovery
- Kahn topological sort for prerequisite-first sequencing
- Mastered-topic exclusion
- Explainable, rule-based recommendation catalogue
- Responsive Flask web interface
- JSON endpoints: `/api/graph`, `/api/path?target=Machine%20Learning&mastered=Python,NumPy`
- Unit tests for ordering, mastery exclusion, invalid targets, cycle checks, and explanations

## Run on Windows
Python 3.10+ recommended.
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m intelligraph.app
```
Open `http://127.0.0.1:5000`.

If PowerShell activation is blocked:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m intelligraph.app
```

## Tests
```powershell
python -m unittest discover -s tests -v
```

## API
- `GET /api/graph` returns topics and edges.
- `GET /api/path?target=Deep%20Learning&mastered=Python,NumPy` returns the ordered path.
- Unknown targets return HTTP 400.

## Data model
`prerequisites[topic] = [required_topic_1, ...]`. For example, `Machine Learning: [Pandas, Probability, Linear Algebra]` means these topics should appear before Machine Learning.

## Complexity
For V topics and E edges: adjacency-list storage O(V+E); DFS cycle detection O(V+E); prerequisite traversal O(V+E); Kahn topological sort O(V+E), excluding sorting overhead for stable display.

## Honest scope and limitations
This is a working prototype with illustrative sample curriculum data and deterministic rules. It does not include a trained AI model, student accounts, quiz-verified mastery, live resource search, persistent user profiles, or production deployment/security. The UI does not edit the graph. Future work could add assessment-derived mastery confidence, vetted resources, graph visualization, natural-language goal parsing, multilingual interaction, and persistent storage.

## Submission evidence
Run the application and capture genuine screenshots from your own computer: home page, generated path, mastered-topic exclusion, `/api/graph` JSON, and successful unit-test output. Do not present conceptual mockups as execution evidence.
