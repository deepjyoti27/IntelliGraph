from flask import Flask, render_template, request, flash
from .graph import KnowledgeGraph
from .sample_data import SAMPLE_PREREQUISITES
from .recommender import recommend_path

app=Flask(__name__,template_folder="../templates",static_folder="../static")
app.secret_key="local-demo-key-change-before-deployment"
graph=KnowledgeGraph(SAMPLE_PREREQUISITES)

@app.route("/",methods=["GET","POST"])
def index():
    target="Machine Learning"; mastered=[]; path=[]
    if request.method=="POST":
        target=request.form.get("target","Machine Learning")
        mastered=request.form.getlist("mastered")
        try: path=recommend_path(graph,target,mastered)
        except KeyError:
            flash("Select a valid target topic."); target="Machine Learning"
    topics=sorted(graph.prerequisites)
    return render_template("index.html",topics=topics,target=target,mastered=mastered,path=path,connections=graph.connections())

@app.route("/api/graph")
def api_graph():
    return {"topics":graph.summary(),"edges":[{"from":a,"to":b} for a,b in graph.connections()]}

@app.route("/api/path")
def api_path():
    target=request.args.get("target","Machine Learning")
    mastered=[t.strip() for t in request.args.get("mastered","").split(",") if t.strip()]
    try: return {"target":target,"mastered":mastered,"path":recommend_path(graph,target,mastered)}
    except KeyError: return {"error":f"Unknown target topic: {target}"},400

if __name__=="__main__": app.run(debug=True)
