# Use the official Node.js image as the base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN npm install

# Expose the port that the application will run on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
