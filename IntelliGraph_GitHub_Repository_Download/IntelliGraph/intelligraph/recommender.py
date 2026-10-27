from .sample_data import SAMPLE_PREREQUISITES

CATALOG={
 "Python":("Practice","Functions, collections, and small Python scripts"),
 "NumPy":("Practice","Array operations and vectorization exercises"),
 "Pandas":("Practice","DataFrames, filtering, grouping, and missing data"),
 "Statistics":("Theory + practice","Descriptive statistics, distributions, and variance"),
 "Probability":("Theory + practice","Conditional probability, Bayes theorem, and random variables"),
 "Linear Algebra":("Theory + practice","Vectors, matrices, dot products, and matrix multiplication"),
 "Machine Learning":("Project","Build a supervised-learning model and evaluate it"),
 "Deep Learning":("Project","Implement a small neural network and compare metrics"),
 "SQL":("Practice","SELECT, JOIN, GROUP BY, and aggregate queries"),
 "Data Visualization":("Practice","Create plots and explain the pattern shown"),
}
def recommend_path(graph,target,mastered=()):
    path=graph.learning_path(target,mastered)
    return [{"step":i,"topic":t,"type":CATALOG.get(t,("Guided study","Review the core concepts and solve three exercises"))[0],
             "suggestion":CATALOG.get(t,("Guided study",f"Review {t} and solve three exercises"))[1],
             "reason":f"{t} is on the prerequisite chain for {target}." if t!=target else f"{target} is your selected goal."}
            for i,t in enumerate(path,1)]
