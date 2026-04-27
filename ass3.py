import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")

        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")

        except Exception as e:
            print(f"Error loading file: {e}")

        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for student in self.students[:n]:
            print(
                f"{student['student_id']} | {student['age']} | "
                f"{student['gender']} | {student['country']} | "
                f"GPA: {student['GPA']}"
            )

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        valid_students = []

        for student in self.students:
            try:
                float(student["final_exam_score"])
                float(student["GPA"])
                valid_students.append(student)

            except ValueError:
                print(f"Warning: could not convert value for student {student['student_id']} — skipping row.")

            except KeyError:
                print("Warning: missing column — skipping row.")

        sorted_students = sorted(
            valid_students,
            key=lambda student: float(student["final_exam_score"]),
            reverse=True
        )

        top10 = sorted_students[:10]

        top_10_list = []

        for i in range(len(top10)):
            student = top10[i]

            top_10_list.append({
                "rank": i + 1,
                "student_id": student["student_id"],
                "country": student["country"],
                "major": student["major"],
                "final_exam_score": float(student["final_exam_score"]),
                "GPA": float(student["GPA"])
            })

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top_10_list
        }

        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        for student in self.result["top_10"]:
            print(
                f"{student['rank']}. {student['student_id']} | "
                f"{student['country']} | {student['major']} | "
                f"Score: {student['final_exam_score']} | GPA: {student['GPA']}"
            )

        print("-" * 30)

    def lambda_filter_demo(self):
        print("-" * 30)
        print("Lambda / Map / Filter")
        print("-" * 30)

        try:
            top_scorers = list(
                filter(lambda student: float(student["final_exam_score"]) > 95, self.students)
            )

            gpa_values = list(
                map(lambda student: float(student["GPA"]), self.students)
            )

            good_assignments = list(
                 filter(lambda student: float(student["assignment_score"]) > 90, self.students)
            )

            print("Students with score > 95:", len(top_scorers))
            print("GPA values first 5:", gpa_values[:5])
            print("Students assignment > 90:", len(good_assignments))

        except ValueError:
            print("Error: some numeric values cannot be converted to float.")

        except KeyError as e:
            print(f"Error: missing column {e}")

        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                json.dump(self.result, file, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error saving file: {e}")


filename = "data.csv"

fm = FileManager(filename)

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

loader = DataLoader(filename)
students = loader.load()
loader.preview()

analyser = DataAnalyser(students)
analyser.analyse()
analyser.print_results()
analyser.lambda_filter_demo()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()

DataLoader("wrong_file.csv").load()