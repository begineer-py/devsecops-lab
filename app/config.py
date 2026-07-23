import os

# Application configuration
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

# 隨便亂改後面幾個字，只要維持 20 碼和 40 碼的長度就好
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7TEST123"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYTEST123456"
AWS_REGION = "us-east-1"

DATABASE_PATH = os.environ.get("DATABASE_PATH", "lab.db")
