import unittest
from intelligraph.graph import KnowledgeGraph
from intelligraph.sample_data import SAMPLE_PREREQUISITES
from intelligraph.recommender import recommend_path

class GraphTests(unittest.TestCase):
    def setUp(self): self.g=KnowledgeGraph(SAMPLE_PREREQUISITES)
    def test_prerequisite_order(self):
        p=self.g.learning_path("Machine Learning")
        self.assertLess(p.index("Python"),p.index("Pandas"))
        self.assertLess(p.index("Pandas"),p.index("Machine Learning"))
        self.assertLess(p.index("Statistics"),p.index("Probability"))
    def test_mastered_removed(self):
        p=self.g.learning_path("Machine Learning",["Python","NumPy"])
        self.assertNotIn("Python",p); self.assertNotIn("NumPy",p)
    def test_unknown_goal(self):
        with self.assertRaises(KeyError): self.g.learning_path("Unknown topic")
    def test_cycle_rejected(self):
        g=KnowledgeGraph({"A":[],"B":["A"]})
        with self.assertRaises(ValueError): g.add_prerequisite("A","B")
    def test_self_dependency_rejected(self):
        with self.assertRaises(ValueError): self.g.add_prerequisite("Python","Python")
    def test_recommendation_explanation(self):
        items=recommend_path(self.g,"Deep Learning")
        self.assertTrue(items); self.assertTrue(all(i["reason"] for i in items))
if __name__=="__main__": unittest.main()
