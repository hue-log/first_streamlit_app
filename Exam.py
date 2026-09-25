
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import re

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CISA Exam Preparation App")
        self.root.geometry("800x750")
        self.root.configure(bg="#f4f6f9")
        
        self.questions = []
        self.current_q_index = 0
        self.selected_option = None
        
        self.setup_ui()
        self.load_sample_questions()
        
    def setup_ui(self):
        # Header
        self.header_frame = tk.Frame(self.root, bg="#2c3e50", height=50)
        self.header_frame.pack(fill='x')
        self.header_frame.pack_propagate(False)
        
        self.title_label = tk.Label(self.header_frame, text="CISA Exam Practice", bg="#2c3e50", fg="white", font=("Helvetica", 16, "bold"))
        self.title_label.pack(side='left', padx=20, pady=10)
        
        self.progress_label = tk.Label(self.header_frame, text="", bg="#2c3e50", fg="white", font=("Helvetica", 12))
        self.progress_label.pack(side='right', padx=20, pady=10)
        
        self.load_btn = tk.Button(self.header_frame, text="Load Full TXT File", command=self.load_from_file, bg="#3498db", fg="white", font=("Helvetica", 10), relief='flat', cursor='hand2')
        self.load_btn.pack(side='right', padx=10, pady=10)

        # Main Content Frame
        self.main_frame = tk.Frame(self.root, bg="#f4f6f9")
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Question
        self.q_label = tk.Label(self.main_frame, text="", font=("Helvetica", 12, "bold"), wraplength=700, justify='left', bg="#f4f6f9", fg="#2c3e50")
        self.q_label.pack(anchor='w', pady=(0, 15))
        
        # Options
        self.opt_frame = tk.Frame(self.main_frame, bg="#f4f6f9")
        self.opt_frame.pack(fill='x')
        self.opt_buttons = {}
        for key in ["A", "B", "C", "D"]:
            btn = tk.Button(self.opt_frame, text="", width=80, anchor='w', font=("Helvetica", 11), 
                            command=lambda k=key: self.select_option(k), relief='flat', bg="white", fg="#333",
                            activebackground="#cce5ff", activeforeground="#000", cursor='hand2',
                            highlightbackground="#ccc", highlightthickness=1)
            btn.pack(pady=5, fill='x')
            self.opt_buttons[key] = btn
            
        # Action Buttons
        self.btn_frame = tk.Frame(self.main_frame, bg="#f4f6f9")
        self.btn_frame.pack(pady=20)
        self.submit_btn = tk.Button(self.btn_frame, text="Submit Answer", command=self.submit_answer, bg="#27ae60", fg="white", font=("Helvetica", 11, "bold"), relief='flat', cursor='hand2', width=15)
        self.submit_btn.pack(side='left', padx=10)
        self.next_btn = tk.Button(self.btn_frame, text="Next Question", command=self.next_question, bg="#7f8c8d", fg="white", font=("Helvetica", 11, "bold"), relief='flat', cursor='hand2', width=15, state='disabled')
        self.next_btn.pack(side='left', padx=10)
        
        # Justification
        self.just_frame = tk.Frame(self.main_frame, bg="#f4f6f9")
        self.just_frame.pack(fill='both', expand=True, pady=(10, 0))
        self.just_label = tk.Label(self.just_frame, text="Explanation:", font=("Helvetica", 11, "bold"), anchor='w', bg="#f4f6f9", fg="#2c3e50")
        self.just_label.pack(anchor='w')
        
        self.just_text = scrolledtext.ScrolledText(self.just_frame, wrap='word', font=("Helvetica", 10), state='disabled', bg="#ecf0f1", fg="#2c3e50", relief='flat', padx=10, pady=10)
        self.just_text.pack(fill='both', expand=True)

    def load_sample_questions(self):
        # 10 Sample Questions embedded for immediate testing
        self.questions = [
            {"question": "1. Who should review and approve system deliverables as they are defined and accomplished, to ensure the successful completion and implementation of a new business system application?", "options": {"A": "User management", "B": "Project steering committee", "C": "Senior management", "D": "Quality assurance (QA) staff"}, "correct_answer": "A", "justification": "A. User management assumes ownership of the project and resulting system, allocates qualified representatives to the team, and actively participates in system requirements definition, acceptance testing and user training."},
            {"question": "2. Which of the following BEST helps to prioritize project activities and determine the timeline for a project?", "options": {"A": "Gantt chart", "B": "Earned value analysis", "C": "Program evaluation review technique (PERT)", "D": "Function point analysis"}, "correct_answer": "C", "justification": "C. The PERT method works on the principle of obtaining project timelines based on project events for three likely scenarios—worst, best and normal. The timeline is calculated by a predefined formula and identifies the critical path."},
            {"question": "3. An information systems (IS) auditor reviewing a series of completed projects finds that the implemented functionality often exceeded requirements and most of the projects ran significantly over budget. Which of these areas of the organization's project management process is the MOST likely cause of this issue?", "options": {"A": "Project scope management", "B": "Project time management", "C": "Project risk management", "D": "Project procurement management"}, "correct_answer": "A", "justification": "A. Because the implemented functionality is greater than what was required, the most likely cause of the budget issue is failure to effectively manage project scope."},
            {"question": "4. An information systems (IS) auditor is reviewing the software development process for an organization. Which of the following functions are appropriate for the end users to perform?", "options": {"A": "Program output testing", "B": "System configuration", "C": "Program logic specification", "D": "Performance tuning"}, "correct_answer": "A", "justification": "A. A user can test program output by checking the program input and comparing it with the system output. This task, although usually done by the programmer, can also be done effectively by the user."},
            {"question": "5. An information systems (IS) auditor is reviewing system development for a health care organization with two application environments-—production and test. During an interview, the auditor notes that production data are used in the test environment to test program changes. What is the MOST significant potential risk from this situation?", "options": {"A": "The test environment may not have adequate controls to ensure data accuracy.", "B": "The test environment may produce inaccurate results due to use of production data.", "C": "Hardware in the test environment may not be identical to the production environment.", "D": "The test environment may not have adequate access controls implemented to ensure data confidentiality."}, "correct_answer": "D", "justification": "D. In many cases, the test environment is not configured with the same access controls that are enabled in the production environment. If the test environment does not have adequate access control, the production data are subject to risk of unauthorized access and/or data disclosure."},
            {"question": "6. The information systems (IS) auditor is reviewing a recently completed conversion to a new enterprise resource planning system. In the final stage of the conversion process, the organization ran the old and new systems in parallel for 30 days before allowing the new system to run on its own. What is the MOST significant advantage to the organization by using this strategy?", "options": {"A": "Significant cost savings over other testing approaches", "B": "Assurance that new, faster hardware is compatible with the new system", "C": "Assurance that the new system meets functional requirements", "D": "Increased resiliency during the parallel processing time"}, "correct_answer": "C", "justification": "C. Parallel operation provides a high level of assurance that the new system functions properly compared to the old system, and therefore, the new system meets its functional requirements."},
            {"question": "7. What kind of software application testing is considered the final stage of testing and typically includes users outside of the development team?", "options": {"A": "Alpha testing", "B": "White box testing", "C": "Regression testing", "D": "Beta testing"}, "correct_answer": "D", "justification": "D. Beta testing is the final stage of testing and typically includes users outside of the development area. Beta testing is a form of user acceptance testing."},
            {"question": "8. During which phase of software application testing should an organization perform the testing of architectural design?", "options": {"A": "Acceptance testing", "B": "System testing", "C": "Integration testing", "D": "Unit testing"}, "correct_answer": "C", "justification": "C. Integration testing evaluates the connection of two or more components that pass information from one area to another. The objective is to use unit-tested modules, thus building an integrated structure according to the design."},
            {"question": "9. Which of the following is an advantage of an integrated test facility?", "options": {"A": "It uses actual master files or dummies, and the information systems (IS) auditor does not have to review the source of the transaction.", "B": "Periodic testing does not require separate test processes.", "C": "It validates application systems and ensures the correct operation of the system.", "D": "The need to prepare test data is eliminated."}, "correct_answer": "B", "justification": "B. An ITF creates a fictitious entity in the database to process test transactions simultaneously with live input. Its advantage is that periodic testing does not require separate test processes."},
            {"question": "10. An organization is replacing a payroll program that it developed in-house, with the relevant subsystem of a commercial enterprise resource planning (ERP) system. Which of the following represents the HIGHEST potential risk?", "options": {"A": "Undocumented approval of some project changes", "B": "Faulty migration of historical data from the old system to the new system", "C": "Incomplete testing of the standard functionality of the ERP subsystem", "D": "Duplication of existing payroll permissions on the new ERP subsystem"}, "correct_answer": "B", "justification": "B. The most significant risk after a payroll system conversion is loss of data integrity resulting in the organization being unable to pay employees in a timely and accurate manner."}
        ]
        self.load_question()

    def load_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                parsed_questions = self.parse_questions_from_text(text)
                if parsed_questions:
                    self.questions = parsed_questions
                    self.current_q_index = 0
                    self.load_question()
                    messagebox.showinfo("Success", f"Successfully loaded {len(self.questions)} questions!")
                else:
                    messagebox.showwarning("Warning", "No questions found. Please ensure the TXT file contains the raw text from the PDF.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def parse_questions_from_text(self, text):
        # Regex engine to parse the specific format from the PDF text dumps
        pattern = re.compile(
            r'(\d+)\.\s+(.*?)\n\s*A\.\s+(.*?)\n\s*B\.\s+(.*?)\n\s*C\.\s+(.*?)\n\s*D\.\s+(.*?)\n\s*([A-D]) is the correct answer\.\s*\n\s*Justification[:：]\s*\n(.*?)(?=\n\d+\.\s+|\Z)', 
            re.DOTALL
        )
        questions = []
        for match in pattern.finditer(text):
            q_num = match.group(1)
            q_text = match.group(2).strip().replace('\n', ' ')
            opt_a = match.group(3).strip()
            opt_b = match.group(4).strip()
            opt_c = match.group(5).strip()
            opt_d = match.group(6).strip()
            correct = match.group(7).strip()
            justification = match.group(8).strip()
            
            questions.append({
                "question": f"{q_num}. {q_text}",
                "options": {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d},
                "correct_answer": correct,
                "justification": justification
            })
        return questions

    def load_question(self):
        q = self.questions[self.current_q_index]
        self.progress_label.config(text=f"Question {self.current_q_index + 1} of {len(self.questions)}")
        self.q_label.config(text=q["question"])
        
        for key, btn in self.opt_buttons.items():
            btn.config(text=f"{key}. {q['options'][key]}", bg="white", fg="#333", state='normal')
            
        self.just_text.config(state='normal')
        self.just_text.delete('1.0', 'end')
        self.just_text.insert('1.0', "Submit your answer to see the explanation.")
        self.just_text.config(state='disabled')
        
        self.submit_btn.config(state='normal')
        self.next_btn.config(state='disabled')
        self.selected_option = None

    def select_option(self, key):
        if self.submit_btn['state'] == 'disabled':
            return
        self.selected_option = key
        for k, btn in self.opt_buttons.items():
            if k == key:
                btn.config(bg="#cce5ff") # Light blue for selection
            else:
                btn.config(bg="white")

    def submit_answer(self):
        if not self.selected_option:
            messagebox.showwarning("Warning", "Please select an option first!")
            return
            
        q = self.questions[self.current_q_index]
        correct = q["correct_answer"]
        
        for k, btn in self.opt_buttons.items():
            btn.config(state='disabled')
            if k == correct:
                btn.config(bg="#90EE90") # Green for correct answer
            elif k == self.selected_option and k != correct:
                btn.config(bg="#FFB6C1") # Red for wrong selection
                
        self.just_text.config(state='normal')
        self.just_text.delete('1.0', 'end')
        self.just_text.insert('1.0', q["justification"])
        self.just_text.config(state='disabled')
        
        self.submit_btn.config(state='disabled')
        self.next_btn.config(state='normal')

    def next_question(self):
        self.current_q_index += 1
        if self.current_q_index < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Finished", "Congratulations! You have completed all questions in this set.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
