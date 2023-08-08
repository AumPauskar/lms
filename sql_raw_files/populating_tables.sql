-- SAMPLE BOOK INFO
-- THIS VALUE IS A SAMPLE DATASET TO TEST THE PROGRAM

-- BOOKS TABLE, 20 VALUES
USE lms;
INSERT INTO books (NAME, AUTHOR, STOCK) VALUES
("The Night Circus", "Erin Morgenstern", 12),
("The Power of One", "Bryce Courtenay", 7),
("Neverwhere", "Neil Gaiman", 15),
("The Goldfinch", "Donna Tartt", 9),
("The Book Thief", "Markus Zusak", 11),
("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 18),
("Dune", "Frank Herbert", 5),
("The Handmaid's Tale", "Margaret Atwood", 14),
("The Alchemist", "Paulo Coelho", 20),
("1984", "George Orwell", 8),
("The Picture of Dorian Gray", "Oscar Wilde", 6),
("The Hobbit", "J.R.R. Tolkien", 17),
("To Kill a Mockingbird", "Harper Lee", 10),
("Brave New World", "Aldous Huxley", 4),
("Pride and Prejudice", "Jane Austen", 13),
("The Catcher in the Rye", "J.D. Salinger", 3),
("The Great Gatsby", "F. Scott Fitzgerald", 16),
("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 19),
("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", 2),
("The Da Vinci Code", "Dan Brown", 6);

-- STUDENTS TABLE, 20 VALUES
INSERT INTO students (NAME, EMAIL, BOOKS_BORROWED, FINES) VALUES
("John Doe", "john@example.com", 0, 0.00),
("Jane Smith", "jane@example.com", 0, 0.00),
("Alice Johnson", "alice@example.com", 0, 0.00),
("Michael Brown", "michael@example.com", 0, 0.00),
("Emily Williams", "emily@example.com", 0, 0.00),
("Daniel Martinez", "daniel@example.com", 0, 0.00),
("Olivia Johnson", "olivia@example.com", 0, 0.00),
("William Davis", "william@example.com", 0, 0.00),
("Sophia Garcia", "sophia@example.com", 0, 0.00),
("Alexander Rodriguez", "alexander@example.com", 0, 0.00),
("Isabella Smith", "isabella@example.com", 0, 0.00),
("Ethan Johnson", "ethan@example.com", 0, 0.00),
("Emma Wilson", "emma@example.com", 0, 0.00),
("James Anderson", "james@example.com", 0, 0.00),
("Ava Martinez", "ava@example.com", 0, 0.00),
("Benjamin Brown", "benjamin@example.com", 0, 0.00),
("Mia Taylor", "mia@example.com", 0, 0.00),
("Logan Moore", "logan@example.com", 0, 0.00),
("Abigail Harris", "abigail@example.com", 0, 0.00),
("Lucas Wilson", "lucas@example.com", 0, 0.00);

-- FACULTIES TABLE, 20 VALUES
INSERT INTO faculties (NAME, EMAIL, BOOKS_BORROWED, FINES) VALUES
("Harper Lee", "harper@example.com", 0, 0.00),
("Liam Thomas", "liam@example.com", 0, 0.00),
("Ella Martinez", "ella@example.com", 0, 0.00),
("Jackson Johnson", "jackson@example.com", 0, 0.00),
("Scarlett Davis", "scarlett@example.com", 0, 0.00),
("Aiden Smith", "aiden@example.com", 0, 0.00),
("Grace Brown", "grace@example.com", 0, 0.00),
("Lucas Martinez", "lucas2@example.com", 0, 0.00),
("Chloe Wilson", "chloe@example.com", 0, 0.00),
("Liam Anderson", "liam2@example.com", 0, 0.00),
("Zoe Harris", "zoe@example.com", 0, 0.00),
("Noah Davis", "noah@example.com", 0, 0.00),
("Lily Johnson", "lily@example.com", 0, 0.00),
("Carter Smith", "carter@example.com", 0, 0.00),
("Aria Brown", "aria@example.com", 0, 0.00),
("Elijah Wilson", "elijah@example.com", 0, 0.00),
("Penelope Martinez", "penelope@example.com", 0, 0.00),
("Grayson Johnson", "grayson@example.com", 0, 0.00),
("Sofia Anderson", "sofia@example.com", 0, 0.00),
("Mia Johnson", "mia.johnson@example.com", 0, 0.00);