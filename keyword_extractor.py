import joblib
import ast
import sys
import warnings
from sklearn.exceptions import ConvergenceWarning

# Suppress all warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Load the trained model and vectorizer
clf = joblib.load('keyword_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

class CodeKeywordExtractor(ast.NodeVisitor):
    def __init__(self):
        self.keywords = {
            'functions': set(),
            'variables': set(),
            'classes': set(),
            'methods': set(),
            'control_structures': set(),
            'literals': set()
        }

    def visit_FunctionDef(self, node):
        self.keywords['functions'].add(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.keywords['classes'].add(node.name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.keywords['variables'].add(target.id)
        self.generic_visit(node)

    def visit_For(self, node):
        self.keywords['control_structures'].add('for')
        self.generic_visit(node)

    def visit_While(self, node):
        self.keywords['control_structures'].add('while')
        self.generic_visit(node)

    def visit_If(self, node):
        self.keywords['control_structures'].add('if')
        self.generic_visit(node)

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Str):
            self.keywords['literals'].add(node.value.s)
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float, str)):
            self.keywords['literals'].add(str(node.value))
        self.generic_visit(node)

    def visit_Name(self, node):
        self.keywords['variables'].add(node.id)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name):
            self.keywords['methods'].add(node.attr)
        self.generic_visit(node)

    def extract_keywords(self, source_code):
        tree = ast.parse(source_code)
        self.visit(tree)
        return self.keywords

def classify_keywords_from_code(source_code):
    extractor = CodeKeywordExtractor()
    ast_keywords = extractor.extract_keywords(source_code)
    keyword_list = []

    for category, items in ast_keywords.items():
        keyword_list.extend(items)

    if not keyword_list:
        print("\n[-] No keywords extracted from the source code.")
        return {}

    X_new = vectorizer.transform(keyword_list)
    predictions = clf.predict(X_new)
    labels = clf.classes_

    ml_keywords = {label: [] for label in labels}

    for keyword, pred in zip(keyword_list, predictions):
        ml_keywords[pred].append(keyword)

    # Filter out empty categories in ML results
    ml_keywords = {label: kw_list for label, kw_list in ml_keywords.items() if kw_list}

    # Combine AST and ML results
    combined_keywords = {}
    for category in ast_keywords:
        combined_keywords[category] = list(ast_keywords[category])
        if category in ml_keywords:
            combined_keywords[category].extend(ml_keywords[category])
            combined_keywords[category] = list(set(combined_keywords[category]))  # Remove duplicates

    return combined_keywords

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            keywords_from_code = classify_keywords_from_code(source_code)
            print("\n[+] Keywords from Code:\n")
            print("----------------------------\n")
            for label, keywords_list in keywords_from_code.items():
                print(f"[*] {label.capitalize()}:")
                for keyword in sorted(keywords_list):
                    print(f"  - {keyword}")
                print()  # Add an extra line for better readability
    except FileNotFoundError:
        print(f"\n[!] Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        process_file(file_path)
    else:
        file_path = input("\n[+] Please enter the path to the source code file: ")
        process_file(file_path)
