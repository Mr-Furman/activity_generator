
### 1. Clone the project:
https://github.com/Mr-Furman/activity_generator.git
### 2. Create virtual environment
### python3 -m venv venv
### 3. Activate virtual environment according to your OS
 pip install -r requirements.txt

### Variant 1 (SQL lite)
 command

 python command.py new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5

### Variant 2(Postgres)
1. Create .env (use env.example)
2. cd terminal into folder db_postgres
3. docker-compouse up --build
4. change code in command.py (line 5, 55, 77)
5. python command.py new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5
'''