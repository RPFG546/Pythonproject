import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS questions")

cursor.execute("""
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option INTEGER NOT NULL
)
""")
questions = [
    ("Sebutan untuk hewan yang hidup di dua kondisi lingkungan","Reptil","Amfibi","Akuatik","Terestrial",2),
    ("Yang termasuk planet kerdil ialah","Mars","Merkurius","Uranus","Pluto",4),
    ("Benua terbesar ketiga di bumi","Eropa","Amerika utara","Asia","Amerika selatan",2),
    ("Julukan untuk benua Asia adalah","Benua kuning","Benua biru","Benua merah","Benua hijau",1),
    ("hasil dari 5 x 5 x -2","50","25","-25","-50",4),
    ("Yang merupakan bilangan prima","1","4","5","8",3)
]


cursor.executemany("""
INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
VALUES (?, ?, ?, ?, ?, ?)
""", questions)


conn.commit()
conn.close()

print("Database berhasil dibuat!")


