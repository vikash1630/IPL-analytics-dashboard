# Use Python 3.10
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 10000 (Render uses this)
EXPOSE 10000

# Start app with gunicorn
CMD ["gunicorn", "APP:app", "-b", "0.0.0.0:10000"]
