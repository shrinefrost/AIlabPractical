# ================== Student Help Desk – FAQs ==================
# 1. How can I take admission in the college?
# 2. What is the admission process?
# 3. What are the eligibility criteria for admission?
# 4. What is the last date to apply for admission?
# 5. Is any entrance exam required for admission?
#
# 6. What is the fee structure of the course?
# 7. How can I pay my college fees?
# 8. Is fee installment facility available?
# 9. What is the refund policy for fees?
# 10. Is there any late fee fine?
#
# 11. Which courses are available in the college?
# 12. What subjects are included in this semester?
# 13. What is the duration of the course?
# 14. Where can I find the syllabus?
# 15. Is the course available in online or offline mode?
#
# 16. When will the exams be conducted?
# 17. Where can I check the exam timetable?
# 18. How can I download my admit card?
# 19. When will the exam results be declared?
# 20. What is the passing criteria for exams?
#
# 21. What is the minimum attendance required?
# 22. Is attendance mandatory for all subjects?
# 23. What happens if attendance is short?
# 24. Can I apply for medical leave?
#
# 25. What are the library timings?
# 26. How many books can I issue from the library?
# 27. For how many days can I keep a library book?
# 28. What is the late fine for library books?
# 29. How can I renew a library book?
#
# 30. Is scholarship available for students?
# 31. How can I apply for a scholarship?
# 32. What are the eligibility criteria for scholarship?
# 33. Are government scholarships accepted?
#
# 34. Is hostel facility available?
# 35. What are the hostel fees?
# 36. Is mess facility available in the hostel?
# 37. Is Wi-Fi available on campus?
# 38. Is transport or bus facility available?
#
# 39. Does the college provide placement support?
# 40. Which companies visit the campus for placement?
# 41. Are internships available for students?
# 42. What is the placement percentage of the college?
#
# 43. How can I get my college ID card?
# 44. How can I apply for a bonafide certificate?
# 45. How can I get a character certificate?
# 46. How can I get a migration certificate?
#
# 47. Whom should I contact for academic issues?
# 48. Whom should I contact for technical issues?
# 49. How can I reset my student portal password?
# 50. How can I contact the student help desk?
# =============================================================


def rule_based_bot(user_input):
    if "admission" in user_input or "enroll" in user_input:
        return "Admission process starts in June. Please visit the college website"
    elif "fees" in user_input or "payment" in user_input:
        return "Fees can be paid online or at account office"
    elif "exam" in user_input or "result" in user_input:
        return "Exam schedule and results are available on the student portal."

    elif "library" in user_input or "book" in user_input:
        return "You can issue up to 3 books for 14 days from the library."

    else:
        return "Sorry, I didn't understand. Please contact the help desk."


print(" !!!!!!!!!!           Hello I am a chatbot. Feel free to ask any academic queries      !!!!!!!!!!!!!!!!!!     ")

# Taking user input
while True:
    print()
    print(" ⚡⚡Note⚡⚡ : Type exit to end chat")
    user_input = input("How can I assit you 😊: ")
    if user_input=="exit":
        print("👋👋👋👋Nice talking to you bye!🙌🙌🙌🙌")
        break
    print()
    print("Your querry 👱: ",user_input)
    print("Bot Response 🤖:",rule_based_bot(user_input))
