roomNumbers = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
instructors = {'CS101': 'Haynes', 'CS102': 'Alvaro', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
meetingTimes = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 a.m.'}

course = input('Enter a course number: ')
print(roomNumbers[course])
print(instructors[course])
print(meetingTimes[course])
