questions = [
      "1.What is the output of: print(2**3)?",
      "A. 5",
      "B. 6",
      "C. 7",
      "D. 8",
      "2.Which of these is a correct syntax to create a Python dictionary",
      "A. { 'name': 'Jhon', 'Age': 30 }",
      "B. ( 'name': 'Jhon', 'Age': 30 )",
      "C. [ 'name': 'Jhon', 'Age': 30 ]",
      "D. < 'name': 'Jhon', 'Age': 30 >",
      "3.What does the len() function do?",
      "A. Returns the number of elements in a list",
      "B. Returns the number of characters in a string",
      "C. Returns the number of key-value pairs in a dictionary",
      "D. All the above",          
]

answers = ["D","A","D"]

score = 0
for i in range(len(answers)):
  print(questions[i * 5])
  for j in range (1,5):
    print(questions[i * 5 + j])
  user_answer = input("Enter your answer (A,B,C or D):").upper()
  if user_answer == answers[i]:
    print("Correction!\n")
    score += 1
  else:
    print(f"Wrong! The correct answer is {answers[i]}\n")
print(f"Your final score is: {score} out of {len(answers)}")