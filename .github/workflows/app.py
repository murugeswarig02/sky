# Create src folder and add a file
mkdir -p src
echo "console.log('Hello World');" > src/app.js
git add src/app.js
git commit -m "Added app.js to src folder"
git push origin main
