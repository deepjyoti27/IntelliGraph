# IntelliGraph — Project Report

## Abstract
Students can struggle to decide what to learn next because advanced topics depend on prerequisite concepts. IntelliGraph is a prototype learning-path planner that models topics and prerequisites as a directed graph. For a selected goal, it identifies the transitive prerequisite set, orders topics using topological sorting, omits topics the learner marks as mastered, and attaches study suggestions and explanations. The implementation uses Python, Flask, adjacency-list graph storage, DFS cycle detection, graph traversal, and Kahn's algorithm. Recommendations are deterministic and the prototype does not use a trained AI model or independently verify mastery.

## Problem statement
Generic syllabi and playlists often fail to provide an individualized order that respects both prerequisite knowledge and what a learner already knows. IntelliGraph models these dependencies and generates a valid sequence toward a target goal while allowing learners to omit self-reported mastered topics.

## Objectives
- Represent topics and prerequisite links as a directed graph.
- Detect and reject cyclic dependencies.
- Discover transitive prerequisites for a target topic.
- Generate prerequisite-first learning paths.
- Exclude self-reported mastered topics.
- Explain each recommendation and expose graph/path JSON endpoints.

## Methodology and DSA
The adjacency list maps each topic to its prerequisite topics. DFS detects cycles. Graph traversal discovers the prerequisite closure. Kahn's topological sorting produces a prerequisite-first order. Set operations remove mastered topics. The Flask interface lets users choose a goal and prior knowledge.

## Architecture
1. Presentation: responsive HTML/CSS interface.
2. Application: Flask routes and request validation.
3. DSA engine: graph storage, cycle detection, prerequisite traversal, topological sorting.
4. Recommendation layer: rule-based suggestions and explanations.
5. Sample data: Python, NumPy, Pandas, Statistics, Probability, Linear Algebra, Machine Learning, Deep Learning, Data Visualization, and SQL.

## Implementation and validation
The repository includes a local web application, graph/path JSON endpoints, mastered-topic exclusion, cycle rejection, and unit tests for ordering, unknown goals, self-dependency, cycles, and recommendation explanations. Run the application and tests on the submission computer and record the actual observed results. No performance benchmark or user study is claimed.

## Complexity
For V topics and E prerequisite edges, adjacency-list storage is O(V+E). DFS cycle detection and prerequisite traversal are O(V+E). Kahn topological sorting is O(V+E), excluding sorting overhead for stable display.

## Limitations and future work
The curriculum is illustrative; recommendations are rule-based; mastery is self-reported. The prototype has no trained AI model, student accounts, quiz-based mastery, live resource retrieval, persistent profiles, or production security. Future enhancements include graph editing, persistent storage, assessment-derived mastery estimates, vetted resources, interactive graph visualization, natural-language goal parsing, multilingual support, and user evaluation.

## Conclusion
IntelliGraph demonstrates how graph data structures, DFS, graph traversal, and topological sorting can support an academic learning utility. It produces an explainable prerequisite-first path rather than an opaque recommendation and can serve as a base for further implementation and evaluation.
